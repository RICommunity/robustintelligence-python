# ListMetricIdentifiersResponse

ListMetricIdentifiersResponse returns metric identifiers grouped under features, subsets or neither.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregated_metrics** | [**List[AggregatedMetric]**](AggregatedMetric.md) |  | [optional] 
**feature_metrics** | [**Dict[str, FeatureMetrics]**](FeatureMetrics.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.list_metric_identifiers_response import ListMetricIdentifiersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListMetricIdentifiersResponse from a JSON string
list_metric_identifiers_response_instance = ListMetricIdentifiersResponse.from_json(json)
# print the JSON string representation of the object
print(ListMetricIdentifiersResponse.to_json())

# convert the object into a dict
list_metric_identifiers_response_dict = list_metric_identifiers_response_instance.to_dict()
# create an instance of ListMetricIdentifiersResponse from a dict
list_metric_identifiers_response_from_dict = ListMetricIdentifiersResponse.from_dict(list_metric_identifiers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

