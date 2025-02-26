# TestCaseMetricIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_batch_id** | **str** | Uniquely specifies a Test Batch. | [optional] 
**metric** | **str** | The metric name. | [optional] 
**feature_names** | **List[str]** | Human-readable names of the features. Must be sorted lexicographically. | [optional] 

## Example

```python
from ri.apiclient.models.test_case_metric_identifier import TestCaseMetricIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of TestCaseMetricIdentifier from a JSON string
test_case_metric_identifier_instance = TestCaseMetricIdentifier.from_json(json)
# print the JSON string representation of the object
print(TestCaseMetricIdentifier.to_json())

# convert the object into a dict
test_case_metric_identifier_dict = test_case_metric_identifier_instance.to_dict()
# create an instance of TestCaseMetricIdentifier from a dict
test_case_metric_identifier_from_dict = TestCaseMetricIdentifier.from_dict(
    test_case_metric_identifier_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

