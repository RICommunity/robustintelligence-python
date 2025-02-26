# ModelWithOwnerDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | [**Model**](Model.md) |  | [optional] 
**owner_details** | [**OwnerDetails**](OwnerDetails.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.model_with_owner_details import ModelWithOwnerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ModelWithOwnerDetails from a JSON string
model_with_owner_details_instance = ModelWithOwnerDetails.from_json(json)
# print the JSON string representation of the object
print(ModelWithOwnerDetails.to_json())

# convert the object into a dict
model_with_owner_details_dict = model_with_owner_details_instance.to_dict()
# create an instance of ModelWithOwnerDetails from a dict
model_with_owner_details_from_dict = ModelWithOwnerDetails.from_dict(model_with_owner_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

