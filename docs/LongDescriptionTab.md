# LongDescriptionTab


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**contents** | **str** |  | [optional] 

## Example

```python
from ri.apiclient.models.long_description_tab import LongDescriptionTab

# TODO update the JSON string below
json = "{}"
# create an instance of LongDescriptionTab from a JSON string
long_description_tab_instance = LongDescriptionTab.from_json(json)
# print the JSON string representation of the object
print(LongDescriptionTab.to_json())

# convert the object into a dict
long_description_tab_dict = long_description_tab_instance.to_dict()
# create an instance of LongDescriptionTab from a dict
long_description_tab_from_dict = LongDescriptionTab.from_dict(long_description_tab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

