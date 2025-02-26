# SyncImageTagResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | [**ManagedImage**](ManagedImage.md) |  | [optional] 
**job** | [**JobMetadata**](JobMetadata.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.sync_image_tag_response import SyncImageTagResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SyncImageTagResponse from a JSON string
sync_image_tag_response_instance = SyncImageTagResponse.from_json(json)
# print the JSON string representation of the object
print(SyncImageTagResponse.to_json())

# convert the object into a dict
sync_image_tag_response_dict = sync_image_tag_response_instance.to_dict()
# create an instance of SyncImageTagResponse from a dict
sync_image_tag_response_from_dict = SyncImageTagResponse.from_dict(sync_image_tag_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

