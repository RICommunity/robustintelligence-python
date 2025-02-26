# UpdateScheduleResponse

UpdateScheduleResponse is the response message for UpdateSchedule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule** | [**Schedule**](Schedule.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.update_schedule_response import UpdateScheduleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateScheduleResponse from a JSON string
update_schedule_response_instance = UpdateScheduleResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateScheduleResponse.to_json())

# convert the object into a dict
update_schedule_response_dict = update_schedule_response_instance.to_dict()
# create an instance of UpdateScheduleResponse from a dict
update_schedule_response_from_dict = UpdateScheduleResponse.from_dict(update_schedule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

