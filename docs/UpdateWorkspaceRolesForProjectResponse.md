# UpdateWorkspaceRolesForProjectResponse

UpdateWorkspaceRolesForProjectResponse returns an updated list of role pairs of the Workspace user roles and their Project user roles.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | [**ID**](ID.md) |  | [optional] 
**role_pairs** | [**List[ParentRoleSubjectRolePair]**](ParentRoleSubjectRolePair.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.update_workspace_roles_for_project_response import (
    UpdateWorkspaceRolesForProjectResponse,
)

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkspaceRolesForProjectResponse from a JSON string
update_workspace_roles_for_project_response_instance = (
    UpdateWorkspaceRolesForProjectResponse.from_json(json)
)
# print the JSON string representation of the object
print(UpdateWorkspaceRolesForProjectResponse.to_json())

# convert the object into a dict
update_workspace_roles_for_project_response_dict = (
    update_workspace_roles_for_project_response_instance.to_dict()
)
# create an instance of UpdateWorkspaceRolesForProjectResponse from a dict
update_workspace_roles_for_project_response_from_dict = (
    UpdateWorkspaceRolesForProjectResponse.from_dict(
        update_workspace_roles_for_project_response_dict
    )
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

