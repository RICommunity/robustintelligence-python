# UpdateIntegrationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_info** | [**IntegrationInfo**](IntegrationInfo.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.update_integration_response import UpdateIntegrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIntegrationResponse from a JSON string
update_integration_response_instance = UpdateIntegrationResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateIntegrationResponse.to_json())

# convert the object into a dict
update_integration_response_dict = update_integration_response_instance.to_dict()
# create an instance of UpdateIntegrationResponse from a dict
update_integration_response_from_dict = UpdateIntegrationResponse.from_dict(update_integration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

