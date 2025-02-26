# StressTestJobProgress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_run** | [**TestRunProgress**](TestRunProgress.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.stress_test_job_progress import StressTestJobProgress

# TODO update the JSON string below
json = "{}"
# create an instance of StressTestJobProgress from a JSON string
stress_test_job_progress_instance = StressTestJobProgress.from_json(json)
# print the JSON string representation of the object
print(StressTestJobProgress.to_json())

# convert the object into a dict
stress_test_job_progress_dict = stress_test_job_progress_instance.to_dict()
# create an instance of StressTestJobProgress from a dict
stress_test_job_progress_from_dict = StressTestJobProgress.from_dict(stress_test_job_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

