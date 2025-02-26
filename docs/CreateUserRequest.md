# CreateUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The email address of the user. | 
**password** | **str** | The password of the user. This password will be changed on the first login. | 
**full_name** | **str** | The full name of the user. | 
**org_role** | [**ActorRole**](ActorRole.md) |  | [optional] [default to ActorRole.UNSPECIFIED]

## Example

```python
from ri.apiclient.models.create_user_request import CreateUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserRequest from a JSON string
create_user_request_instance = CreateUserRequest.from_json(json)
# print the JSON string representation of the object
print(CreateUserRequest.to_json())

# convert the object into a dict
create_user_request_dict = create_user_request_instance.to_dict()
# create an instance of CreateUserRequest from a dict
create_user_request_from_dict = CreateUserRequest.from_dict(create_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

