# MonitorDataPoint

MonitorDataPoint defines a single data point in the monitor time series. It identifies both a metric value and time interval.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_interval** | [**TimeInterval**](TimeInterval.md) |  | [optional] 
**monitor_value** | **float** |  | [optional] 

## Example

```python
from ri.apiclient.models.monitor_data_point import MonitorDataPoint

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorDataPoint from a JSON string
monitor_data_point_instance = MonitorDataPoint.from_json(json)
# print the JSON string representation of the object
print(MonitorDataPoint.to_json())

# convert the object into a dict
monitor_data_point_dict = monitor_data_point_instance.to_dict()
# create an instance of MonitorDataPoint from a dict
monitor_data_point_from_dict = MonitorDataPoint.from_dict(monitor_data_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

