# GetAgentResponse

GetAgentResponse is the response returns a single agent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent** | [**Agent**](Agent.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.get_agent_response import GetAgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAgentResponse from a JSON string
get_agent_response_instance = GetAgentResponse.from_json(json)
# print the JSON string representation of the object
print(GetAgentResponse.to_json())

# convert the object into a dict
get_agent_response_dict = get_agent_response_instance.to_dict()
# create an instance of GetAgentResponse from a dict
get_agent_response_from_dict = GetAgentResponse.from_dict(get_agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

