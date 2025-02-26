# RegisterPredictionSetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registry_validation_job_id** | [**ID**](ID.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.register_prediction_set_response import (
    RegisterPredictionSetResponse,
)

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterPredictionSetResponse from a JSON string
register_prediction_set_response_instance = RegisterPredictionSetResponse.from_json(
    json
)
# print the JSON string representation of the object
print(RegisterPredictionSetResponse.to_json())

# convert the object into a dict
register_prediction_set_response_dict = (
    register_prediction_set_response_instance.to_dict()
)
# create an instance of RegisterPredictionSetResponse from a dict
register_prediction_set_response_from_dict = RegisterPredictionSetResponse.from_dict(
    register_prediction_set_response_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

