# GetCategoryResultsResponse

GetCategoryResultsResponse returns the list of summary tests as requested.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_test_results** | [**List[CategoryTestResult]**](CategoryTestResult.md) | The list of summary test results. | [optional] 

## Example

```python
from ri.apiclient.models.get_category_results_response import GetCategoryResultsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCategoryResultsResponse from a JSON string
get_category_results_response_instance = GetCategoryResultsResponse.from_json(json)
# print the JSON string representation of the object
print(GetCategoryResultsResponse.to_json())

# convert the object into a dict
get_category_results_response_dict = get_category_results_response_instance.to_dict()
# create an instance of GetCategoryResultsResponse from a dict
get_category_results_response_from_dict = GetCategoryResultsResponse.from_dict(
    get_category_results_response_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

