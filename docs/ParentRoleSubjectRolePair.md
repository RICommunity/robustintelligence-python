# ParentRoleSubjectRolePair

For users who have the specified role on the parent object, this specifies the role the user will have on the subject object (a child, such as a Project). For example, you can specify that a user with admin rights on a Workspace will get viewer rights on Projects in that Workspace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject_role** | [**ActorRole**](ActorRole.md) |  | [optional] [default to ActorRole.UNSPECIFIED]
**parent_role** | [**ActorRole**](ActorRole.md) |  | [optional] [default to ActorRole.UNSPECIFIED]

## Example

```python
from ri.apiclient.models.parent_role_subject_role_pair import ParentRoleSubjectRolePair

# TODO update the JSON string below
json = "{}"
# create an instance of ParentRoleSubjectRolePair from a JSON string
parent_role_subject_role_pair_instance = ParentRoleSubjectRolePair.from_json(json)
# print the JSON string representation of the object
print(ParentRoleSubjectRolePair.to_json())

# convert the object into a dict
parent_role_subject_role_pair_dict = parent_role_subject_role_pair_instance.to_dict()
# create an instance of ParentRoleSubjectRolePair from a dict
parent_role_subject_role_pair_from_dict = ParentRoleSubjectRolePair.from_dict(parent_role_subject_role_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

