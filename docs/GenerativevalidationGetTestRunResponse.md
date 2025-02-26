# GenerativevalidationGetTestRunResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_run** | [**GenerativeValidationTestRun**](GenerativeValidationTestRun.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.generativevalidation_get_test_run_response import GenerativevalidationGetTestRunResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenerativevalidationGetTestRunResponse from a JSON string
generativevalidation_get_test_run_response_instance = GenerativevalidationGetTestRunResponse.from_json(json)
# print the JSON string representation of the object
print(GenerativevalidationGetTestRunResponse.to_json())

# convert the object into a dict
generativevalidation_get_test_run_response_dict = generativevalidation_get_test_run_response_instance.to_dict()
# create an instance of GenerativevalidationGetTestRunResponse from a dict
generativevalidation_get_test_run_response_from_dict = GenerativevalidationGetTestRunResponse.from_dict(generativevalidation_get_test_run_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

