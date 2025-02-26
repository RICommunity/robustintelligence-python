# SearchSpec

SearchSpec will return all elements that contain the provided expression as a substring in any of the specified search_fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **str** |  | [optional] 
**search_fields** | **List[str]** |  | [optional] 

## Example

```python
from ri.apiclient.models.search_spec import SearchSpec

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSpec from a JSON string
search_spec_instance = SearchSpec.from_json(json)
# print the JSON string representation of the object
print(SearchSpec.to_json())

# convert the object into a dict
search_spec_dict = search_spec_instance.to_dict()
# create an instance of SearchSpec from a dict
search_spec_from_dict = SearchSpec.from_dict(search_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

