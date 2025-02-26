# MetricDegradationConfig

MetricDegradation Monitors track metrics over time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | [**Aggregation**](Aggregation.md) |  | [optional] 
**transform** | [**Transform**](Transform.md) |  | [optional] 
**threshold** | [**Threshold**](Threshold.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.metric_degradation_config import MetricDegradationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of MetricDegradationConfig from a JSON string
metric_degradation_config_instance = MetricDegradationConfig.from_json(json)
# print the JSON string representation of the object
print(MetricDegradationConfig.to_json())

# convert the object into a dict
metric_degradation_config_dict = metric_degradation_config_instance.to_dict()
# create an instance of MetricDegradationConfig from a dict
metric_degradation_config_from_dict = MetricDegradationConfig.from_dict(metric_degradation_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

