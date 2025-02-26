# GetUpgradeForAgentResponse

GetUpgradeForAgentResponse is the response for GetUpgradeForAgent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**desired_state** | [**AgentDesiredState**](AgentDesiredState.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.get_upgrade_for_agent_response import GetUpgradeForAgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUpgradeForAgentResponse from a JSON string
get_upgrade_for_agent_response_instance = GetUpgradeForAgentResponse.from_json(json)
# print the JSON string representation of the object
print(GetUpgradeForAgentResponse.to_json())

# convert the object into a dict
get_upgrade_for_agent_response_dict = get_upgrade_for_agent_response_instance.to_dict()
# create an instance of GetUpgradeForAgentResponse from a dict
get_upgrade_for_agent_response_from_dict = GetUpgradeForAgentResponse.from_dict(get_upgrade_for_agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

