# GetModelCardResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_card** | [**ModelCard**](ModelCard.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.get_model_card_response import GetModelCardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetModelCardResponse from a JSON string
get_model_card_response_instance = GetModelCardResponse.from_json(json)
# print the JSON string representation of the object
print(GetModelCardResponse.to_json())

# convert the object into a dict
get_model_card_response_dict = get_model_card_response_instance.to_dict()
# create an instance of GetModelCardResponse from a dict
get_model_card_response_from_dict = GetModelCardResponse.from_dict(get_model_card_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

