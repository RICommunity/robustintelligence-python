# ListSummaryTestsResponse

ListSummaryTestsResponse returns the list of summary tests as requested.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary_test_results** | [**List[CategoryTestResult]**](CategoryTestResult.md) | The list of summary test results. | [optional] 
**next_page_token** | **str** | A token representing the next page from the list returned by a ListSummaryTests query. | [optional] 
**has_more** | **bool** | A Boolean flag that specifies whether there are more summary tests to return. | [optional] 

## Example

```python
from ri.apiclient.models.list_summary_tests_response import ListSummaryTestsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListSummaryTestsResponse from a JSON string
list_summary_tests_response_instance = ListSummaryTestsResponse.from_json(json)
# print the JSON string representation of the object
print(ListSummaryTestsResponse.to_json())

# convert the object into a dict
list_summary_tests_response_dict = list_summary_tests_response_instance.to_dict()
# create an instance of ListSummaryTestsResponse from a dict
list_summary_tests_response_from_dict = ListSummaryTestsResponse.from_dict(list_summary_tests_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

