# RegisterModelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | [**ID**](ID.md) |  | [optional] 
**registry_validation_job_id** | [**ID**](ID.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.register_model_response import RegisterModelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterModelResponse from a JSON string
register_model_response_instance = RegisterModelResponse.from_json(json)
# print the JSON string representation of the object
print(RegisterModelResponse.to_json())

# convert the object into a dict
register_model_response_dict = register_model_response_instance.to_dict()
# create an instance of RegisterModelResponse from a dict
register_model_response_from_dict = RegisterModelResponse.from_dict(register_model_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

