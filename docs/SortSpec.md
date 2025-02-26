# SortSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sort_order** | [**Order**](Order.md) |  | [optional] [default to Order.UNSPECIFIED]
**sort_by** | **str** |  | [optional] 

## Example

```python
from ri.apiclient.models.sort_spec import SortSpec

# TODO update the JSON string below
json = "{}"
# create an instance of SortSpec from a JSON string
sort_spec_instance = SortSpec.from_json(json)
# print the JSON string representation of the object
print(SortSpec.to_json())

# convert the object into a dict
sort_spec_dict = sort_spec_instance.to_dict()
# create an instance of SortSpec from a dict
sort_spec_from_dict = SortSpec.from_dict(sort_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

