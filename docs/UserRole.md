# UserRole

Represents a role to an associated subject i.e. an Admin role to a subject Project.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject_type** | [**SubjectType**](SubjectType.md) |  | [optional] [default to SubjectType.UNSPECIFIED]
**subject_id** | **str** |  | [optional] 
**role** | [**ActorRole**](ActorRole.md) |  | [optional] [default to ActorRole.UNSPECIFIED]
**implicit_grant** | **bool** |  | [optional] 

## Example

```python
from ri.apiclient.models.user_role import UserRole

# TODO update the JSON string below
json = "{}"
# create an instance of UserRole from a JSON string
user_role_instance = UserRole.from_json(json)
# print the JSON string representation of the object
print(UserRole.to_json())

# convert the object into a dict
user_role_dict = user_role_instance.to_dict()
# create an instance of UserRole from a dict
user_role_from_dict = UserRole.from_dict(user_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

