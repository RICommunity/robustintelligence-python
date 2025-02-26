# PrivateInfo

PrivateInfo holds fields which are considered private to a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**favorite_projects** | [**List[FavoriteProjects]**](FavoriteProjects.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.private_info import PrivateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateInfo from a JSON string
private_info_instance = PrivateInfo.from_json(json)
# print the JSON string representation of the object
print(PrivateInfo.to_json())

# convert the object into a dict
private_info_dict = private_info_instance.to_dict()
# create an instance of PrivateInfo from a dict
private_info_from_dict = PrivateInfo.from_dict(private_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

