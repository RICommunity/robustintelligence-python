# PackageRequirement

A requirement specifying a system package to install on the Image.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the package. | [optional] 
**version_specifier** | **str** |  | [optional] 
**package_type** | [**ManagedImagePackageType**](ManagedImagePackageType.md) |  | [optional] [default to ManagedImagePackageType.UNSPECIFIED]

## Example

```python
from ri.apiclient.models.package_requirement import PackageRequirement

# TODO update the JSON string below
json = "{}"
# create an instance of PackageRequirement from a JSON string
package_requirement_instance = PackageRequirement.from_json(json)
# print the JSON string representation of the object
print(PackageRequirement.to_json())

# convert the object into a dict
package_requirement_dict = package_requirement_instance.to_dict()
# create an instance of PackageRequirement from a dict
package_requirement_from_dict = PackageRequirement.from_dict(package_requirement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

