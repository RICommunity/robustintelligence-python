# AzureConfig

Configuration for Azure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_client_id** | **str** | Azure workload Identity Client ID. | [optional] 
**azure_tenant_id** | **str** | Azure workload Identity Tenant ID. | [optional] 

## Example

```python
from ri.apiclient.models.azure_config import AzureConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AzureConfig from a JSON string
azure_config_instance = AzureConfig.from_json(json)
# print the JSON string representation of the object
print(AzureConfig.to_json())

# convert the object into a dict
azure_config_dict = azure_config_instance.to_dict()
# create an instance of AzureConfig from a dict
azure_config_from_dict = AzureConfig.from_dict(azure_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

