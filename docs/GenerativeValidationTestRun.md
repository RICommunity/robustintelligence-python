# GenerativeValidationTestRun

GenerativeValidationTestRun are the details about a generative validation test run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | [optional] 
**name** | **str** | A name of the test run. | [optional] 
**workspace_id** | [**ID**](ID.md) |  | [optional] 
**config** | [**GenerativeValidationConfig**](GenerativeValidationConfig.md) |  | [optional] 
**job_info** | [**JobInfo**](JobInfo.md) |  | [optional] 
**total_attacks** | **int** | Total attacks run during the test. | [optional] 
**successful_attacks** | **int** | The number of successful attacks on the model. | [optional] 
**attempted_attacks** | **int** | The number of attacks attempted. | [optional] 

## Example

```python
from ri.apiclient.models.generative_validation_test_run import GenerativeValidationTestRun

# TODO update the JSON string below
json = "{}"
# create an instance of GenerativeValidationTestRun from a JSON string
generative_validation_test_run_instance = GenerativeValidationTestRun.from_json(json)
# print the JSON string representation of the object
print(GenerativeValidationTestRun.to_json())

# convert the object into a dict
generative_validation_test_run_dict = generative_validation_test_run_instance.to_dict()
# create an instance of GenerativeValidationTestRun from a dict
generative_validation_test_run_from_dict = GenerativeValidationTestRun.from_dict(generative_validation_test_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

