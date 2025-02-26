# StrList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **List[str]** |  | [optional] 

## Example

```python
from ri.apiclient.models.str_list import StrList

# TODO update the JSON string below
json = "{}"
# create an instance of StrList from a JSON string
str_list_instance = StrList.from_json(json)
# print the JSON string representation of the object
print(StrList.to_json())

# convert the object into a dict
str_list_dict = str_list_instance.to_dict()
# create an instance of StrList from a dict
str_list_from_dict = StrList.from_dict(str_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

