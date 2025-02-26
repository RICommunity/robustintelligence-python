# ListWorkspaceIntegrationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_infos** | [**List[IntegrationInfo]**](IntegrationInfo.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.list_workspace_integrations_response import ListWorkspaceIntegrationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListWorkspaceIntegrationsResponse from a JSON string
list_workspace_integrations_response_instance = ListWorkspaceIntegrationsResponse.from_json(json)
# print the JSON string representation of the object
print(ListWorkspaceIntegrationsResponse.to_json())

# convert the object into a dict
list_workspace_integrations_response_dict = list_workspace_integrations_response_instance.to_dict()
# create an instance of ListWorkspaceIntegrationsResponse from a dict
list_workspace_integrations_response_from_dict = ListWorkspaceIntegrationsResponse.from_dict(list_workspace_integrations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

