# ConfigureIntegrationRequestIntegrationVariable

Represents a variable for an Integration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Integration variable. | [optional] 
**value** | **str** | Value of the Integration variable. | [optional] 

## Example

```python
from ri.apiclient.models.configure_integration_request_integration_variable import ConfigureIntegrationRequestIntegrationVariable

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigureIntegrationRequestIntegrationVariable from a JSON string
configure_integration_request_integration_variable_instance = ConfigureIntegrationRequestIntegrationVariable.from_json(json)
# print the JSON string representation of the object
print(ConfigureIntegrationRequestIntegrationVariable.to_json())

# convert the object into a dict
configure_integration_request_integration_variable_dict = configure_integration_request_integration_variable_instance.to_dict()
# create an instance of ConfigureIntegrationRequestIntegrationVariable from a dict
configure_integration_request_integration_variable_from_dict = ConfigureIntegrationRequestIntegrationVariable.from_dict(configure_integration_request_integration_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

