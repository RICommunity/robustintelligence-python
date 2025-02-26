# PipLibraryFilter

Specification of a filter for a pip library.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the library. | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from ri.apiclient.models.pip_library_filter import PipLibraryFilter

# TODO update the JSON string below
json = "{}"
# create an instance of PipLibraryFilter from a JSON string
pip_library_filter_instance = PipLibraryFilter.from_json(json)
# print the JSON string representation of the object
print(PipLibraryFilter.to_json())

# convert the object into a dict
pip_library_filter_dict = pip_library_filter_instance.to_dict()
# create an instance of PipLibraryFilter from a dict
pip_library_filter_from_dict = PipLibraryFilter.from_dict(pip_library_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

