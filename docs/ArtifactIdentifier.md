# ArtifactIdentifier

ArtifactIdentifier specifies the artifact a monitor tracks over time. Metrics exist in TestCases, TestBatches and CategoryTests. This is extendable to allow new kinds of metrics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_case_metric_identifier** | [**TestCaseMetricIdentifier**](TestCaseMetricIdentifier.md) |  | [optional] 
**category_test_metric_identifier** | [**CategoryTestIdentifier**](CategoryTestIdentifier.md) |  | [optional] 
**subset_test_metric_identifier** | [**SubsetTestMetricIdentifier**](SubsetTestMetricIdentifier.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.artifact_identifier import ArtifactIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactIdentifier from a JSON string
artifact_identifier_instance = ArtifactIdentifier.from_json(json)
# print the JSON string representation of the object
print(ArtifactIdentifier.to_json())

# convert the object into a dict
artifact_identifier_dict = artifact_identifier_instance.to_dict()
# create an instance of ArtifactIdentifier from a dict
artifact_identifier_from_dict = ArtifactIdentifier.from_dict(artifact_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

