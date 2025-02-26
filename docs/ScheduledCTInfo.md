# ScheduledCTInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eval_data_integration_id** | [**ID**](ID.md) |  | [optional] 
**eval_data_info** | [**DataInfo**](DataInfo.md) |  | [optional] 
**eval_pred_integration_id** | [**ID**](ID.md) |  | [optional] 
**eval_pred_info** | [**PredInfo**](PredInfo.md) |  | [optional] 
**last_ct_scheduled** | **datetime** | Specifies a timestamp based on the end time of the window for each run. The scheduler uses this timestamp to determine job start times and the time bin to use. | [optional] 
**activated_time** | **datetime** | When the AI Firewall has no bins, this value is used as the start time. Otherwise, the end time of the last bin in the AI Firewall is used as the AI Firewall start time. | [optional] 
**disable_scheduled_ct** | **bool** | Option for disabling scheduled CT - this should be false by default. This enables users to suspend a scheduled CT while preserving existing settings. | [optional] 

## Example

```python
from ri.apiclient.models.scheduled_ct_info import ScheduledCTInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledCTInfo from a JSON string
scheduled_ct_info_instance = ScheduledCTInfo.from_json(json)
# print the JSON string representation of the object
print(ScheduledCTInfo.to_json())

# convert the object into a dict
scheduled_ct_info_dict = scheduled_ct_info_instance.to_dict()
# create an instance of ScheduledCTInfo from a dict
scheduled_ct_info_from_dict = ScheduledCTInfo.from_dict(scheduled_ct_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

