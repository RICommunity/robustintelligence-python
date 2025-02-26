# IntegrationInfo

Represents an Integration and its configuration status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration** | [**Integration**](Integration.md) |  | [optional] 
**configured** | **bool** |  | [optional] 

## Example

```python
from ri.apiclient.models.integration_info import IntegrationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationInfo from a JSON string
integration_info_instance = IntegrationInfo.from_json(json)
# print the JSON string representation of the object
print(IntegrationInfo.to_json())

# convert the object into a dict
integration_info_dict = integration_info_instance.to_dict()
# create an instance of IntegrationInfo from a dict
integration_info_from_dict = IntegrationInfo.from_dict(integration_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

