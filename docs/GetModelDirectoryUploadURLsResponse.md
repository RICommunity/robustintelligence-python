# GetModelDirectoryUploadURLsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_path_map** | **Dict[str, str]** |  | [optional] 
**done_file_upload_url** | **str** |  | [optional] 
**destination_url** | **str** |  | [optional] 
**upload_limit** | **str** |  | [optional] 

## Example

```python
from ri.apiclient.models.get_model_directory_upload_urls_response import GetModelDirectoryUploadURLsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetModelDirectoryUploadURLsResponse from a JSON string
get_model_directory_upload_urls_response_instance = GetModelDirectoryUploadURLsResponse.from_json(json)
# print the JSON string representation of the object
print(GetModelDirectoryUploadURLsResponse.to_json())

# convert the object into a dict
get_model_directory_upload_urls_response_dict = get_model_directory_upload_urls_response_instance.to_dict()
# create an instance of GetModelDirectoryUploadURLsResponse from a dict
get_model_directory_upload_urls_response_from_dict = GetModelDirectoryUploadURLsResponse.from_dict(get_model_directory_upload_urls_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

