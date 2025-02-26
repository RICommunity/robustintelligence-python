# CreateScheduleResponse

CreateScheduleResponse is the response message for CreateSchedule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_id** | [**ID**](ID.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.create_schedule_response import CreateScheduleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateScheduleResponse from a JSON string
create_schedule_response_instance = CreateScheduleResponse.from_json(json)
# print the JSON string representation of the object
print(CreateScheduleResponse.to_json())

# convert the object into a dict
create_schedule_response_dict = create_schedule_response_instance.to_dict()
# create an instance of CreateScheduleResponse from a dict
create_schedule_response_from_dict = CreateScheduleResponse.from_dict(create_schedule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

