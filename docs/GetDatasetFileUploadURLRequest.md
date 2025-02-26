# GetDatasetFileUploadURLRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | Path of dataset file on the local file system. | 
**upload_path** | **str** | Specify a path in the blob store to use for data uploads. | [optional] 

## Example

```python
from ri.apiclient.models.get_dataset_file_upload_url_request import GetDatasetFileUploadURLRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatasetFileUploadURLRequest from a JSON string
get_dataset_file_upload_url_request_instance = GetDatasetFileUploadURLRequest.from_json(json)
# print the JSON string representation of the object
print(GetDatasetFileUploadURLRequest.to_json())

# convert the object into a dict
get_dataset_file_upload_url_request_dict = get_dataset_file_upload_url_request_instance.to_dict()
# create an instance of GetDatasetFileUploadURLRequest from a dict
get_dataset_file_upload_url_request_from_dict = GetDatasetFileUploadURLRequest.from_dict(get_dataset_file_upload_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

