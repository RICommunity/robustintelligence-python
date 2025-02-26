# GetValidatePredictionsTaskStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**ValidatePredictionsResponse**](ValidatePredictionsResponse.md) |  | [optional] 
**job_metadata** | [**JobMetadata**](JobMetadata.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.get_validate_predictions_task_status_response import GetValidatePredictionsTaskStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetValidatePredictionsTaskStatusResponse from a JSON string
get_validate_predictions_task_status_response_instance = GetValidatePredictionsTaskStatusResponse.from_json(json)
# print the JSON string representation of the object
print(GetValidatePredictionsTaskStatusResponse.to_json())

# convert the object into a dict
get_validate_predictions_task_status_response_dict = get_validate_predictions_task_status_response_instance.to_dict()
# create an instance of GetValidatePredictionsTaskStatusResponse from a dict
get_validate_predictions_task_status_response_from_dict = GetValidatePredictionsTaskStatusResponse.from_dict(get_validate_predictions_task_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

