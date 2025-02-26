# TestRunIncrementalConfig

TestRunIncrementalConfig contains the configuration necessary to run a Continuous Test.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eval_dataset_id** | **str** | Uniquely specifies an evaluation Dataset. | [optional] 
**run_time_info** | [**RunTimeInfo**](RunTimeInfo.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.test_run_incremental_config import TestRunIncrementalConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunIncrementalConfig from a JSON string
test_run_incremental_config_instance = TestRunIncrementalConfig.from_json(json)
# print the JSON string representation of the object
print(TestRunIncrementalConfig.to_json())

# convert the object into a dict
test_run_incremental_config_dict = test_run_incremental_config_instance.to_dict()
# create an instance of TestRunIncrementalConfig from a dict
test_run_incremental_config_from_dict = TestRunIncrementalConfig.from_dict(test_run_incremental_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

