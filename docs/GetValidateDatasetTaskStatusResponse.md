# GetValidateDatasetTaskStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**ValidateDatasetResponse**](ValidateDatasetResponse.md) |  | [optional] 
**job_metadata** | [**JobMetadata**](JobMetadata.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.get_validate_dataset_task_status_response import GetValidateDatasetTaskStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetValidateDatasetTaskStatusResponse from a JSON string
get_validate_dataset_task_status_response_instance = GetValidateDatasetTaskStatusResponse.from_json(json)
# print the JSON string representation of the object
print(GetValidateDatasetTaskStatusResponse.to_json())

# convert the object into a dict
get_validate_dataset_task_status_response_dict = get_validate_dataset_task_status_response_instance.to_dict()
# create an instance of GetValidateDatasetTaskStatusResponse from a dict
get_validate_dataset_task_status_response_from_dict = GetValidateDatasetTaskStatusResponse.from_dict(get_validate_dataset_task_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

