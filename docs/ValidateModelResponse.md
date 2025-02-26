# ValidateModelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_valid** | **bool** |  | [optional] 
**error_message** | **str** |  | [optional] 
**validation_status** | [**ValidityStatus**](ValidityStatus.md) |  | [optional] [default to ValidityStatus.UNSPECIFIED]

## Example

```python
from ri.apiclient.models.validate_model_response import ValidateModelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateModelResponse from a JSON string
validate_model_response_instance = ValidateModelResponse.from_json(json)
# print the JSON string representation of the object
print(ValidateModelResponse.to_json())

# convert the object into a dict
validate_model_response_dict = validate_model_response_instance.to_dict()
# create an instance of ValidateModelResponse from a dict
validate_model_response_from_dict = ValidateModelResponse.from_dict(validate_model_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

