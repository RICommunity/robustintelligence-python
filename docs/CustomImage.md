# CustomImage

CustomImage is an external image provided by the customer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the custom image (e.g. a docker image name). | [optional] 
**pull_secret** | [**PullSecret**](PullSecret.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.custom_image import CustomImage

# TODO update the JSON string below
json = "{}"
# create an instance of CustomImage from a JSON string
custom_image_instance = CustomImage.from_json(json)
# print the JSON string representation of the object
print(CustomImage.to_json())

# convert the object into a dict
custom_image_dict = custom_image_instance.to_dict()
# create an instance of CustomImage from a dict
custom_image_from_dict = CustomImage.from_dict(custom_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

