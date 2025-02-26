# PipLibrary

A pip library to install on the Managed Image.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the library. | [optional] 
**version** | **str** | Version of the library. | [optional] 

## Example

```python
from ri.apiclient.models.pip_library import PipLibrary

# TODO update the JSON string below
json = "{}"
# create an instance of PipLibrary from a JSON string
pip_library_instance = PipLibrary.from_json(json)
# print the JSON string representation of the object
print(PipLibrary.to_json())

# convert the object into a dict
pip_library_dict = pip_library_instance.to_dict()
# create an instance of PipLibrary from a dict
pip_library_from_dict = PipLibrary.from_dict(pip_library_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

