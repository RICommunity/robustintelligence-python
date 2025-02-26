# FavoriteProjects

Up to 3 favorite project_ids for each workspace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | [**ID**](ID.md) |  | [optional] 
**project_ids** | [**List[ID]**](ID.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.favorite_projects import FavoriteProjects

# TODO update the JSON string below
json = "{}"
# create an instance of FavoriteProjects from a JSON string
favorite_projects_instance = FavoriteProjects.from_json(json)
# print the JSON string representation of the object
print(FavoriteProjects.to_json())

# convert the object into a dict
favorite_projects_dict = favorite_projects_instance.to_dict()
# create an instance of FavoriteProjects from a dict
favorite_projects_from_dict = FavoriteProjects.from_dict(favorite_projects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

