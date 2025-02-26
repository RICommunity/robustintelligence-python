# UserDetailWithRole

Specifies a User object and a corresponding Role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_detail** | [**UserDetail**](UserDetail.md) |  | 
**user_role** | [**ActorRole**](ActorRole.md) |  | [default to ActorRole.UNSPECIFIED]
**implicit_grant** | **bool** |  | [optional] 

## Example

```python
from ri.apiclient.models.user_detail_with_role import UserDetailWithRole

# TODO update the JSON string below
json = "{}"
# create an instance of UserDetailWithRole from a JSON string
user_detail_with_role_instance = UserDetailWithRole.from_json(json)
# print the JSON string representation of the object
print(UserDetailWithRole.to_json())

# convert the object into a dict
user_detail_with_role_dict = user_detail_with_role_instance.to_dict()
# create an instance of UserDetailWithRole from a dict
user_detail_with_role_from_dict = UserDetailWithRole.from_dict(user_detail_with_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

