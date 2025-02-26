# StressTest

A stress test job runs a single test run over a model and dataset. This is also known as offline testing; it is run before production deployment of the model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | [**ID**](ID.md) |  | [optional] 
**test_run_id** | **str** |  | [optional] 
**progress** | [**StressTestJobProgress**](StressTestJobProgress.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.stress_test import StressTest

# TODO update the JSON string below
json = "{}"
# create an instance of StressTest from a JSON string
stress_test_instance = StressTest.from_json(json)
# print the JSON string representation of the object
print(StressTest.to_json())

# convert the object into a dict
stress_test_dict = stress_test_instance.to_dict()
# create an instance of StressTest from a dict
stress_test_from_dict = StressTest.from_dict(stress_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

