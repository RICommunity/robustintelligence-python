# UpdateIntegrationRequestIntegration

Integration object in RIME.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Unique ID of an object in RIME. | [optional] 
**workspace_id** | [**ID**](ID.md) |  | [optional] 
**creation_time** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | [**IntegrationType**](IntegrationType.md) |  | [optional] [default to IntegrationType.UNSPECIFIED]
**var_schema** | [**IntegrationSchema**](IntegrationSchema.md) |  | [optional] 
**level** | [**IntegrationLevel**](IntegrationLevel.md) |  | [optional] [default to IntegrationLevel.UNSPECIFIED]

## Example

```python
from ri.apiclient.models.update_integration_request_integration import UpdateIntegrationRequestIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIntegrationRequestIntegration from a JSON string
update_integration_request_integration_instance = UpdateIntegrationRequestIntegration.from_json(json)
# print the JSON string representation of the object
print(UpdateIntegrationRequestIntegration.to_json())

# convert the object into a dict
update_integration_request_integration_dict = update_integration_request_integration_instance.to_dict()
# create an instance of UpdateIntegrationRequestIntegration from a dict
update_integration_request_integration_from_dict = UpdateIntegrationRequestIntegration.from_dict(update_integration_request_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

