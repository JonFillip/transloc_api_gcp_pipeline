import argparse
import time
import logging
import json
import typing
from datetime import datetime
import requests
import apache_beam as beam
from apache_beam import window
from apache_beam.options.pipeline_options import GoogleCloudOptions, PipelineOptions, StandardOptions
from apache_beam.transforms.sql import SqlTransform
from apache_beam.runners import DataflowRunner, DirectRunner
from apache_beam.io.gcp.bigquery import BigQueryDisposition, WriteToBigQuery
from apache_beam.io.gcp.bigquery_tools import parse_table_schema_from_json




class ArrivalEstimate(typing.NamedTuple):
    route_id: str
    arrival_at: str
    stop_id: str

beam.coders.registry.register_coder(ArrivalEstimate, beam.coders.RowCoder)

class VehicleData(typing.NamedTuple):
    vehicle_id: str
    segment_id: str
    standing_capacity: int
    sitting_capacity: int
    call_name: str
    speed: float
    last_updated_on: str
    route_id: str
    tracking_status: str
    latitude: float
    longitude: float
    heading: int
    passenger_load: typing.Optional[int]  # Nullable field
    arrival_estimates: typing.List[ArrivalEstimate]

beam.coders.registry.register_coder(VehicleData, beam.coders.RowCoder)

class FetchVehicleData(beam.DoFn):
    def process(self, element):
        url = "https://transloc-api-1-2.p.rapidapi.com/vehicles.json"
        querystring = {
            "agencies":"uchicago",
        }
        headers = {
            "X-RapidAPI-Key": "API_KEYS",
            "X-RapidAPI-Host": "transloc-api-1-2.p.rapidapi.com"
        }
        try:
            response = requests.get(url, headers=headers, params=querystring, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            logging.error(f"Error fetching data from API: {e}")
            return
        data = json.loads(response.text)
        for agency_vehicles in data.get("data", {}).values():
            for vehicle in agency_vehicles:
                arrival_estimates = [
                    {
                        "route_id": estimate["route_id"],
                        "arrival_at": estimate["arrival_at"],
                        "stop_id": estimate["stop_id"]
                    } for estimate in vehicle.get("arrival_estimates", [])
                ]
                vehicle_data = {
                    "vehicle_id": vehicle.get("vehicle_id"),
                    "segment_id": vehicle.get("segment_id"),
                    "standing_capacity": vehicle.get("standing_capacity"),
                    "sitting_capacity": vehicle.get("sitting_capacity"),
                    "call_name": vehicle.get("call_name"),
                    "speed": vehicle.get("speed"),
                    "last_updated_on": vehicle.get("last_updated_on"),
                    "route_id": vehicle.get("route_id"),
                    "tracking_status": vehicle.get("tracking_status"),
                    "latitude": vehicle["location"]["lat"],
                    "longitude": vehicle["location"]["lng"],
                    "heading": vehicle.get("heading"),
                    "passenger_load": vehicle.get("passenger_load"),
                    "arrival_estimates": arrival_estimates
                }
                yield vehicle_data


def run():
    parser = argparse.ArgumentParser(description='Load from Json from Pub/Sub into BigQuery')
    parser.add_argument('--project',required=True, help='Specify Google Cloud project')
    parser.add_argument('--region', required=True, help='Specify Google Cloud region')
    parser.add_argument('--staging_location', required=True, help='Specify Cloud Storage bucket for staging')
    parser.add_argument('--temp_location', required=True, help='Specify Cloud Storage bucket for temp')
    parser.add_argument('--runner', required=True, help='Specify Apache Beam Runner')
    parser.add_argument('--table_name', required=True, help='BigQuery table name for aggregate results')


    opts, pipeline_args = parser.parse_known_args()

    # Setting up the Beam pipeline options
    options = PipelineOptions(pipeline_args, save_main_session=True, streaming=True)
    options.view_as(GoogleCloudOptions).project = opts.project
    options.view_as(GoogleCloudOptions).region = opts.region
    options.view_as(GoogleCloudOptions).staging_location = opts.staging_location
    options.view_as(GoogleCloudOptions).temp_location = opts.temp_location
    options.view_as(GoogleCloudOptions).job_name = '{0}{1}'.format('streaming-transloc-traffic-sql-pipeline-',time.time_ns())
    options.view_as(StandardOptions).runner = opts.runner

    table_name = opts.table_name

    # Table schema for BigQuery
    vehicle_data_schema_json = """
    {
    "fields": [
        {"name": "vehicle_id", "type": "STRING", "mode": "REQUIRED"},
        {"name": "segment_id", "type": "STRING", "mode": "NULLABLE"},
        {"name": "standing_capacity", "type": "INTEGER", "mode": "NULLABLE"},
        {"name": "sitting_capacity", "type": "INTEGER", "mode": "NULLABLE"},
        {"name": "call_name", "type": "STRING", "mode": "NULLABLE"},
        {"name": "speed", "type": "FLOAT", "mode": "NULLABLE"},
        {"name": "last_updated_on", "type": "TIMESTAMP", "mode": "NULLABLE"},
        {"name": "route_id", "type": "STRING", "mode": "NULLABLE"},
        {"name": "tracking_status", "type": "STRING", "mode": "NULLABLE"},
        {"name": "latitude", "type": "FLOAT", "mode": "NULLABLE"},
        {"name": "longitude", "type": "FLOAT", "mode": "NULLABLE"},
        {"name": "heading", "type": "INTEGER", "mode": "NULLABLE"},
        {"name": "passenger_load", "type": "INTEGER", "mode": "NULLABLE"},
        {
        "name": "arrival_estimates", 
        "type": "RECORD", 
        "mode": "REPEATED",
        "fields": [
            {"name": "route_id", "type": "STRING", "mode": "NULLABLE"},
            {"name": "arrival_at", "type": "TIMESTAMP", "mode": "NULLABLE"},
            {"name": "stop_id", "type": "STRING", "mode": "NULLABLE"}
        ]
        }
    ]
    }
"""

    vehicle_data_schema = parse_table_schema_from_json(vehicle_data_schema_json)
        
    with beam.Pipeline(options=options) as pipeline:
        (
            pipeline
            | 'Periodic Trigger' >> beam.Create([None])
            | 'Fixed Interval Window' >> beam.WindowInto(beam.window.FixedWindows(3600))  # Trigger every 1 hour
            | 'Fetch Vehicle Data' >> beam.ParDo(FetchVehicleData())
            | 'Write to BigQuery Raw Table' >> beam.io.WriteToBigQuery(
                table_name,
                schema=vehicle_data_schema,
                create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
            )
        )

    logging.info("Building pipeline ...")

    pipeline.run().wait_until_finish()

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    try:
        run()
    except Exception as e:
        logging.error(f"Pipeline execution failed: {e}")