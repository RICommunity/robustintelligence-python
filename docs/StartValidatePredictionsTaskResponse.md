# StartValidatePredictionsTaskResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | [**ID**](ID.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.start_validate_predictions_task_response import StartValidatePredictionsTaskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StartValidatePredictionsTaskResponse from a JSON string
start_validate_predictions_task_response_instance = StartValidatePredictionsTaskResponse.from_json(json)
# print the JSON string representation of the object
print(StartValidatePredictionsTaskResponse.to_json())

# convert the object into a dict
start_validate_predictions_task_response_dict = start_validate_predictions_task_response_instance.to_dict()
# create an instance of StartValidatePredictionsTaskResponse from a dict
start_validate_predictions_task_response_from_dict = StartValidatePredictionsTaskResponse.from_dict(start_validate_predictions_task_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

