# CreateIntegrationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_info** | [**IntegrationInfo**](IntegrationInfo.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.create_integration_response import CreateIntegrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIntegrationResponse from a JSON string
create_integration_response_instance = CreateIntegrationResponse.from_json(json)
# print the JSON string representation of the object
print(CreateIntegrationResponse.to_json())

# convert the object into a dict
create_integration_response_dict = create_integration_response_instance.to_dict()
# create an instance of CreateIntegrationResponse from a dict
create_integration_response_from_dict = CreateIntegrationResponse.from_dict(
    create_integration_response_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

