# IntegrationIntegrationVariable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**sensitivity** | [**VariableSensitivity**](VariableSensitivity.md) |  | [optional] [default to VariableSensitivity.UNSPECIFIED]
**value** | **str** | Field \&quot;value\&quot; is plaintext if the variable is not sensitive or nil if it is secret. | [optional] 

## Example

```python
from ri.apiclient.models.integration_integration_variable import (
    IntegrationIntegrationVariable,
)

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationIntegrationVariable from a JSON string
integration_integration_variable_instance = IntegrationIntegrationVariable.from_json(
    json
)
# print the JSON string representation of the object
print(IntegrationIntegrationVariable.to_json())

# convert the object into a dict
integration_integration_variable_dict = (
    integration_integration_variable_instance.to_dict()
)
# create an instance of IntegrationIntegrationVariable from a dict
integration_integration_variable_from_dict = IntegrationIntegrationVariable.from_dict(
    integration_integration_variable_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

