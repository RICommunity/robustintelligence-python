# ProjectWithDetails

ProjectWithDetails returns the Project and the Project Owner's details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | [**Project**](Project.md) |  | [optional] 
**owner_details** | [**OwnerDetails**](OwnerDetails.md) |  | [optional] 
**last_updated_time** | **datetime** |  | [optional] 

## Example

```python
from ri.apiclient.models.project_with_details import ProjectWithDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectWithDetails from a JSON string
project_with_details_instance = ProjectWithDetails.from_json(json)
# print the JSON string representation of the object
print(ProjectWithDetails.to_json())

# convert the object into a dict
project_with_details_dict = project_with_details_instance.to_dict()
# create an instance of ProjectWithDetails from a dict
project_with_details_from_dict = ProjectWithDetails.from_dict(project_with_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

