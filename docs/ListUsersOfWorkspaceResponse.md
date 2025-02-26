# ListUsersOfWorkspaceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | [**ID**](ID.md) |  | [optional] 
**users** | [**List[UserDetailWithRole]**](UserDetailWithRole.md) |  | [optional] 
**next_page_token** | **str** |  | [optional] 
**has_more** | **bool** |  | [optional] 

## Example

```python
from ri.apiclient.models.list_users_of_workspace_response import (
    ListUsersOfWorkspaceResponse,
)

# TODO update the JSON string below
json = "{}"
# create an instance of ListUsersOfWorkspaceResponse from a JSON string
list_users_of_workspace_response_instance = ListUsersOfWorkspaceResponse.from_json(json)
# print the JSON string representation of the object
print(ListUsersOfWorkspaceResponse.to_json())

# convert the object into a dict
list_users_of_workspace_response_dict = (
    list_users_of_workspace_response_instance.to_dict()
)
# create an instance of ListUsersOfWorkspaceResponse from a dict
list_users_of_workspace_response_from_dict = ListUsersOfWorkspaceResponse.from_dict(
    list_users_of_workspace_response_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

