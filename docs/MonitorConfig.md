# MonitorConfig

Config defines a configuration for a monitor. There are different varities of monitors, such as metric degradation monitors and anomaly monitors. Metric degradation monitors track metrics over time and make up the vast majority of monitors in our system. Anomaly monitors track discrete events such as Security infractions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**degradation** | [**MetricDegradationConfig**](MetricDegradationConfig.md) |  | [optional] 
**anomaly** | **object** | Anomaly Monitors track events over time that are not associated with metrics. For instance, attacks on a model constitute Anomalies. | [optional] 

## Example

```python
from ri.apiclient.models.monitor_config import MonitorConfig

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorConfig from a JSON string
monitor_config_instance = MonitorConfig.from_json(json)
# print the JSON string representation of the object
print(MonitorConfig.to_json())

# convert the object into a dict
monitor_config_dict = monitor_config_instance.to_dict()
# create an instance of MonitorConfig from a dict
monitor_config_from_dict = MonitorConfig.from_dict(monitor_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

