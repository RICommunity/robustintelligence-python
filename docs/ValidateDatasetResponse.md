# ValidateDatasetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_valid** | **bool** |  | [optional] 
**error_message** | **str** |  | [optional] 
**validation_status** | [**ValidityStatus**](ValidityStatus.md) |  | [optional] [default to ValidityStatus.UNSPECIFIED]
**size_bytes** | **str** |  | [optional] 

## Example

```python
from ri.apiclient.models.validate_dataset_response import ValidateDatasetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateDatasetResponse from a JSON string
validate_dataset_response_instance = ValidateDatasetResponse.from_json(json)
# print the JSON string representation of the object
print(ValidateDatasetResponse.to_json())

# convert the object into a dict
validate_dataset_response_dict = validate_dataset_response_instance.to_dict()
# create an instance of ValidateDatasetResponse from a dict
validate_dataset_response_from_dict = ValidateDatasetResponse.from_dict(validate_dataset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

