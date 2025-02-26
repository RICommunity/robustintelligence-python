# CreateScheduleRequest

CreateScheduleRequest is the request message for CreateSchedule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | [**ID**](ID.md) |  | 
**test_run_config** | [**TestRunConfig**](TestRunConfig.md) |  | 
**frequency_cron_expr** | **str** | Cron expression used to determine how often to run the schedule. | 

## Example

```python
from ri.apiclient.models.create_schedule_request import CreateScheduleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateScheduleRequest from a JSON string
create_schedule_request_instance = CreateScheduleRequest.from_json(json)
# print the JSON string representation of the object
print(CreateScheduleRequest.to_json())

# convert the object into a dict
create_schedule_request_dict = create_schedule_request_instance.to_dict()
# create an instance of CreateScheduleRequest from a dict
create_schedule_request_from_dict = CreateScheduleRequest.from_dict(
    create_schedule_request_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

