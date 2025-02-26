# CustomImageType

CustomImageType is a union of all possible custom managed image and RI managed image.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_image** | [**CustomImage**](CustomImage.md) |  | [optional] 
**managed_image_name** | **str** | Name of the RI managed image. | [optional] 

## Example

```python
from ri.apiclient.models.custom_image_type import CustomImageType

# TODO update the JSON string below
json = "{}"
# create an instance of CustomImageType from a JSON string
custom_image_type_instance = CustomImageType.from_json(json)
# print the JSON string representation of the object
print(CustomImageType.to_json())

# convert the object into a dict
custom_image_type_dict = custom_image_type_instance.to_dict()
# create an instance of CustomImageType from a dict
custom_image_type_from_dict = CustomImageType.from_dict(custom_image_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

