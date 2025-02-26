# CreateFirewallAgentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | [**ID**](ID.md) |  | [optional] 
**api_token** | **str** | The API token used by the agent for registration. | [optional] 

## Example

```python
from ri.apiclient.models.create_firewall_agent_response import CreateFirewallAgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFirewallAgentResponse from a JSON string
create_firewall_agent_response_instance = CreateFirewallAgentResponse.from_json(json)
# print the JSON string representation of the object
print(CreateFirewallAgentResponse.to_json())

# convert the object into a dict
create_firewall_agent_response_dict = create_firewall_agent_response_instance.to_dict()
# create an instance of CreateFirewallAgentResponse from a dict
create_firewall_agent_response_from_dict = CreateFirewallAgentResponse.from_dict(create_firewall_agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

