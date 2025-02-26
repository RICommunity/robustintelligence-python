# ListCurrentUserRolesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | [**List[UserRole]**](UserRole.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.list_current_user_roles_response import ListCurrentUserRolesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListCurrentUserRolesResponse from a JSON string
list_current_user_roles_response_instance = ListCurrentUserRolesResponse.from_json(json)
# print the JSON string representation of the object
print(ListCurrentUserRolesResponse.to_json())

# convert the object into a dict
list_current_user_roles_response_dict = list_current_user_roles_response_instance.to_dict()
# create an instance of ListCurrentUserRolesResponse from a dict
list_current_user_roles_response_from_dict = ListCurrentUserRolesResponse.from_dict(list_current_user_roles_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

