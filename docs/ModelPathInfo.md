# ModelPathInfo

Represents info for a file at path that interfaces with a model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The path to the model.  This can be a local path or a path to a file in a configured integration. | 

## Example

```python
from ri.apiclient.models.model_path_info import ModelPathInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ModelPathInfo from a JSON string
model_path_info_instance = ModelPathInfo.from_json(json)
# print the JSON string representation of the object
print(ModelPathInfo.to_json())

# convert the object into a dict
model_path_info_dict = model_path_info_instance.to_dict()
# create an instance of ModelPathInfo from a dict
model_path_info_from_dict = ModelPathInfo.from_dict(model_path_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

