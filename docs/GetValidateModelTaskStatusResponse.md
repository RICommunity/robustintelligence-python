# GetValidateModelTaskStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**ValidateModelResponse**](ValidateModelResponse.md) |  | [optional] 
**job_metadata** | [**JobMetadata**](JobMetadata.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.get_validate_model_task_status_response import GetValidateModelTaskStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetValidateModelTaskStatusResponse from a JSON string
get_validate_model_task_status_response_instance = GetValidateModelTaskStatusResponse.from_json(json)
# print the JSON string representation of the object
print(GetValidateModelTaskStatusResponse.to_json())

# convert the object into a dict
get_validate_model_task_status_response_dict = get_validate_model_task_status_response_instance.to_dict()
# create an instance of GetValidateModelTaskStatusResponse from a dict
get_validate_model_task_status_response_from_dict = GetValidateModelTaskStatusResponse.from_dict(get_validate_model_task_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

