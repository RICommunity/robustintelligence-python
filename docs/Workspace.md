# Workspace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Workspace. | [optional] 
**agent_ids** | [**List[ID]**](ID.md) | List of Agent IDs that can be used by the Workspace. | [optional] 
**default_agent_id** | [**ID**](ID.md) |  | [optional] 
**workspace_id** | [**ID**](ID.md) |  | [optional] 
**description** | **str** | Description of the Workspace. | [optional] 
**results_retention_in_days** | **int** |  | [optional] 

## Example

```python
from ri.apiclient.models.workspace import Workspace

# TODO update the JSON string below
json = "{}"
# create an instance of Workspace from a JSON string
workspace_instance = Workspace.from_json(json)
# print the JSON string representation of the object
print(Workspace.to_json())

# convert the object into a dict
workspace_dict = workspace_instance.to_dict()
# create an instance of Workspace from a dict
workspace_from_dict = Workspace.from_dict(workspace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

