# GetScheduleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule** | [**Schedule**](Schedule.md) |  | [optional] 
**next_run_time** | **datetime** |  | [optional] 

## Example

```python
from ri.apiclient.models.get_schedule_response import GetScheduleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetScheduleResponse from a JSON string
get_schedule_response_instance = GetScheduleResponse.from_json(json)
# print the JSON string representation of the object
print(GetScheduleResponse.to_json())

# convert the object into a dict
get_schedule_response_dict = get_schedule_response_instance.to_dict()
# create an instance of GetScheduleResponse from a dict
get_schedule_response_from_dict = GetScheduleResponse.from_dict(get_schedule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

