# GetIntegrationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_info** | [**IntegrationInfo**](IntegrationInfo.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.get_integration_response import GetIntegrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetIntegrationResponse from a JSON string
get_integration_response_instance = GetIntegrationResponse.from_json(json)
# print the JSON string representation of the object
print(GetIntegrationResponse.to_json())

# convert the object into a dict
get_integration_response_dict = get_integration_response_instance.to_dict()
# create an instance of GetIntegrationResponse from a dict
get_integration_response_from_dict = GetIntegrationResponse.from_dict(get_integration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

