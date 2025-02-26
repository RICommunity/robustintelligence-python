# TestRunDetail

TestRunDetail returns the details for a given test run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_run_id** | **str** | Uniquely specifies a Test Run. | [optional] 
**name** | **str** | The name of the Test Run. | [optional] 
**project_id** | [**ID**](ID.md) |  | [optional] 
**testing_type** | [**TestType**](TestType.md) |  | [optional] [default to TestType.STRESS_TESTING_UNSPECIFIED]
**model_task** | [**ModelTask**](ModelTask.md) |  | [optional] [default to ModelTask.UNSPECIFIED]
**ref_data_id** | **str** | Uniquely specifies a reference dataset. | [optional] 
**eval_data_id** | **str** | Uniquely specifies an evaluation dataset. | [optional] 
**model_id** | [**ID**](ID.md) |  | [optional] 
**upload_time** | **datetime** | The upload time of the test run. | [optional] 
**web_app_url** | [**SafeURL**](SafeURL.md) |  | [optional] 
**test_categories** | [**List[TestCategoryType]**](TestCategoryType.md) | The list of child references to the category tests belonging to this test run. | [optional] 
**metrics** | [**TestRunMetrics**](TestRunMetrics.md) |  | [optional] 
**status** | [**TestTaskStatus**](TestTaskStatus.md) |  | [optional] [default to TestTaskStatus.UNSPECIFIED]
**progress** | **str** | Human-readable succinct message about the progress of the test run. | [optional] 
**rime_version** | **str** | The version of Robust Intelligence that ran this test. | [optional] 
**bin_time_interval** | [**TimeInterval**](TimeInterval.md) |  | [optional] 
**ref_data_sampling_pct** | **float** | Percentage of the reference dataset used for this test. If no sampling occurred, this will be 1.0. | [optional] 
**eval_data_sampling_pct** | **float** | Percentage of the evaluation dataset used for this test. If no sampling occurred, this will be 1.0. | [optional] 
**schedule_id** | [**ID**](ID.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.test_run_detail import TestRunDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunDetail from a JSON string
test_run_detail_instance = TestRunDetail.from_json(json)
# print the JSON string representation of the object
print(TestRunDetail.to_json())

# convert the object into a dict
test_run_detail_dict = test_run_detail_instance.to_dict()
# create an instance of TestRunDetail from a dict
test_run_detail_from_dict = TestRunDetail.from_dict(test_run_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

