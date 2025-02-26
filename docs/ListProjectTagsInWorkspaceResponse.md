# ListProjectTagsInWorkspaceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | [**ID**](ID.md) |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from ri.apiclient.models.list_project_tags_in_workspace_response import ListProjectTagsInWorkspaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListProjectTagsInWorkspaceResponse from a JSON string
list_project_tags_in_workspace_response_instance = ListProjectTagsInWorkspaceResponse.from_json(json)
# print the JSON string representation of the object
print(ListProjectTagsInWorkspaceResponse.to_json())

# convert the object into a dict
list_project_tags_in_workspace_response_dict = list_project_tags_in_workspace_response_instance.to_dict()
# create an instance of ListProjectTagsInWorkspaceResponse from a dict
list_project_tags_in_workspace_response_from_dict = ListProjectTagsInWorkspaceResponse.from_dict(list_project_tags_in_workspace_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

