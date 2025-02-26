# TestBatchProgress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | (test run ID, test batch type) are a unique ID of the test batch. | [optional] 
**status** | [**TestTaskStatus**](TestTaskStatus.md) |  | [optional] [default to TestTaskStatus.UNSPECIFIED]

## Example

```python
from ri.apiclient.models.test_batch_progress import TestBatchProgress

# TODO update the JSON string below
json = "{}"
# create an instance of TestBatchProgress from a JSON string
test_batch_progress_instance = TestBatchProgress.from_json(json)
# print the JSON string representation of the object
print(TestBatchProgress.to_json())

# convert the object into a dict
test_batch_progress_dict = test_batch_progress_instance.to_dict()
# create an instance of TestBatchProgress from a dict
test_batch_progress_from_dict = TestBatchProgress.from_dict(test_batch_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

