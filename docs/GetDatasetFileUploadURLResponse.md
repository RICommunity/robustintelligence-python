# GetDatasetFileUploadURLResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_url** | **str** |  | [optional] 
**done_file_upload_url** | **str** |  | [optional] 
**destination_url** | **str** |  | [optional] 
**upload_limit** | **str** |  | [optional] 

## Example

```python
from ri.apiclient.models.get_dataset_file_upload_url_response import GetDatasetFileUploadURLResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatasetFileUploadURLResponse from a JSON string
get_dataset_file_upload_url_response_instance = GetDatasetFileUploadURLResponse.from_json(json)
# print the JSON string representation of the object
print(GetDatasetFileUploadURLResponse.to_json())

# convert the object into a dict
get_dataset_file_upload_url_response_dict = get_dataset_file_upload_url_response_instance.to_dict()
# create an instance of GetDatasetFileUploadURLResponse from a dict
get_dataset_file_upload_url_response_from_dict = GetDatasetFileUploadURLResponse.from_dict(get_dataset_file_upload_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

