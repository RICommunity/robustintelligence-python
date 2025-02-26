# ListImagesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**images** | [**List[ManagedImage]**](ManagedImage.md) |  | [optional] 
**next_page_token** | **str** |  | [optional] 

## Example

```python
from ri.apiclient.models.list_images_response import ListImagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListImagesResponse from a JSON string
list_images_response_instance = ListImagesResponse.from_json(json)
# print the JSON string representation of the object
print(ListImagesResponse.to_json())

# convert the object into a dict
list_images_response_dict = list_images_response_instance.to_dict()
# create an instance of ListImagesResponse from a dict
list_images_response_from_dict = ListImagesResponse.from_dict(list_images_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

