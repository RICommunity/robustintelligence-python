# WorkspaceWriteMask

Mask used to specify fields of Workspace for updates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **bool** | Specifies whether to update name. | [optional] 
**agent_ids** | **bool** | Specifies whether to update list of Agent IDs. | [optional] 
**default_agent_id** | **bool** | Specifies whether to update default Agent ID. | [optional] 
**description** | **bool** | Specifies whether to update description. | [optional] 
**results_retention_in_days** | **bool** | Specifies whether to results retention in days. | [optional] 

## Example

```python
from ri.apiclient.models.workspace_write_mask import WorkspaceWriteMask

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceWriteMask from a JSON string
workspace_write_mask_instance = WorkspaceWriteMask.from_json(json)
# print the JSON string representation of the object
print(WorkspaceWriteMask.to_json())

# convert the object into a dict
workspace_write_mask_dict = workspace_write_mask_instance.to_dict()
# create an instance of WorkspaceWriteMask from a dict
workspace_write_mask_from_dict = WorkspaceWriteMask.from_dict(workspace_write_mask_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

