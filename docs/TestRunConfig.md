# TestRunConfig

TestRunConfig contains the configuration necessary to run a Stress Test. model_id and data_info are required fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_name** | **str** | Name for this Test Run. | 
**model_id** | [**ID**](ID.md) |  | 
**data_info** | [**RefEvalDatasets**](RefEvalDatasets.md) |  | 
**run_time_info** | [**RunTimeInfo**](RunTimeInfo.md) |  | [optional] 
**profiling_config** | [**ProfilingConfig**](ProfilingConfig.md) |  | [optional] 
**test_suite_config** | [**TestSuiteConfig**](TestSuiteConfig.md) |  | [optional] 
**categories** | [**List[TestCategoryType]**](TestCategoryType.md) | List of test categories to be run. | [optional] 

## Example

```python
from ri.apiclient.models.test_run_config import TestRunConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunConfig from a JSON string
test_run_config_instance = TestRunConfig.from_json(json)
# print the JSON string representation of the object
print(TestRunConfig.to_json())

# convert the object into a dict
test_run_config_dict = test_run_config_instance.to_dict()
# create an instance of TestRunConfig from a dict
test_run_config_from_dict = TestRunConfig.from_dict(test_run_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

