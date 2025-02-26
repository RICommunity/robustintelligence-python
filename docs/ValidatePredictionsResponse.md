# ValidatePredictionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_valid** | **bool** |  | [optional] 
**error_message** | **str** |  | [optional] 
**validation_status** | [**ValidityStatus**](ValidityStatus.md) |  | [optional] [default to ValidityStatus.UNSPECIFIED]

## Example

```python
from ri.apiclient.models.validate_predictions_response import (
    ValidatePredictionsResponse,
)

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatePredictionsResponse from a JSON string
validate_predictions_response_instance = ValidatePredictionsResponse.from_json(json)
# print the JSON string representation of the object
print(ValidatePredictionsResponse.to_json())

# convert the object into a dict
validate_predictions_response_dict = validate_predictions_response_instance.to_dict()
# create an instance of ValidatePredictionsResponse from a dict
validate_predictions_response_from_dict = ValidatePredictionsResponse.from_dict(
    validate_predictions_response_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

