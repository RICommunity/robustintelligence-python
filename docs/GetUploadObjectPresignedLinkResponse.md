# GetUploadObjectPresignedLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 

## Example

```python
from ri.apiclient.models.get_upload_object_presigned_link_response import (
    GetUploadObjectPresignedLinkResponse,
)

# TODO update the JSON string below
json = "{}"
# create an instance of GetUploadObjectPresignedLinkResponse from a JSON string
get_upload_object_presigned_link_response_instance = (
    GetUploadObjectPresignedLinkResponse.from_json(json)
)
# print the JSON string representation of the object
print(GetUploadObjectPresignedLinkResponse.to_json())

# convert the object into a dict
get_upload_object_presigned_link_response_dict = (
    get_upload_object_presigned_link_response_instance.to_dict()
)
# create an instance of GetUploadObjectPresignedLinkResponse from a dict
get_upload_object_presigned_link_response_from_dict = (
    GetUploadObjectPresignedLinkResponse.from_dict(
        get_upload_object_presigned_link_response_dict
    )
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

