# Schedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_id** | [**ID**](ID.md) |  | [optional] 
**project_id** | [**ID**](ID.md) |  | [optional] 
**test_run_config** | [**TestRunConfig**](TestRunConfig.md) |  | [optional] 
**frequency_cron_expr** | **str** | Cron expression used to determine how often to run the schedule. Accepts \&quot;@hourly\&quot;, \&quot;@daily\&quot;, \&quot;@weekly\&quot;, and \&quot;@monthly\&quot;. | [optional] 

## Example

```python
from ri.apiclient.models.schedule import Schedule

# TODO update the JSON string below
json = "{}"
# create an instance of Schedule from a JSON string
schedule_instance = Schedule.from_json(json)
# print the JSON string representation of the object
print(Schedule.to_json())

# convert the object into a dict
schedule_dict = schedule_instance.to_dict()
# create an instance of Schedule from a dict
schedule_from_dict = Schedule.from_dict(schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

