# CreateAPITokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the API token. | 
**workspace_id** | [**ID**](ID.md) |  | [optional] 
**token_type** | [**TokenType**](TokenType.md) |  | [optional] [default to TokenType.UNSPECIFIED]
**agent_id** | [**ID**](ID.md) |  | [optional] 
**expiry_days** | **int** |  | [optional] 

## Example

```python
from ri.apiclient.models.create_api_token_request import CreateAPITokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAPITokenRequest from a JSON string
create_api_token_request_instance = CreateAPITokenRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAPITokenRequest.to_json())

# convert the object into a dict
create_api_token_request_dict = create_api_token_request_instance.to_dict()
# create an instance of CreateAPITokenRequest from a dict
create_api_token_request_from_dict = CreateAPITokenRequest.from_dict(create_api_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

