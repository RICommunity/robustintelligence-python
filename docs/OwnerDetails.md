# OwnerDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from ri.apiclient.models.owner_details import OwnerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of OwnerDetails from a JSON string
owner_details_instance = OwnerDetails.from_json(json)
# print the JSON string representation of the object
print(OwnerDetails.to_json())

# convert the object into a dict
owner_details_dict = owner_details_instance.to_dict()
# create an instance of OwnerDetails from a dict
owner_details_from_dict = OwnerDetails.from_dict(owner_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

