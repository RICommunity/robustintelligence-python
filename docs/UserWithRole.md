# UserWithRole

Specifies a User ID and a corresponding Role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | [**ID**](ID.md) |  | 
**user_role** | [**ActorRole**](ActorRole.md) |  | [default to ActorRole.UNSPECIFIED]

## Example

```python
from ri.apiclient.models.user_with_role import UserWithRole

# TODO update the JSON string below
json = "{}"
# create an instance of UserWithRole from a JSON string
user_with_role_instance = UserWithRole.from_json(json)
# print the JSON string representation of the object
print(UserWithRole.to_json())

# convert the object into a dict
user_with_role_dict = user_with_role_instance.to_dict()
# create an instance of UserWithRole from a dict
user_with_role_from_dict = UserWithRole.from_dict(user_with_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

