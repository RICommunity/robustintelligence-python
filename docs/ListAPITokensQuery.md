# ListAPITokensQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_type** | [**TokenType**](TokenType.md) |  | [optional] [default to TokenType.UNSPECIFIED]

## Example

```python
from ri.apiclient.models.list_api_tokens_query import ListAPITokensQuery

# TODO update the JSON string below
json = "{}"
# create an instance of ListAPITokensQuery from a JSON string
list_api_tokens_query_instance = ListAPITokensQuery.from_json(json)
# print the JSON string representation of the object
print(ListAPITokensQuery.to_json())

# convert the object into a dict
list_api_tokens_query_dict = list_api_tokens_query_instance.to_dict()
# create an instance of ListAPITokensQuery from a dict
list_api_tokens_query_from_dict = ListAPITokensQuery.from_dict(list_api_tokens_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

