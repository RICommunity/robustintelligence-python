# APITokenInfo

API token object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | [optional] 
**name** | **str** | The name of the API token. | [optional] 
**suffix** | **str** | The suffix of the API token, which is visible in the Robust Intelligence web application. | [optional] 
**creation_time** | **datetime** |  | [optional] 
**expiration_time** | **datetime** |  | [optional] 
**workspace_id** | [**ID**](ID.md) |  | [optional] 
**user_id** | **str** | The ID of the user who created the API token. | [optional] 
**token_type** | [**TokenType**](TokenType.md) |  | [optional] [default to TokenType.UNSPECIFIED]

## Example

```python
from ri.apiclient.models.api_token_info import APITokenInfo

# TODO update the JSON string below
json = "{}"
# create an instance of APITokenInfo from a JSON string
api_token_info_instance = APITokenInfo.from_json(json)
# print the JSON string representation of the object
print(APITokenInfo.to_json())

# convert the object into a dict
api_token_info_dict = api_token_info_instance.to_dict()
# create an instance of APITokenInfo from a dict
api_token_info_from_dict = APITokenInfo.from_dict(api_token_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

