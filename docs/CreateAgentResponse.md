# CreateAgentResponse

CreateAgentResponse is a response that contains the configuration values required for installing the agent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **bytearray** | File that contains configuration values for installing the agent. | [optional] 
**agent_id** | [**ID**](ID.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.create_agent_response import CreateAgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAgentResponse from a JSON string
create_agent_response_instance = CreateAgentResponse.from_json(json)
# print the JSON string representation of the object
print(CreateAgentResponse.to_json())

# convert the object into a dict
create_agent_response_dict = create_agent_response_instance.to_dict()
# create an instance of CreateAgentResponse from a dict
create_agent_response_from_dict = CreateAgentResponse.from_dict(create_agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

