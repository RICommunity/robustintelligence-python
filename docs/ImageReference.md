# ImageReference

A reference to another image, managed or not.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the image being referenced. For a managed image, this is the &#x60;name&#x60; record of the &#x60;ManagedImage&#x60; object. For an external image, this is the full name of that image. | [optional] 
**reference_type** | [**ReferenceType**](ReferenceType.md) |  | [optional] [default to ReferenceType.UNSPECIFIED]

## Example

```python
from ri.apiclient.models.image_reference import ImageReference

# TODO update the JSON string below
json = "{}"
# create an instance of ImageReference from a JSON string
image_reference_instance = ImageReference.from_json(json)
# print the JSON string representation of the object
print(ImageReference.to_json())

# convert the object into a dict
image_reference_dict = image_reference_instance.to_dict()
# create an instance of ImageReference from a dict
image_reference_from_dict = ImageReference.from_dict(image_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

