"""Generated message classes for orgpolicy version v2.

The Organization Policy API allows users to configure governance rules on
their Google Cloud resources across the resource hierarchy.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding


package = 'orgpolicy'


class GoogleCloudOrgpolicyV2AlternatePolicySpec(_messages.Message):
  r"""Similar to PolicySpec but with an extra 'launch' field for launch
  reference. The PolicySpec here is specific for dry-run/darklaunch.

  Fields:
    launch: Reference to the launch that will be used while audit logging and
      to control the launch. Should be set only in the alternate policy.
    spec: Specify constraint for configurations of Google Cloud resources.
  """

  launch = _messages.StringField(1)
  spec = _messages.MessageField('GoogleCloudOrgpolicyV2PolicySpec', 2)


class GoogleCloudOrgpolicyV2Constraint(_messages.Message):
  r"""A constraint describes a way to restrict resource's configuration. For
  example, you could enforce a constraint that controls which Google Cloud
  services can be activated across an organization, or whether a Compute
  Engine instance can have serial port connections established. Constraints
  can be configured by the organization policy administrator to fit the needs
  of the organization by setting a policy that includes constraints at
  different locations in the organization's resource hierarchy. Policies are
  inherited down the resource hierarchy from higher levels, but can also be
  overridden. For details about the inheritance rules please read about
  `policies`. Constraints have a default behavior determined by the
  `constraint_default` field, which is the enforcement behavior that is used
  in the absence of a policy being defined or inherited for the resource in
  question.

  Enums:
    ConstraintDefaultValueValuesEnum: The evaluation behavior of this
      constraint in the absence of a policy.

  Fields:
    booleanConstraint: Defines this constraint as being a BooleanConstraint.
    constraintDefault: The evaluation behavior of this constraint in the
      absence of a policy.
    description: Detailed description of what this constraint controls as well
      as how and where it is enforced. Mutable.
    displayName: The human readable name. Mutable.
    listConstraint: Defines this constraint as being a ListConstraint.
    name: Immutable. The resource name of the constraint. Must be in one of
      the following forms: *
      `projects/{project_number}/constraints/{constraint_name}` *
      `folders/{folder_id}/constraints/{constraint_name}` *
      `organizations/{organization_id}/constraints/{constraint_name}` For
      example, "/projects/123/constraints/compute.disableSerialPortAccess".
    supportsDryRun: Shows if dry run is supported for this constraint or not.
  """

  class ConstraintDefaultValueValuesEnum(_messages.Enum):
    r"""The evaluation behavior of this constraint in the absence of a policy.

    Values:
      CONSTRAINT_DEFAULT_UNSPECIFIED: This is only used for distinguishing
        unset values and should never be used.
      ALLOW: Indicate that all values are allowed for list constraints.
        Indicate that enforcement is off for boolean constraints.
      DENY: Indicate that all values are denied for list constraints. Indicate
        that enforcement is on for boolean constraints.
    """
    CONSTRAINT_DEFAULT_UNSPECIFIED = 0
    ALLOW = 1
    DENY = 2

  booleanConstraint = _messages.MessageField('GoogleCloudOrgpolicyV2ConstraintBooleanConstraint', 1)
  constraintDefault = _messages.EnumField('ConstraintDefaultValueValuesEnum', 2)
  description = _messages.StringField(3)
  displayName = _messages.StringField(4)
  listConstraint = _messages.MessageField('GoogleCloudOrgpolicyV2ConstraintListConstraint', 5)
  name = _messages.StringField(6)
  supportsDryRun = _messages.BooleanField(7)


class GoogleCloudOrgpolicyV2ConstraintBooleanConstraint(_messages.Message):
  r"""A constraint that is either enforced or not. For example, a constraint
  `constraints/compute.disableSerialPortAccess`. If it is enforced on a VM
  instance, serial port connections will not be opened to that instance.
  """



class GoogleCloudOrgpolicyV2ConstraintListConstraint(_messages.Message):
  r"""A constraint that allows or disallows a list of string values, which are
  configured by an Organization Policy administrator with a policy.

  Fields:
    supportsIn: Indicates whether values grouped into categories can be used
      in `Policy.allowed_values` and `Policy.denied_values`. For example,
      `"in:Python"` would match any value in the 'Python' group.
    supportsUnder: Indicates whether subtrees of the Resource Manager resource
      hierarchy can be used in `Policy.allowed_values` and
      `Policy.denied_values`. For example, `"under:folders/123"` would match
      any resource under the 'folders/123' folder.
  """

  supportsIn = _messages.BooleanField(1)
  supportsUnder = _messages.BooleanField(2)


class GoogleCloudOrgpolicyV2CustomConstraint(_messages.Message):
  r"""A custom constraint defined by customers which can *only* be applied to
  the given resource types and organization. By creating a custom constraint,
  customers can apply policies of this custom constraint. *Creating a custom
  constraint itself does NOT apply any policy enforcement*.

  Enums:
    ActionTypeValueValuesEnum: Allow or deny type.
    MethodTypesValueListEntryValuesEnum:

  Fields:
    actionType: Allow or deny type.
    condition: Org policy condition/expression. For example:
      `resource.instanceName.matches("[production|test]_.*_(\d)+")` or,
      `resource.management.auto_upgrade == true` The max length of the
      condition is 1000 characters.
    description: Detailed information about this custom policy constraint. The
      max length of the description is 2000 characters.
    displayName: One line display name for the UI. The max length of the
      display_name is 200 characters.
    methodTypes: All the operations being applied for this constraint.
    name: Immutable. Name of the constraint. This is unique within the
      organization. Format of the name should be * `organizations/{organizatio
      n_id}/customConstraints/{custom_constraint_id}` Example:
      `organizations/123/customConstraints/custom.createOnlyE2TypeVms` The max
      length is 70 characters and the minimum length is 1. Note that the
      prefix `organizations/{organization_id}/customConstraints/` is not
      counted.
    resourceTypes: Immutable. The resource instance type on which this policy
      applies. Format will be of the form : `/` Example: *
      `compute.googleapis.com/Instance`.
    updateTime: Output only. The last time this custom constraint was updated.
      This represents the last time that the `CreateCustomConstraint` or
      `UpdateCustomConstraint` RPC was called
  """

  class ActionTypeValueValuesEnum(_messages.Enum):
    r"""Allow or deny type.

    Values:
      ACTION_TYPE_UNSPECIFIED: Unspecified. Results in an error.
      ALLOW: Allowed action type.
      DENY: Deny action type.
    """
    ACTION_TYPE_UNSPECIFIED = 0
    ALLOW = 1
    DENY = 2

  class MethodTypesValueListEntryValuesEnum(_messages.Enum):
    r"""MethodTypesValueListEntryValuesEnum enum type.

    Values:
      METHOD_TYPE_UNSPECIFIED: Unspecified. Results in an error.
      CREATE: Constraint applied when creating the resource.
      UPDATE: Constraint applied when updating the resource.
      DELETE: Constraint applied when deleting the resource. Not supported
        yet.
    """
    METHOD_TYPE_UNSPECIFIED = 0
    CREATE = 1
    UPDATE = 2
    DELETE = 3

  actionType = _messages.EnumField('ActionTypeValueValuesEnum', 1)
  condition = _messages.StringField(2)
  description = _messages.StringField(3)
  displayName = _messages.StringField(4)
  methodTypes = _messages.EnumField('MethodTypesValueListEntryValuesEnum', 5, repeated=True)
  name = _messages.StringField(6)
  resourceTypes = _messages.StringField(7, repeated=True)
  updateTime = _messages.StringField(8)


class GoogleCloudOrgpolicyV2ListConstraintsResponse(_messages.Message):
  r"""The response returned from the ListConstraints method.

  Fields:
    constraints: The collection of constraints that are available on the
      targeted resource.
    nextPageToken: Page token used to retrieve the next page. This is
      currently not used.
  """

  constraints = _messages.MessageField('GoogleCloudOrgpolicyV2Constraint', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class GoogleCloudOrgpolicyV2ListCustomConstraintsResponse(_messages.Message):
  r"""The response returned from the ListCustomConstraints method. It will be
  empty if no custom constraints are set on the organization resource.

  Fields:
    customConstraints: All custom constraints that exist on the organization
      resource. It will be empty if no custom constraints are set.
    nextPageToken: Page token used to retrieve the next page. This is
      currently not used, but the server may at any point start supplying a
      valid token.
  """

  customConstraints = _messages.MessageField('GoogleCloudOrgpolicyV2CustomConstraint', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class GoogleCloudOrgpolicyV2ListPoliciesResponse(_messages.Message):
  r"""The response returned from the ListPolicies method. It will be empty if
  no policies are set on the resource.

  Fields:
    nextPageToken: Page token used to retrieve the next page. This is
      currently not used, but the server may at any point start supplying a
      valid token.
    policies: All policies that exist on the resource. It will be empty if no
      policies are set.
  """

  nextPageToken = _messages.StringField(1)
  policies = _messages.MessageField('GoogleCloudOrgpolicyV2Policy', 2, repeated=True)


class GoogleCloudOrgpolicyV2Policy(_messages.Message):
  r"""Defines an organization policy which is used to specify constraints for
  configurations of Google Cloud resources.

  Fields:
    alternate: Deprecated.
    dryRunSpec: Dry-run policy. Audit-only policy, can be used to monitor how
      the policy would have impacted the existing and future resources if it's
      enforced.
    etag: Optional. An opaque tag indicating the current state of the policy,
      used for concurrency control. This 'etag' is computed by the server
      based on the value of other fields, and may be sent on update and delete
      requests to ensure the client has an up-to-date value before proceeding.
    name: Immutable. The resource name of the policy. Must be one of the
      following forms, where `constraint_name` is the name of the constraint
      which this policy configures: *
      `projects/{project_number}/policies/{constraint_name}` *
      `folders/{folder_id}/policies/{constraint_name}` *
      `organizations/{organization_id}/policies/{constraint_name}` For
      example, `projects/123/policies/compute.disableSerialPortAccess`. Note:
      `projects/{project_id}/policies/{constraint_name}` is also an acceptable
      name for API requests, but responses will return the name using the
      equivalent project number.
    spec: Basic information about the Organization Policy.
  """

  alternate = _messages.MessageField('GoogleCloudOrgpolicyV2AlternatePolicySpec', 1)
  dryRunSpec = _messages.MessageField('GoogleCloudOrgpolicyV2PolicySpec', 2)
  etag = _messages.StringField(3)
  name = _messages.StringField(4)
  spec = _messages.MessageField('GoogleCloudOrgpolicyV2PolicySpec', 5)


class GoogleCloudOrgpolicyV2PolicySpec(_messages.Message):
  r"""Defines a Google Cloud policy specification which is used to specify
  constraints for configurations of Google Cloud resources.

  Fields:
    etag: An opaque tag indicating the current version of the policySpec, used
      for concurrency control. This field is ignored if used in a
      `CreatePolicy` request. When the policy is returned from either a
      `GetPolicy` or a `ListPolicies` request, this `etag` indicates the
      version of the current policySpec to use when executing a read-modify-
      write loop. When the policy is returned from a `GetEffectivePolicy`
      request, the `etag` will be unset.
    inheritFromParent: Determines the inheritance behavior for this policy. If
      `inherit_from_parent` is true, policy rules set higher up in the
      hierarchy (up to the closest root) are inherited and present in the
      effective policy. If it is false, then no rules are inherited, and this
      policy becomes the new root for evaluation. This field can be set only
      for policies which configure list constraints.
    reset: Ignores policies set above this resource and restores the
      `constraint_default` enforcement behavior of the specific constraint at
      this resource. This field can be set in policies for either list or
      boolean constraints. If set, `rules` must be empty and
      `inherit_from_parent` must be set to false.
    rules: In policies for boolean constraints, the following requirements
      apply: - There must be one and only one policy rule where condition is
      unset. - Boolean policy rules with conditions must set `enforced` to the
      opposite of the policy rule without a condition. - During policy
      evaluation, policy rules with conditions that are true for a target
      resource take precedence.
    updateTime: Output only. The time stamp this was previously updated. This
      represents the last time a call to `CreatePolicy` or `UpdatePolicy` was
      made for that policy.
  """

  etag = _messages.StringField(1)
  inheritFromParent = _messages.BooleanField(2)
  reset = _messages.BooleanField(3)
  rules = _messages.MessageField('GoogleCloudOrgpolicyV2PolicySpecPolicyRule', 4, repeated=True)
  updateTime = _messages.StringField(5)


class GoogleCloudOrgpolicyV2PolicySpecPolicyRule(_messages.Message):
  r"""A rule used to express this policy.

  Fields:
    allowAll: Setting this to true means that all values are allowed. This
      field can be set only in policies for list constraints.
    condition: A condition which determines whether this rule is used in the
      evaluation of the policy. When set, the `expression` field in the `Expr'
      must include from 1 to 10 subexpressions, joined by the "||" or "&&"
      operators. Each subexpression must be of the form
      "resource.matchTag('/tag_key_short_name, 'tag_value_short_name')". or
      "resource.matchTagId('tagKeys/key_id', 'tagValues/value_id')". where
      key_name and value_name are the resource names for Label Keys and
      Values. These names are available from the Tag Manager Service. An
      example expression is: "resource.matchTag('123456789/environment,
      'prod')". or "resource.matchTagId('tagKeys/123', 'tagValues/456')".
    denyAll: Setting this to true means that all values are denied. This field
      can be set only in policies for list constraints.
    enforce: If `true`, then the policy is enforced. If `false`, then any
      configuration is acceptable. This field can be set only in policies for
      boolean constraints.
    values: List of values to be used for this policy rule. This field can be
      set only in policies for list constraints.
  """

  allowAll = _messages.BooleanField(1)
  condition = _messages.MessageField('GoogleTypeExpr', 2)
  denyAll = _messages.BooleanField(3)
  enforce = _messages.BooleanField(4)
  values = _messages.MessageField('GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValues', 5)


class GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValues(_messages.Message):
  r"""A message that holds specific allowed and denied values. This message
  can define specific values and subtrees of the Resource Manager resource
  hierarchy (`Organizations`, `Folders`, `Projects`) that are allowed or
  denied. This is achieved by using the `under:` and optional `is:` prefixes.
  The `under:` prefix is used to denote resource subtree values. The `is:`
  prefix is used to denote specific values, and is required only if the value
  contains a ":". Values prefixed with "is:" are treated the same as values
  with no prefix. Ancestry subtrees must be in one of the following formats: -
  `projects/` (for example, `projects/tokyo-rain-123`) - `folders/` (for
  example, `folders/1234`) - `organizations/` (for example,
  `organizations/1234`) The `supports_under` field of the associated
  `Constraint` defines whether ancestry prefixes can be used.

  Fields:
    allowedValues: List of values allowed at this resource.
    deniedValues: List of values denied at this resource.
  """

  allowedValues = _messages.StringField(1, repeated=True)
  deniedValues = _messages.StringField(2, repeated=True)


class GoogleProtobufEmpty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance: service Foo { rpc
  Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }
  """



class GoogleTypeExpr(_messages.Message):
  r"""Represents a textual expression in the Common Expression Language (CEL)
  syntax. CEL is a C-like expression language. The syntax and semantics of CEL
  are documented at https://github.com/google/cel-spec. Example (Comparison):
  title: "Summary size limit" description: "Determines if a summary is less
  than 100 chars" expression: "document.summary.size() < 100" Example
  (Equality): title: "Requestor is owner" description: "Determines if
  requestor is the document owner" expression: "document.owner ==
  request.auth.claims.email" Example (Logic): title: "Public documents"
  description: "Determine whether the document should be publicly visible"
  expression: "document.type != 'private' && document.type != 'internal'"
  Example (Data Manipulation): title: "Notification string" description:
  "Create a notification string with a timestamp." expression: "'New message
  received at ' + string(document.create_time)" The exact variables and
  functions that may be referenced within an expression are determined by the
  service that evaluates it. See the service documentation for additional
  information.

  Fields:
    description: Optional. Description of the expression. This is a longer
      text which describes the expression, e.g. when hovered over it in a UI.
    expression: Textual representation of an expression in Common Expression
      Language syntax.
    location: Optional. String indicating the location of the expression for
      error reporting, e.g. a file name and a position in the file.
    title: Optional. Title for the expression, i.e. a short string describing
      its purpose. This can be used e.g. in UIs which allow to enter the
      expression.
  """

  description = _messages.StringField(1)
  expression = _messages.StringField(2)
  location = _messages.StringField(3)
  title = _messages.StringField(4)


class OrgpolicyFoldersConstraintsListRequest(_messages.Message):
  r"""A OrgpolicyFoldersConstraintsListRequest object.

  Fields:
    pageSize: Size of the pages to be returned. This is currently unsupported
      and will be ignored. The server may at any point start using this field
      to limit page size.
    pageToken: Page token used to retrieve the next page. This is currently
      unsupported and will be ignored. The server may at any point start using
      this field.
    parent: Required. The Google Cloud resource that parents the constraint.
      Must be in one of the following forms: * `projects/{project_number}` *
      `projects/{project_id}` * `folders/{folder_id}` *
      `organizations/{organization_id}`
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class OrgpolicyFoldersPoliciesCreateRequest(_messages.Message):
  r"""A OrgpolicyFoldersPoliciesCreateRequest object.

  Fields:
    googleCloudOrgpolicyV2Policy: A GoogleCloudOrgpolicyV2Policy resource to
      be passed as the request body.
    parent: Required. The Google Cloud resource that will parent the new
      policy. Must be in one of the following forms: *
      `projects/{project_number}` * `projects/{project_id}` *
      `folders/{folder_id}` * `organizations/{organization_id}`
  """

  googleCloudOrgpolicyV2Policy = _messages.MessageField('GoogleCloudOrgpolicyV2Policy', 1)
  parent = _messages.StringField(2, required=True)


class OrgpolicyFoldersPoliciesDeleteRequest(_messages.Message):
  r"""A OrgpolicyFoldersPoliciesDeleteRequest object.

  Fields:
    etag: Optional. The current etag of policy. If an etag is provided and
      does not match the current etag of the policy, deletion will be blocked
      and an ABORTED error will be returned.
    name: Required. Name of the policy to delete. See the policy entry for
      naming rules.
  """

  etag = _messages.StringField(1)
  name = _messages.StringField(2, required=True)


class OrgpolicyFoldersPoliciesGetEffectivePolicyRequest(_messages.Message):
  r"""A OrgpolicyFoldersPoliciesGetEffectivePolicyRequest object.

  Fields:
    name: Required. The effective policy to compute. See Policy for naming
      requirements.
  """

  name = _messages.StringField(1, required=True)


class OrgpolicyFoldersPoliciesGetRequest(_messages.Message):
  r"""A OrgpolicyFoldersPoliciesGetRequest object.

  Fields:
    name: Required. Resource name of the policy. See Policy for naming
      requirements.
  """

  name = _messages.StringField(1, required=True)


class OrgpolicyFoldersPoliciesListRequest(_messages.Message):
  r"""A OrgpolicyFoldersPoliciesListRequest object.

  Fields:
    pageSize: Size of the pages to be returned. This is currently unsupported
      and will be ignored. The server may at any point start using this field
      to limit page size.
    pageToken: Page token used to retrieve the next page. This is currently
      unsupported and will be ignored. The server may at any point start using
      this field.
    parent: Required. The target Google Cloud resource that parents the set of
      constraints and policies that will be returned from this call. Must be
      in one of the following forms: * `projects/{project_number}` *
      `projects/{project_id}` * `folders/{folder_id}` *
      `organizations/{organization_id}`
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class OrgpolicyFoldersPoliciesPatchRequest(_messages.Message):
  r"""A OrgpolicyFoldersPoliciesPatchRequest object.

  Fields:
    googleCloudOrgpolicyV2Policy: A GoogleCloudOrgpolicyV2Policy resource to
      be passed as the request body.
    name: Immutable. The resource name of the policy. Must be one of the
      following forms, where `constraint_name` is the name of the constraint
      which this policy configures: *
      `projects/{project_number}/policies/{constraint_name}` *
      `folders/{folder_id}/policies/{constraint_name}` *
      `organizations/{organization_id}/policies/{constraint_name}` For
      example, `projects/123/policies/compute.disableSerialPortAccess`. Note:
      `projects/{project_id}/policies/{constraint_name}` is also an acceptable
      name for API requests, but responses will return the name using the
      equivalent project number.
    updateMask: Field mask used to specify the fields to be overwritten in the
      policy by the set. The fields specified in the update_mask are relative
      to the policy, not the full request.
  """

  googleCloudOrgpolicyV2Policy = _messages.MessageField('GoogleCloudOrgpolicyV2Policy', 1)
  name = _messages.StringField(2, required=True)
  updateMask = _messages.StringField(3)


class OrgpolicyOrganizationsConstraintsListRequest(_messages.Message):
  r"""A OrgpolicyOrganizationsConstraintsListRequest object.

  Fields:
    pageSize: Size of the pages to be returned. This is currently unsupported
      and will be ignored. The server may at any point start using this field
      to limit page size.
    pageToken: Page token used to retrieve the next page. This is currently
      unsupported and will be ignored. The server may at any point start using
      this field.
    parent: Required. The Google Cloud resource that parents the constraint.
      Must be in one of the following forms: * `projects/{project_number}` *
      `projects/{project_id}` * `folders/{folder_id}` *
      `organizations/{organization_id}`
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class OrgpolicyOrganizationsCustomConstraintsCreateRequest(_messages.Message):
  r"""A OrgpolicyOrganizationsCustomConstraintsCreateRequest object.

  Fields:
    googleCloudOrgpolicyV2CustomConstraint: A
      GoogleCloudOrgpolicyV2CustomConstraint resource to be passed as the
      request body.
    parent: Required. Must be in the following form: *
      `organizations/{organization_id}`
  """

  googleCloudOrgpolicyV2CustomConstraint = _messages.MessageField('GoogleCloudOrgpolicyV2CustomConstraint', 1)
  parent = _messages.StringField(2, required=True)


class OrgpolicyOrganizationsCustomConstraintsDeleteRequest(_messages.Message):
  r"""A OrgpolicyOrganizationsCustomConstraintsDeleteRequest object.

  Fields:
    name: Required. Name of the custom constraint to delete. See the custom
      constraint entry for naming rules.
  """

  name = _messages.StringField(1, required=True)


class OrgpolicyOrganizationsCustomConstraintsGetRequest(_messages.Message):
  r"""A OrgpolicyOrganizationsCustomConstraintsGetRequest object.

  Fields:
    name: Required. Resource name of the custom constraint. See the custom
      constraint entry for naming requirements.
  """

  name = _messages.StringField(1, required=True)


class OrgpolicyOrganizationsCustomConstraintsListRequest(_messages.Message):
  r"""A OrgpolicyOrganizationsCustomConstraintsListRequest object.

  Fields:
    pageSize: Size of the pages to be returned. This is currently unsupported
      and will be ignored. The server may at any point start using this field
      to limit page size.
    pageToken: Page token used to retrieve the next page. This is currently
      unsupported and will be ignored. The server may at any point start using
      this field.
    parent: Required. The target Google Cloud resource that parents the set of
      custom constraints that will be returned from this call. Must be in one
      of the following forms: * `organizations/{organization_id}`
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class OrgpolicyOrganizationsCustomConstraintsPatchRequest(_messages.Message):
  r"""A OrgpolicyOrganizationsCustomConstraintsPatchRequest object.

  Fields:
    googleCloudOrgpolicyV2CustomConstraint: A
      GoogleCloudOrgpolicyV2CustomConstraint resource to be passed as the
      request body.
    name: Immutable. Name of the constraint. This is unique within the
      organization. Format of the name should be * `organizations/{organizatio
      n_id}/customConstraints/{custom_constraint_id}` Example:
      `organizations/123/customConstraints/custom.createOnlyE2TypeVms` The max
      length is 70 characters and the minimum length is 1. Note that the
      prefix `organizations/{organization_id}/customConstraints/` is not
      counted.
  """

  googleCloudOrgpolicyV2CustomConstraint = _messages.MessageField('GoogleCloudOrgpolicyV2CustomConstraint', 1)
  name = _messages.StringField(2, required=True)


class OrgpolicyOrganizationsPoliciesCreateRequest(_messages.Message):
  r"""A OrgpolicyOrganizationsPoliciesCreateRequest object.

  Fields:
    googleCloudOrgpolicyV2Policy: A GoogleCloudOrgpolicyV2Policy resource to
      be passed as the request body.
    parent: Required. The Google Cloud resource that will parent the new
      policy. Must be in one of the following forms: *
      `projects/{project_number}` * `projects/{project_id}` *
      `folders/{folder_id}` * `organizations/{organization_id}`
  """

  googleCloudOrgpolicyV2Policy = _messages.MessageField('GoogleCloudOrgpolicyV2Policy', 1)
  parent = _messages.StringField(2, required=True)


class OrgpolicyOrganizationsPoliciesDeleteRequest(_messages.Message):
  r"""A OrgpolicyOrganizationsPoliciesDeleteRequest object.

  Fields:
    etag: Optional. The current etag of policy. If an etag is provided and
      does not match the current etag of the policy, deletion will be blocked
      and an ABORTED error will be returned.
    name: Required. Name of the policy to delete. See the policy entry for
      naming rules.
  """

  etag = _messages.StringField(1)
  name = _messages.StringField(2, required=True)


class OrgpolicyOrganizationsPoliciesGetEffectivePolicyRequest(_messages.Message):
  r"""A OrgpolicyOrganizationsPoliciesGetEffectivePolicyRequest object.

  Fields:
    name: Required. The effective policy to compute. See Policy for naming
      requirements.
  """

  name = _messages.StringField(1, required=True)


class OrgpolicyOrganizationsPoliciesGetRequest(_messages.Message):
  r"""A OrgpolicyOrganizationsPoliciesGetRequest object.

  Fields:
    name: Required. Resource name of the policy. See Policy for naming
      requirements.
  """

  name = _messages.StringField(1, required=True)


class OrgpolicyOrganizationsPoliciesListRequest(_messages.Message):
  r"""A OrgpolicyOrganizationsPoliciesListRequest object.

  Fields:
    pageSize: Size of the pages to be returned. This is currently unsupported
      and will be ignored. The server may at any point start using this field
      to limit page size.
    pageToken: Page token used to retrieve the next page. This is currently
      unsupported and will be ignored. The server may at any point start using
      this field.
    parent: Required. The target Google Cloud resource that parents the set of
      constraints and policies that will be returned from this call. Must be
      in one of the following forms: * `projects/{project_number}` *
      `projects/{project_id}` * `folders/{folder_id}` *
      `organizations/{organization_id}`
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class OrgpolicyOrganizationsPoliciesPatchRequest(_messages.Message):
  r"""A OrgpolicyOrganizationsPoliciesPatchRequest object.

  Fields:
    googleCloudOrgpolicyV2Policy: A GoogleCloudOrgpolicyV2Policy resource to
      be passed as the request body.
    name: Immutable. The resource name of the policy. Must be one of the
      following forms, where `constraint_name` is the name of the constraint
      which this policy configures: *
      `projects/{project_number}/policies/{constraint_name}` *
      `folders/{folder_id}/policies/{constraint_name}` *
      `organizations/{organization_id}/policies/{constraint_name}` For
      example, `projects/123/policies/compute.disableSerialPortAccess`. Note:
      `projects/{project_id}/policies/{constraint_name}` is also an acceptable
      name for API requests, but responses will return the name using the
      equivalent project number.
    updateMask: Field mask used to specify the fields to be overwritten in the
      policy by the set. The fields specified in the update_mask are relative
      to the policy, not the full request.
  """

  googleCloudOrgpolicyV2Policy = _messages.MessageField('GoogleCloudOrgpolicyV2Policy', 1)
  name = _messages.StringField(2, required=True)
  updateMask = _messages.StringField(3)


class OrgpolicyProjectsConstraintsListRequest(_messages.Message):
  r"""A OrgpolicyProjectsConstraintsListRequest object.

  Fields:
    pageSize: Size of the pages to be returned. This is currently unsupported
      and will be ignored. The server may at any point start using this field
      to limit page size.
    pageToken: Page token used to retrieve the next page. This is currently
      unsupported and will be ignored. The server may at any point start using
      this field.
    parent: Required. The Google Cloud resource that parents the constraint.
      Must be in one of the following forms: * `projects/{project_number}` *
      `projects/{project_id}` * `folders/{folder_id}` *
      `organizations/{organization_id}`
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class OrgpolicyProjectsPoliciesCreateRequest(_messages.Message):
  r"""A OrgpolicyProjectsPoliciesCreateRequest object.

  Fields:
    googleCloudOrgpolicyV2Policy: A GoogleCloudOrgpolicyV2Policy resource to
      be passed as the request body.
    parent: Required. The Google Cloud resource that will parent the new
      policy. Must be in one of the following forms: *
      `projects/{project_number}` * `projects/{project_id}` *
      `folders/{folder_id}` * `organizations/{organization_id}`
  """

  googleCloudOrgpolicyV2Policy = _messages.MessageField('GoogleCloudOrgpolicyV2Policy', 1)
  parent = _messages.StringField(2, required=True)


class OrgpolicyProjectsPoliciesDeleteRequest(_messages.Message):
  r"""A OrgpolicyProjectsPoliciesDeleteRequest object.

  Fields:
    etag: Optional. The current etag of policy. If an etag is provided and
      does not match the current etag of the policy, deletion will be blocked
      and an ABORTED error will be returned.
    name: Required. Name of the policy to delete. See the policy entry for
      naming rules.
  """

  etag = _messages.StringField(1)
  name = _messages.StringField(2, required=True)


class OrgpolicyProjectsPoliciesGetEffectivePolicyRequest(_messages.Message):
  r"""A OrgpolicyProjectsPoliciesGetEffectivePolicyRequest object.

  Fields:
    name: Required. The effective policy to compute. See Policy for naming
      requirements.
  """

  name = _messages.StringField(1, required=True)


class OrgpolicyProjectsPoliciesGetRequest(_messages.Message):
  r"""A OrgpolicyProjectsPoliciesGetRequest object.

  Fields:
    name: Required. Resource name of the policy. See Policy for naming
      requirements.
  """

  name = _messages.StringField(1, required=True)


class OrgpolicyProjectsPoliciesListRequest(_messages.Message):
  r"""A OrgpolicyProjectsPoliciesListRequest object.

  Fields:
    pageSize: Size of the pages to be returned. This is currently unsupported
      and will be ignored. The server may at any point start using this field
      to limit page size.
    pageToken: Page token used to retrieve the next page. This is currently
      unsupported and will be ignored. The server may at any point start using
      this field.
    parent: Required. The target Google Cloud resource that parents the set of
      constraints and policies that will be returned from this call. Must be
      in one of the following forms: * `projects/{project_number}` *
      `projects/{project_id}` * `folders/{folder_id}` *
      `organizations/{organization_id}`
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class OrgpolicyProjectsPoliciesPatchRequest(_messages.Message):
  r"""A OrgpolicyProjectsPoliciesPatchRequest object.

  Fields:
    googleCloudOrgpolicyV2Policy: A GoogleCloudOrgpolicyV2Policy resource to
      be passed as the request body.
    name: Immutable. The resource name of the policy. Must be one of the
      following forms, where `constraint_name` is the name of the constraint
      which this policy configures: *
      `projects/{project_number}/policies/{constraint_name}` *
      `folders/{folder_id}/policies/{constraint_name}` *
      `organizations/{organization_id}/policies/{constraint_name}` For
      example, `projects/123/policies/compute.disableSerialPortAccess`. Note:
      `projects/{project_id}/policies/{constraint_name}` is also an acceptable
      name for API requests, but responses will return the name using the
      equivalent project number.
    updateMask: Field mask used to specify the fields to be overwritten in the
      policy by the set. The fields specified in the update_mask are relative
      to the policy, not the full request.
  """

  googleCloudOrgpolicyV2Policy = _messages.MessageField('GoogleCloudOrgpolicyV2Policy', 1)
  name = _messages.StringField(2, required=True)
  updateMask = _messages.StringField(3)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default='json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
