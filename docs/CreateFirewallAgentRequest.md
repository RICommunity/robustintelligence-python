# CreateFirewallAgentRequest

CreateFirewallAgentRequest is the request for creating a firewall agent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The agent name given by the user. | [optional] 

## Example

```python
from ri.apiclient.models.create_firewall_agent_request import CreateFirewallAgentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFirewallAgentRequest from a JSON string
create_firewall_agent_request_instance = CreateFirewallAgentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFirewallAgentRequest.to_json())

# convert the object into a dict
create_firewall_agent_request_dict = create_firewall_agent_request_instance.to_dict()
# create an instance of CreateFirewallAgentRequest from a dict
create_firewall_agent_request_from_dict = CreateFirewallAgentRequest.from_dict(create_firewall_agent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

