# Monitor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**name** | **str** | The name of the monitor. | [optional] 
**firewall_id** | [**ID**](ID.md) |  | [optional] 
**monitor_type** | [**MonitorType**](MonitorType.md) |  | [optional] [default to MonitorType.UNSPECIFIED]
**risk_category_type** | [**RiskCategoryType**](RiskCategoryType.md) |  | [optional] [default to RiskCategoryType.UNSPECIFIED]
**test_category** | [**TestCategoryType**](TestCategoryType.md) |  | [optional] [default to TestCategoryType.UNSPECIFIED]
**artifact_identifier** | [**ArtifactIdentifier**](ArtifactIdentifier.md) |  | [optional] 
**created_time** | **datetime** | The time at which the monitor was created. | [optional] 
**notify** | **bool** | This field indicates whether the system should send CT monitoring notifications when this monitor is triggered. For default monitors, after the RIME engine creates a Monitor, this field should only be modified directly by the user. i.e. when we upsert the monitor in the Result synthesizer, we must not overwrite the value configured by the user. | [optional] 
**config** | [**MonitorConfig**](MonitorConfig.md) |  | [optional] 
**excluded_transforms** | [**ExcludedTransforms**](ExcludedTransforms.md) |  | [optional] 
**pinned** | **bool** | Option to pin a monitor. Pinned monitors are pinned for all users visiting the monitor&#39;s project. | [optional] 

## Example

```python
from ri.apiclient.models.monitor import Monitor

# TODO update the JSON string below
json = "{}"
# create an instance of Monitor from a JSON string
monitor_instance = Monitor.from_json(json)
# print the JSON string representation of the object
print(Monitor.to_json())

# convert the object into a dict
monitor_dict = monitor_instance.to_dict()
# create an instance of Monitor from a dict
monitor_from_dict = Monitor.from_dict(monitor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

