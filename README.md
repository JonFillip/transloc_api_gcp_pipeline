<<<<<<< HEAD
# Transport Data Pipeline

## Project Description

This project is a data pipeline designed to fetch real-time vehicle data from the TransLoc API and ingest it into Google BigQuery. The pipeline is implemented using Apache Beam, a unified stream and batch processing model. It fetches vehicle data from the API, transforms it, and loads it into BigQuery for further analysis.

## Requirements

Before running the pipeline, ensure you have the following dependencies installed:

- Python 3.x
- Apache Beam
- Google Cloud SDK
- Other Python dependencies (install using `pip install -r requirements.txt`)

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/transport-data-pipeline.git
   cd transport-data-pipeline
   ```
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

3. **Setup Google Credentials**
    - Follow the instructions [here](https://cloud.google.com/docs/authentication/getting-started) to setup

4. **Setup Project, Cloud Storage and BigQuery**
    - Ensure that you have a Google Cloud project set with proper permissions given to the admin and service account. See more [here](https://cloud.google.com/docs)
    - Create a BigQuery Table (Sink)
    - Create a Cloud Storage Bucket (Source)
    - Enable Dataflow API
    - Enable Cloud Storage API
    - Enable BigQuery API

5. **Configure the Pipeline**
    Open `transloc_streaming_pipeline.py` and modify the pipeline options like project ID, region, staging location, etc., according to your Google Cloud project.

6. **Run the Pipeline**
    Run the following command to execute the data pipeline:
    ```bash
    python transloc_streaming_pipeline.py \
    --project your-project-id \
    --region your-region \
    --staging_location gs://your-staging-bucket \
    --temp_location gs://your-temp-bucket \
    --runner DataflowRunner \
    --table_name your-project-id:your-dataset.your-table \

Adjust the parameters according to your project details.# transloc_api_gcp_etl