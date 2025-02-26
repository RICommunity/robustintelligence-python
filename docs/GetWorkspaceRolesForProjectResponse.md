# GetWorkspaceRolesForProjectResponse

GetWorkspaceRolesForProjectResponse returns a list of role pairs of Workspace user roles and their Project user roles.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | [**ID**](ID.md) |  | [optional] 
**role_pairs** | [**List[ParentRoleSubjectRolePair]**](ParentRoleSubjectRolePair.md) | The elements of role_pairs maps each Workspace role to a Project role. | [optional] 

## Example

```python
from ri.apiclient.models.get_workspace_roles_for_project_response import GetWorkspaceRolesForProjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWorkspaceRolesForProjectResponse from a JSON string
get_workspace_roles_for_project_response_instance = GetWorkspaceRolesForProjectResponse.from_json(json)
# print the JSON string representation of the object
print(GetWorkspaceRolesForProjectResponse.to_json())

# convert the object into a dict
get_workspace_roles_for_project_response_dict = get_workspace_roles_for_project_response_instance.to_dict()
# create an instance of GetWorkspaceRolesForProjectResponse from a dict
get_workspace_roles_for_project_response_from_dict = GetWorkspaceRolesForProjectResponse.from_dict(get_workspace_roles_for_project_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

