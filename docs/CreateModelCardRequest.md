# CreateModelCardRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_card** | [**ModelCard**](ModelCard.md) |  | [optional] 
**project_id** | [**ID**](ID.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.create_model_card_request import CreateModelCardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateModelCardRequest from a JSON string
create_model_card_request_instance = CreateModelCardRequest.from_json(json)
# print the JSON string representation of the object
print(CreateModelCardRequest.to_json())

# convert the object into a dict
create_model_card_request_dict = create_model_card_request_instance.to_dict()
# create an instance of CreateModelCardRequest from a dict
create_model_card_request_from_dict = CreateModelCardRequest.from_dict(create_model_card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

