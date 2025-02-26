# Agent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | [**ID**](ID.md) |  | [optional] 
**name** | **str** | The user specified name of the agent. | [optional] 
**creation_time** | **datetime** | The time of creation of the agent. | [optional] 
**status** | [**AgentStatus**](AgentStatus.md) |  | [optional] [default to AgentStatus.UNSPECIFIED]
**internal** | **bool** | Specifies whether the agent is an internal agent. Internal agents come bundled with the deployment. | [optional] 
**last_heartbeat_time** | **datetime** | The time of the last heartbeat. | [optional] 
**version** | **str** | Agent version. | [optional] 
**desired_state** | [**AgentDesiredState**](AgentDesiredState.md) |  | [optional] 
**type** | [**AgentType**](AgentType.md) |  | [optional] [default to AgentType.VALIDATION]
**url** | **str** | The url of the agent. E.g., https://dev.my-firewall.rbst.io This is used for firewall agents, which can have a different URL than the control plane. | [optional] 

## Example

```python
from ri.apiclient.models.agent import Agent

# TODO update the JSON string below
json = "{}"
# create an instance of Agent from a JSON string
agent_instance = Agent.from_json(json)
# print the JSON string representation of the object
print(Agent.to_json())

# convert the object into a dict
agent_dict = agent_instance.to_dict()
# create an instance of Agent from a dict
agent_from_dict = Agent.from_dict(agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

