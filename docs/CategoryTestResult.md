# CategoryTestResult

CategoryTestResult is a summary of a single category of tests in Robust Intelligence. For instance, the \"Drift\" category includes specific tests such as Prediction Drift or Label Drift. The CategoryTestResult for Drift includes an overall severity and other details aggregated across those individual tests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | When combined with the test run ID, this uniquely identifies a category test result. | [optional] 
**severity** | [**RimeSeverity**](RimeSeverity.md) |  | [optional] [default to RimeSeverity.UNSPECIFIED]
**suggestion** | [**Suggestion**](Suggestion.md) |  | [optional] 
**category_metrics** | [**List[CategoryMetric]**](CategoryMetric.md) | Category metrics are aggregated or important metrics for the category. | [optional] 
**test_batch_types** | **List[str]** | List of the tests in the category. | [optional] 
**description** | **str** | Human-readable description of the category test result. | [optional] 
**severity_counts** | [**SeverityCounts**](SeverityCounts.md) |  | [optional] 
**failing_test_types** | **List[str]** | List of all the failing test types. | [optional] 
**duration** | **float** | Duration is the total time in seconds for tests in that category. | [optional] 
**category_importance** | **float** | The relative importance of the category. | [optional] 
**risk_category** | [**RiskCategoryType**](RiskCategoryType.md) |  | [optional] [default to RiskCategoryType.UNSPECIFIED]
**test_category** | [**TestCategoryType**](TestCategoryType.md) |  | [optional] [default to TestCategoryType.UNSPECIFIED]

## Example

```python
from ri.apiclient.models.category_test_result import CategoryTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryTestResult from a JSON string
category_test_result_instance = CategoryTestResult.from_json(json)
# print the JSON string representation of the object
print(CategoryTestResult.to_json())

# convert the object into a dict
category_test_result_dict = category_test_result_instance.to_dict()
# create an instance of CategoryTestResult from a dict
category_test_result_from_dict = CategoryTestResult.from_dict(category_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

