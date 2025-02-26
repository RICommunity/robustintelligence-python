# UpdateModelCardResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_card** | [**ModelCard**](ModelCard.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.update_model_card_response import UpdateModelCardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateModelCardResponse from a JSON string
update_model_card_response_instance = UpdateModelCardResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateModelCardResponse.to_json())

# convert the object into a dict
update_model_card_response_dict = update_model_card_response_instance.to_dict()
# create an instance of UpdateModelCardResponse from a dict
update_model_card_response_from_dict = UpdateModelCardResponse.from_dict(
    update_model_card_response_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

