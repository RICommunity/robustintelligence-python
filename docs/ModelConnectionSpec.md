# ModelConnectionSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http** | [**HttpConnectionSpec**](HttpConnectionSpec.md) |  | [optional] 
**bedrock** | [**BedrockConnectionSpec**](BedrockConnectionSpec.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.model_connection_spec import ModelConnectionSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ModelConnectionSpec from a JSON string
model_connection_spec_instance = ModelConnectionSpec.from_json(json)
# print the JSON string representation of the object
print(ModelConnectionSpec.to_json())

# convert the object into a dict
model_connection_spec_dict = model_connection_spec_instance.to_dict()
# create an instance of ModelConnectionSpec from a dict
model_connection_spec_from_dict = ModelConnectionSpec.from_dict(model_connection_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

