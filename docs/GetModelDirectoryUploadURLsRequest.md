# GetModelDirectoryUploadURLsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**directory_name** | **str** | Path of model directory on local file system. | 
**relative_file_paths** | **List[str]** | Array of relative paths from the model directory to model files. | 
**upload_path** | **str** | Specify a path in the blob store to which the model will be uploaded. | [optional] 

## Example

```python
from ri.apiclient.models.get_model_directory_upload_urls_request import GetModelDirectoryUploadURLsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetModelDirectoryUploadURLsRequest from a JSON string
get_model_directory_upload_urls_request_instance = GetModelDirectoryUploadURLsRequest.from_json(json)
# print the JSON string representation of the object
print(GetModelDirectoryUploadURLsRequest.to_json())

# convert the object into a dict
get_model_directory_upload_urls_request_dict = get_model_directory_upload_urls_request_instance.to_dict()
# create an instance of GetModelDirectoryUploadURLsRequest from a dict
get_model_directory_upload_urls_request_from_dict = GetModelDirectoryUploadURLsRequest.from_dict(get_model_directory_upload_urls_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

