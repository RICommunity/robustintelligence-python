# DeleteModelCardResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_card_id** | [**ID**](ID.md) |  | 

## Example

```python
from ri.apiclient.models.delete_model_card_response import DeleteModelCardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteModelCardResponse from a JSON string
delete_model_card_response_instance = DeleteModelCardResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteModelCardResponse.to_json())

# convert the object into a dict
delete_model_card_response_dict = delete_model_card_response_instance.to_dict()
# create an instance of DeleteModelCardResponse from a dict
delete_model_card_response_from_dict = DeleteModelCardResponse.from_dict(delete_model_card_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

