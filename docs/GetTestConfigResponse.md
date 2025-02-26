# GetTestConfigResponse

GetTestConfigResponse returns the test config as requested.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotated_test_config** | [**AnnotatedTestConfig**](AnnotatedTestConfig.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.get_test_config_response import GetTestConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTestConfigResponse from a JSON string
get_test_config_response_instance = GetTestConfigResponse.from_json(json)
# print the JSON string representation of the object
print(GetTestConfigResponse.to_json())

# convert the object into a dict
get_test_config_response_dict = get_test_config_response_instance.to_dict()
# create an instance of GetTestConfigResponse from a dict
get_test_config_response_from_dict = GetTestConfigResponse.from_dict(get_test_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

