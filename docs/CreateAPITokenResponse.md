# CreateAPITokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | [optional] 
**full_api_token** | **str** |  | [optional] 

## Example

```python
from ri.apiclient.models.create_api_token_response import CreateAPITokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAPITokenResponse from a JSON string
create_api_token_response_instance = CreateAPITokenResponse.from_json(json)
# print the JSON string representation of the object
print(CreateAPITokenResponse.to_json())

# convert the object into a dict
create_api_token_response_dict = create_api_token_response_instance.to_dict()
# create an instance of CreateAPITokenResponse from a dict
create_api_token_response_from_dict = CreateAPITokenResponse.from_dict(create_api_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

