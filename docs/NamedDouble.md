# NamedDouble


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from ri.apiclient.models.named_double import NamedDouble

# TODO update the JSON string below
json = "{}"
# create an instance of NamedDouble from a JSON string
named_double_instance = NamedDouble.from_json(json)
# print the JSON string representation of the object
print(NamedDouble.to_json())

# convert the object into a dict
named_double_dict = named_double_instance.to_dict()
# create an instance of NamedDouble from a dict
named_double_from_dict = NamedDouble.from_dict(named_double_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

