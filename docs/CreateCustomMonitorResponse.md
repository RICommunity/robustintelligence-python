# CreateCustomMonitorResponse

CreateCustomMonitorResponse returns the created custom monitor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitor** | [**Monitor**](Monitor.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.create_custom_monitor_response import (
    CreateCustomMonitorResponse,
)

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomMonitorResponse from a JSON string
create_custom_monitor_response_instance = CreateCustomMonitorResponse.from_json(json)
# print the JSON string representation of the object
print(CreateCustomMonitorResponse.to_json())

# convert the object into a dict
create_custom_monitor_response_dict = create_custom_monitor_response_instance.to_dict()
# create an instance of CreateCustomMonitorResponse from a dict
create_custom_monitor_response_from_dict = CreateCustomMonitorResponse.from_dict(
    create_custom_monitor_response_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

