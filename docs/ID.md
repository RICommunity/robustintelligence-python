# ID

Unique ID of an object in RIME.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique object ID. | [optional] 

## Example

```python
from ri.apiclient.models.id import ID

# TODO update the JSON string below
json = "{}"
# create an instance of ID from a JSON string
id_instance = ID.from_json(json)
# print the JSON string representation of the object
print(ID.to_json())

# convert the object into a dict
id_dict = id_instance.to_dict()
# create an instance of ID from a dict
id_from_dict = ID.from_dict(id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

