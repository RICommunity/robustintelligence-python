# ActivateScheduleForProjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | [**ID**](ID.md) |  | [optional] 
**active_schedule** | [**ScheduleInfo**](ScheduleInfo.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.activate_schedule_for_project_response import ActivateScheduleForProjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActivateScheduleForProjectResponse from a JSON string
activate_schedule_for_project_response_instance = ActivateScheduleForProjectResponse.from_json(json)
# print the JSON string representation of the object
print(ActivateScheduleForProjectResponse.to_json())

# convert the object into a dict
activate_schedule_for_project_response_dict = activate_schedule_for_project_response_instance.to_dict()
# create an instance of ActivateScheduleForProjectResponse from a dict
activate_schedule_for_project_response_from_dict = ActivateScheduleForProjectResponse.from_dict(activate_schedule_for_project_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

