# ConfigureIntegrationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_info** | [**IntegrationInfo**](IntegrationInfo.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.configure_integration_response import ConfigureIntegrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigureIntegrationResponse from a JSON string
configure_integration_response_instance = ConfigureIntegrationResponse.from_json(json)
# print the JSON string representation of the object
print(ConfigureIntegrationResponse.to_json())

# convert the object into a dict
configure_integration_response_dict = configure_integration_response_instance.to_dict()
# create an instance of ConfigureIntegrationResponse from a dict
configure_integration_response_from_dict = ConfigureIntegrationResponse.from_dict(configure_integration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

