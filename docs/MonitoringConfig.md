# MonitoringConfig

MonitoringConfig is a configuration for Continuous Testing notifications. These notifications are triggered when certain Monitors detect abnormalities. For instance, if a model performance Monitor fails, the system will send a notification after the job completes. Turn on and off notifications for Monitors in the web application or the SDK. Only a subset of Monitors will have notifications on by default.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | [**AlertLevel**](AlertLevel.md) |  | [optional] [default to AlertLevel.UNSPECIFIED]

## Example

```python
from ri.apiclient.models.monitoring_config import MonitoringConfig

# TODO update the JSON string below
json = "{}"
# create an instance of MonitoringConfig from a JSON string
monitoring_config_instance = MonitoringConfig.from_json(json)
# print the JSON string representation of the object
print(MonitoringConfig.to_json())

# convert the object into a dict
monitoring_config_dict = monitoring_config_instance.to_dict()
# create an instance of MonitoringConfig from a dict
monitoring_config_from_dict = MonitoringConfig.from_dict(monitoring_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

