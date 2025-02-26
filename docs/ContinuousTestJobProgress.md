# ContinuousTestJobProgress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_runs** | [**List[ContinuousTestRunProgress]**](ContinuousTestRunProgress.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.continuous_test_job_progress import ContinuousTestJobProgress

# TODO update the JSON string below
json = "{}"
# create an instance of ContinuousTestJobProgress from a JSON string
continuous_test_job_progress_instance = ContinuousTestJobProgress.from_json(json)
# print the JSON string representation of the object
print(ContinuousTestJobProgress.to_json())

# convert the object into a dict
continuous_test_job_progress_dict = continuous_test_job_progress_instance.to_dict()
# create an instance of ContinuousTestJobProgress from a dict
continuous_test_job_progress_from_dict = ContinuousTestJobProgress.from_dict(continuous_test_job_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

