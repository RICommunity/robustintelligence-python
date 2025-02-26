# ListUploadedFileURLsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_urls** | **List[str]** |  | [optional] 

## Example

```python
from ri.apiclient.models.list_uploaded_file_urls_response import (
    ListUploadedFileURLsResponse,
)

# TODO update the JSON string below
json = "{}"
# create an instance of ListUploadedFileURLsResponse from a JSON string
list_uploaded_file_urls_response_instance = ListUploadedFileURLsResponse.from_json(json)
# print the JSON string representation of the object
print(ListUploadedFileURLsResponse.to_json())

# convert the object into a dict
list_uploaded_file_urls_response_dict = (
    list_uploaded_file_urls_response_instance.to_dict()
)
# create an instance of ListUploadedFileURLsResponse from a dict
list_uploaded_file_urls_response_from_dict = ListUploadedFileURLsResponse.from_dict(
    list_uploaded_file_urls_response_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

