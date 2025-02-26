# ManagedImage

A representation of a custom Image whose tag or version is managed by the ImageRegistry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The external name of the image. This name must match the /^[a-z][a-z0-9]*(?:[_-][a-z0-9]+)*$/ regular expression. See the naming rules in https://docs.docker.com/engine/reference/commandline/tag/#extended-description https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html from which the naming convention derives. The above names are valid ECR or Docker image names. | [optional] 
**base_image** | [**ImageReference**](ImageReference.md) |  | [optional] 
**role_type** | [**RoleType**](RoleType.md) |  | [optional] [default to RoleType.UNSPECIFIED]
**child_images** | [**List[ImageReference]**](ImageReference.md) | The set of images that use this image as a source. | [optional] 
**rime_tag** | **str** | The tag of the RIME wheel used to build the managed image. | [optional] 
**repo_uri** | **str** | The URI of the repository. | [optional] 
**status** | [**ManagedImageStatus**](ManagedImageStatus.md) |  | [optional] [default to ManagedImageStatus.UNSPECIFIED]
**package_requirements** | [**List[PackageRequirement]**](PackageRequirement.md) | A list of all system package requirements used to build this image. | [optional] 
**pip_requirements** | [**List[PipRequirement]**](PipRequirement.md) | A list of all pip requirements used to build this image. | [optional] 
**pip_libraries** | [**List[PipLibrary]**](PipLibrary.md) | A list of all pip libraries installed on this image as obtained by running &#x60;pip list&#x60;. | [optional] 
**python_version** | **str** | The version of Python used to build the Robust Intelligence image. | [optional] 

## Example

```python
from ri.apiclient.models.managed_image import ManagedImage

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedImage from a JSON string
managed_image_instance = ManagedImage.from_json(json)
# print the JSON string representation of the object
print(ManagedImage.to_json())

# convert the object into a dict
managed_image_dict = managed_image_instance.to_dict()
# create an instance of ManagedImage from a dict
managed_image_from_dict = ManagedImage.from_dict(managed_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

