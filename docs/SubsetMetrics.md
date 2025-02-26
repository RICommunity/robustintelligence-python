# SubsetMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_ids** | [**List[SubsetMetric]**](SubsetMetric.md) | List of Metric IDs. | [optional] 

## Example

```python
from ri.apiclient.models.subset_metrics import SubsetMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of SubsetMetrics from a JSON string
subset_metrics_instance = SubsetMetrics.from_json(json)
# print the JSON string representation of the object
print(SubsetMetrics.to_json())

# convert the object into a dict
subset_metrics_dict = subset_metrics_instance.to_dict()
# create an instance of SubsetMetrics from a dict
subset_metrics_from_dict = SubsetMetrics.from_dict(subset_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

