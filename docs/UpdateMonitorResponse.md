# UpdateMonitorResponse

UpdateMonitorResponse returns the updated monitor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitor** | [**Monitor**](Monitor.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.update_monitor_response import UpdateMonitorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMonitorResponse from a JSON string
update_monitor_response_instance = UpdateMonitorResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateMonitorResponse.to_json())

# convert the object into a dict
update_monitor_response_dict = update_monitor_response_instance.to_dict()
# create an instance of UpdateMonitorResponse from a dict
update_monitor_response_from_dict = UpdateMonitorResponse.from_dict(
    update_monitor_response_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

