# ListModelCardsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_card_map** | [**Dict[str, ModelCard]**](ModelCard.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.list_model_cards_response import ListModelCardsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListModelCardsResponse from a JSON string
list_model_cards_response_instance = ListModelCardsResponse.from_json(json)
# print the JSON string representation of the object
print(ListModelCardsResponse.to_json())

# convert the object into a dict
list_model_cards_response_dict = list_model_cards_response_instance.to_dict()
# create an instance of ListModelCardsResponse from a dict
list_model_cards_response_from_dict = ListModelCardsResponse.from_dict(list_model_cards_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

