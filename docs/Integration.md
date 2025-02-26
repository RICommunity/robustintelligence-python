# Integration

Integration object in RIME.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | [optional] 
**workspace_id** | [**ID**](ID.md) |  | [optional] 
**creation_time** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | [**IntegrationType**](IntegrationType.md) |  | [optional] [default to IntegrationType.UNSPECIFIED]
**var_schema** | [**IntegrationSchema**](IntegrationSchema.md) |  | [optional] 
**level** | [**IntegrationLevel**](IntegrationLevel.md) |  | [optional] [default to IntegrationLevel.UNSPECIFIED]

## Example

```python
from ri.apiclient.models.integration import Integration

# TODO update the JSON string below
json = "{}"
# create an instance of Integration from a JSON string
integration_instance = Integration.from_json(json)
# print the JSON string representation of the object
print(Integration.to_json())

# convert the object into a dict
integration_dict = integration_instance.to_dict()
# create an instance of Integration from a dict
integration_from_dict = Integration.from_dict(integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

