# CreateWorkspaceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Workspace. | 
**agent_ids** | [**List[ID]**](ID.md) | List of Agent IDs to be added to the Workspace. | [optional] 
**default_agent_id** | [**ID**](ID.md) |  | [optional] 
**description** | **str** | Description of the Workspace. | [optional] 
**results_retention_in_days** | **int** |  | [optional] 

## Example

```python
from ri.apiclient.models.create_workspace_request import CreateWorkspaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWorkspaceRequest from a JSON string
create_workspace_request_instance = CreateWorkspaceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateWorkspaceRequest.to_json())

# convert the object into a dict
create_workspace_request_dict = create_workspace_request_instance.to_dict()
# create an instance of CreateWorkspaceRequest from a dict
create_workspace_request_from_dict = CreateWorkspaceRequest.from_dict(
    create_workspace_request_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

