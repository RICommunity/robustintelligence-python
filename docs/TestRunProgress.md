# TestRunProgress

TestRunProgress is a shared message for representing the progress of a single test run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_run_id** | **str** |  | [optional] 
**status** | [**TestTaskStatus**](TestTaskStatus.md) |  | [optional] [default to TestTaskStatus.UNSPECIFIED]
**test_batches** | [**List[TestBatchProgress]**](TestBatchProgress.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.test_run_progress import TestRunProgress

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunProgress from a JSON string
test_run_progress_instance = TestRunProgress.from_json(json)
# print the JSON string representation of the object
print(TestRunProgress.to_json())

# convert the object into a dict
test_run_progress_dict = test_run_progress_instance.to_dict()
# create an instance of TestRunProgress from a dict
test_run_progress_from_dict = TestRunProgress.from_dict(test_run_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

