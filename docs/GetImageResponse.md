# GetImageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | [**ManagedImage**](ManagedImage.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.get_image_response import GetImageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetImageResponse from a JSON string
get_image_response_instance = GetImageResponse.from_json(json)
# print the JSON string representation of the object
print(GetImageResponse.to_json())

# convert the object into a dict
get_image_response_dict = get_image_response_instance.to_dict()
# create an instance of GetImageResponse from a dict
get_image_response_from_dict = GetImageResponse.from_dict(get_image_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

