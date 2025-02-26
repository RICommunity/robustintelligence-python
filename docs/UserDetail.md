# UserDetail

Information about a user in RIME.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | [optional] 
**name** | **str** | Name of the user. | [optional] 
**role** | [**Role**](Role.md) |  | [optional] [default to Role.UNSPECIFIED]
**email** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**show_tutorial** | **bool** |  | [optional] 
**org_role** | [**ActorRole**](ActorRole.md) |  | [optional] [default to ActorRole.UNSPECIFIED]
**private_info** | [**PrivateInfo**](PrivateInfo.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.user_detail import UserDetail

# TODO update the JSON string below
json = "{}"
# create an instance of UserDetail from a JSON string
user_detail_instance = UserDetail.from_json(json)
# print the JSON string representation of the object
print(UserDetail.to_json())

# convert the object into a dict
user_detail_dict = user_detail_instance.to_dict()
# create an instance of UserDetail from a dict
user_detail_from_dict = UserDetail.from_dict(user_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

