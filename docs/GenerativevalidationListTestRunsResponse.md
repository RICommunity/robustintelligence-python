# GenerativevalidationListTestRunsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_runs** | [**List[GenerativeValidationTestRun]**](GenerativeValidationTestRun.md) | The list of generative testing results. | [optional] 
**next_page_token** | **str** | A token representing the next page from the list returned by a query. | [optional] 
**has_more** | **bool** | A Boolean flag that specifies whether there are more results to return. | [optional] 

## Example

```python
from ri.apiclient.models.generativevalidation_list_test_runs_response import GenerativevalidationListTestRunsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenerativevalidationListTestRunsResponse from a JSON string
generativevalidation_list_test_runs_response_instance = GenerativevalidationListTestRunsResponse.from_json(json)
# print the JSON string representation of the object
print(GenerativevalidationListTestRunsResponse.to_json())

# convert the object into a dict
generativevalidation_list_test_runs_response_dict = generativevalidation_list_test_runs_response_instance.to_dict()
# create an instance of GenerativevalidationListTestRunsResponse from a dict
generativevalidation_list_test_runs_response_from_dict = GenerativevalidationListTestRunsResponse.from_dict(generativevalidation_list_test_runs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

