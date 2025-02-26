# FeatureMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_metric_without_subsets** | [**List[FeatureMetricWithoutSubsets]**](FeatureMetricWithoutSubsets.md) |  | [optional] 
**subset_metrics** | [**Dict[str, SubsetMetrics]**](SubsetMetrics.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.feature_metrics import FeatureMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureMetrics from a JSON string
feature_metrics_instance = FeatureMetrics.from_json(json)
# print the JSON string representation of the object
print(FeatureMetrics.to_json())

# convert the object into a dict
feature_metrics_dict = feature_metrics_instance.to_dict()
# create an instance of FeatureMetrics from a dict
feature_metrics_from_dict = FeatureMetrics.from_dict(feature_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

