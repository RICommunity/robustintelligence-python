# SubsetMetric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_id** | [**SubsetTestMetricIdentifier**](SubsetTestMetricIdentifier.md) |  | [optional] 
**excluded_transforms** | [**ExcludedTransforms**](ExcludedTransforms.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.subset_metric import SubsetMetric

# TODO update the JSON string below
json = "{}"
# create an instance of SubsetMetric from a JSON string
subset_metric_instance = SubsetMetric.from_json(json)
# print the JSON string representation of the object
print(SubsetMetric.to_json())

# convert the object into a dict
subset_metric_dict = subset_metric_instance.to_dict()
# create an instance of SubsetMetric from a dict
subset_metric_from_dict = SubsetMetric.from_dict(subset_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

