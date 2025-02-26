# RegisterDatasetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | **str** | dataset_id is a string as it contains semantic meaning and does not adhere to ID standard. | [optional] 
**registry_validation_job_id** | [**ID**](ID.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.register_dataset_response import RegisterDatasetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterDatasetResponse from a JSON string
register_dataset_response_instance = RegisterDatasetResponse.from_json(json)
# print the JSON string representation of the object
print(RegisterDatasetResponse.to_json())

# convert the object into a dict
register_dataset_response_dict = register_dataset_response_instance.to_dict()
# create an instance of RegisterDatasetResponse from a dict
register_dataset_response_from_dict = RegisterDatasetResponse.from_dict(register_dataset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

