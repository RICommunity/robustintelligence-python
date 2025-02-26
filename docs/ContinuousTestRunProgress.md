# ContinuousTestRunProgress

ContinuousTestRunProgress is a wrapper around TestRunProgress with added metadata about the bins.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_run** | [**TestRunProgress**](TestRunProgress.md) |  | [optional] 
**bin_start_time** | **datetime** |  | [optional] 
**bin_end_time** | **datetime** |  | [optional] 

## Example

```python
from ri.apiclient.models.continuous_test_run_progress import ContinuousTestRunProgress

# TODO update the JSON string below
json = "{}"
# create an instance of ContinuousTestRunProgress from a JSON string
continuous_test_run_progress_instance = ContinuousTestRunProgress.from_json(json)
# print the JSON string representation of the object
print(ContinuousTestRunProgress.to_json())

# convert the object into a dict
continuous_test_run_progress_dict = continuous_test_run_progress_instance.to_dict()
# create an instance of ContinuousTestRunProgress from a dict
continuous_test_run_progress_from_dict = ContinuousTestRunProgress.from_dict(continuous_test_run_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

