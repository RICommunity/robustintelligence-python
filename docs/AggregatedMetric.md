# AggregatedMetric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_case_metric_id** | [**TestCaseMetricIdentifier**](TestCaseMetricIdentifier.md) |  | [optional] 
**category_test_metric_id** | [**CategoryTestIdentifier**](CategoryTestIdentifier.md) |  | [optional] 
**excluded_transforms** | [**ExcludedTransforms**](ExcludedTransforms.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.aggregated_metric import AggregatedMetric

# TODO update the JSON string below
json = "{}"
# create an instance of AggregatedMetric from a JSON string
aggregated_metric_instance = AggregatedMetric.from_json(json)
# print the JSON string representation of the object
print(AggregatedMetric.to_json())

# convert the object into a dict
aggregated_metric_dict = aggregated_metric_instance.to_dict()
# create an instance of AggregatedMetric from a dict
aggregated_metric_from_dict = AggregatedMetric.from_dict(aggregated_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

