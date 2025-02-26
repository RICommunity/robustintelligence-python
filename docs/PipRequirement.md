# PipRequirement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the library. | [optional] 
**version_specifier** | **str** | Specifier for a version of the library, see: https://www.python.org/dev/peps/pep-0440/#version-specifiers or https://peps.python.org/pep-0440/ for reference.  TODO[RIME-7908]: Remove this unsafe usage once we have a way of  allowing for unescaped HTML characters. | [optional] 

## Example

```python
from ri.apiclient.models.pip_requirement import PipRequirement

# TODO update the JSON string below
json = "{}"
# create an instance of PipRequirement from a JSON string
pip_requirement_instance = PipRequirement.from_json(json)
# print the JSON string representation of the object
print(PipRequirement.to_json())

# convert the object into a dict
pip_requirement_dict = pip_requirement_instance.to_dict()
# create an instance of PipRequirement from a dict
pip_requirement_from_dict = PipRequirement.from_dict(pip_requirement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

