# UpdateAgentAPITokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | [**ID**](ID.md) |  | 

## Example

```python
from ri.apiclient.models.update_agent_api_token_request import UpdateAgentAPITokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAgentAPITokenRequest from a JSON string
update_agent_api_token_request_instance = UpdateAgentAPITokenRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAgentAPITokenRequest.to_json())

# convert the object into a dict
update_agent_api_token_request_dict = update_agent_api_token_request_instance.to_dict()
# create an instance of UpdateAgentAPITokenRequest from a dict
update_agent_api_token_request_from_dict = UpdateAgentAPITokenRequest.from_dict(update_agent_api_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

