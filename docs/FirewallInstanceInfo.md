# FirewallInstanceInfo

Information about a single Firewall Instance, including its configuration and the current status of its deployment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firewall_instance_id** | [**ID**](ID.md) |  | [optional] 
**config** | [**FirewallRuleConfig**](FirewallRuleConfig.md) |  | [optional] 
**deployment_status** | [**FirewallInstanceStatus**](FirewallInstanceStatus.md) |  | [optional] [default to FirewallInstanceStatus.UNSPECIFIED]
**description** | **str** | Optional human-readable description of the firewall instance. | [optional] 
**agent_id** | [**ID**](ID.md) |  | [optional] 
**spec** | [**FirewallInstanceDeploymentConfig**](FirewallInstanceDeploymentConfig.md) |  | [optional] 
**last_heartbeat_time** | **datetime** | Last time the control plan received a heartbeat from the firewall instance. | [optional] 

## Example

```python
from ri.apiclient.models.firewall_instance_info import FirewallInstanceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallInstanceInfo from a JSON string
firewall_instance_info_instance = FirewallInstanceInfo.from_json(json)
# print the JSON string representation of the object
print(FirewallInstanceInfo.to_json())

# convert the object into a dict
firewall_instance_info_dict = firewall_instance_info_instance.to_dict()
# create an instance of FirewallInstanceInfo from a dict
firewall_instance_info_from_dict = FirewallInstanceInfo.from_dict(firewall_instance_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

