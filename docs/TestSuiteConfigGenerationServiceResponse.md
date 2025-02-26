# TestSuiteConfigGenerationServiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_suite_config** | [**TestSuiteConfig**](TestSuiteConfig.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.test_suite_config_generation_service_response import TestSuiteConfigGenerationServiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TestSuiteConfigGenerationServiceResponse from a JSON string
test_suite_config_generation_service_response_instance = TestSuiteConfigGenerationServiceResponse.from_json(json)
# print the JSON string representation of the object
print(TestSuiteConfigGenerationServiceResponse.to_json())

# convert the object into a dict
test_suite_config_generation_service_response_dict = test_suite_config_generation_service_response_instance.to_dict()
# create an instance of TestSuiteConfigGenerationServiceResponse from a dict
test_suite_config_generation_service_response_from_dict = TestSuiteConfigGenerationServiceResponse.from_dict(test_suite_config_generation_service_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

