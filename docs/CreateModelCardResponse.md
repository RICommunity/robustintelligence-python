# CreateModelCardResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_card_id** | [**ID**](ID.md) |  | 

## Example

```python
from ri.apiclient.models.create_model_card_response import CreateModelCardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateModelCardResponse from a JSON string
create_model_card_response_instance = CreateModelCardResponse.from_json(json)
# print the JSON string representation of the object
print(CreateModelCardResponse.to_json())

# convert the object into a dict
create_model_card_response_dict = create_model_card_response_instance.to_dict()
# create an instance of CreateModelCardResponse from a dict
create_model_card_response_from_dict = CreateModelCardResponse.from_dict(create_model_card_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

