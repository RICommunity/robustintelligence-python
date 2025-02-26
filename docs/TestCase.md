# TestCase

TestCase returns information for a given test case.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_run_id** | **str** | Uniquely specifies a Test Run. | [optional] 
**features** | **List[str]** | The list of features used in the test case. | [optional] 
**test_batch_type** | **str** | The type of test batch. | [optional] 
**status** | [**TestCaseStatus**](TestCaseStatus.md) |  | [optional] [default to TestCaseStatus.PASS_UNSPECIFIED]
**severity** | [**RimeSeverity**](RimeSeverity.md) |  | [optional] [default to RimeSeverity.UNSPECIFIED]
**importance_score** | **float** | The model impact of the test case. | [optional] 
**test_category** | [**TestCategoryType**](TestCategoryType.md) |  | [optional] [default to TestCategoryType.UNSPECIFIED]
**category** | **str** | The string field &#x60;category&#x60; is deprecated in v2.1 and will be removed in v2.3. Please use the enum field test_category instead, which provides the same info. | [optional] 
**metrics** | [**List[TestMetric]**](TestMetric.md) |  | [optional] 
**url_safe_feature_id** | **str** | Optional URL-safe feature ID if the test case is associated with a feature. This may be empty for modalities that do not have features or test cases that pertain to two or more features, such as subset tests. | [optional] 
**test_case_id** | **str** | Together with the Test Run ID and the test batch type, this forms the primary key for the test case. | [optional] 
**display** | [**TestCaseDisplay**](TestCaseDisplay.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.test_case import TestCase

# TODO update the JSON string below
json = "{}"
# create an instance of TestCase from a JSON string
test_case_instance = TestCase.from_json(json)
# print the JSON string representation of the object
print(TestCase.to_json())

# convert the object into a dict
test_case_dict = test_case_instance.to_dict()
# create an instance of TestCase from a dict
test_case_from_dict = TestCase.from_dict(test_case_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

