# GetMonitorResultResponse

GetMonitorResultResponse returns the results for a monitor within a time range.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitor_id** | [**ID**](ID.md) |  | [optional] 
**monitor_name** | **str** | The name of the monitor. | [optional] 
**metric_name** | **str** |  | [optional] 
**threshold** | [**Threshold**](Threshold.md) |  | [optional] 
**data_points** | [**List[MonitorDataPoint]**](MonitorDataPoint.md) | The monitor data points. | [optional] 
**description_html** | **str** | Description of the monitor that may contain HTML. | [optional] 
**long_description_tabs** | [**List[LongDescriptionTab]**](LongDescriptionTab.md) | More detailed information about the monitor. | [optional] 

## Example

```python
from ri.apiclient.models.get_monitor_result_response import GetMonitorResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMonitorResultResponse from a JSON string
get_monitor_result_response_instance = GetMonitorResultResponse.from_json(json)
# print the JSON string representation of the object
print(GetMonitorResultResponse.to_json())

# convert the object into a dict
get_monitor_result_response_dict = get_monitor_result_response_instance.to_dict()
# create an instance of GetMonitorResultResponse from a dict
get_monitor_result_response_from_dict = GetMonitorResultResponse.from_dict(
    get_monitor_result_response_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

