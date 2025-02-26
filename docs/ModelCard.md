# ModelCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_card_id** | [**ID**](ID.md) |  | [optional] 
**details** | **str** |  | [optional] 

## Example

```python
from ri.apiclient.models.model_card import ModelCard

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCard from a JSON string
model_card_instance = ModelCard.from_json(json)
# print the JSON string representation of the object
print(ModelCard.to_json())

# convert the object into a dict
model_card_dict = model_card_instance.to_dict()
# create an instance of ModelCard from a dict
model_card_from_dict = ModelCard.from_dict(model_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

