# ListTestCasesQuery

The resulting query is the intersection of the following constraints.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_run_id** | **str** | Uniquely specifies a Test Run associated with test cases. Specify exactly one of the page_token field or this field. | [optional] 
**test_types** | **List[str]** | Optional filter for test types. | [optional] 
**url_safe_feature_ids** | **List[str]** | Optional filter for features.  &#x60;test_types&#x60; and &#x60;url_safe_feature_ids&#x60; are applied as &#39;In&#39; filters.  Filters are not applied to empty slices. | [optional] 

## Example

```python
from ri.apiclient.models.list_test_cases_query import ListTestCasesQuery

# TODO update the JSON string below
json = "{}"
# create an instance of ListTestCasesQuery from a JSON string
list_test_cases_query_instance = ListTestCasesQuery.from_json(json)
# print the JSON string representation of the object
print(ListTestCasesQuery.to_json())

# convert the object into a dict
list_test_cases_query_dict = list_test_cases_query_instance.to_dict()
# create an instance of ListTestCasesQuery from a dict
list_test_cases_query_from_dict = ListTestCasesQuery.from_dict(list_test_cases_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

