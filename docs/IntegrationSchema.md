# IntegrationSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variables** | [**List[IntegrationIntegrationVariable]**](IntegrationIntegrationVariable.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.integration_schema import IntegrationSchema

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationSchema from a JSON string
integration_schema_instance = IntegrationSchema.from_json(json)
# print the JSON string representation of the object
print(IntegrationSchema.to_json())

# convert the object into a dict
integration_schema_dict = integration_schema_instance.to_dict()
# create an instance of IntegrationSchema from a dict
integration_schema_from_dict = IntegrationSchema.from_dict(integration_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

