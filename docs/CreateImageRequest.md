# CreateImageRequest

Request and response for a CreateImage RPC.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Managed Image.  Name must match the regexp described in managed_image.proto  for &#x60;ManagedImage.name&#x60;. | 
**pip_requirements** | [**List[PipRequirement]**](PipRequirement.md) | List of &#x60;pip&#x60; requirements that specify the customization used for this Image. | 
**package_requirements** | [**List[PackageRequirement]**](PackageRequirement.md) | List of system requirements that specify the customization used for this Image. | [optional] 
**python_version** | **str** | The version of the Python interpreter to use. | [optional] 

## Example

```python
from ri.apiclient.models.create_image_request import CreateImageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateImageRequest from a JSON string
create_image_request_instance = CreateImageRequest.from_json(json)
# print the JSON string representation of the object
print(CreateImageRequest.to_json())

# convert the object into a dict
create_image_request_dict = create_image_request_instance.to_dict()
# create an instance of CreateImageRequest from a dict
create_image_request_from_dict = CreateImageRequest.from_dict(create_image_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

