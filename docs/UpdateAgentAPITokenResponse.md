# UpdateAgentAPITokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_api_token** | **str** |  | [optional] 

## Example

```python
from ri.apiclient.models.update_agent_api_token_response import UpdateAgentAPITokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAgentAPITokenResponse from a JSON string
update_agent_api_token_response_instance = UpdateAgentAPITokenResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateAgentAPITokenResponse.to_json())

# convert the object into a dict
update_agent_api_token_response_dict = update_agent_api_token_response_instance.to_dict()
# create an instance of UpdateAgentAPITokenResponse from a dict
update_agent_api_token_response_from_dict = UpdateAgentAPITokenResponse.from_dict(update_agent_api_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

