# ListWorkspacesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspaces** | [**List[Workspace]**](Workspace.md) |  | [optional] 
**next_page_token** | **str** |  | [optional] 
**has_more** | **bool** |  | [optional] 

## Example

```python
from ri.apiclient.models.list_workspaces_response import ListWorkspacesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListWorkspacesResponse from a JSON string
list_workspaces_response_instance = ListWorkspacesResponse.from_json(json)
# print the JSON string representation of the object
print(ListWorkspacesResponse.to_json())

# convert the object into a dict
list_workspaces_response_dict = list_workspaces_response_instance.to_dict()
# create an instance of ListWorkspacesResponse from a dict
list_workspaces_response_from_dict = ListWorkspacesResponse.from_dict(
    list_workspaces_response_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

