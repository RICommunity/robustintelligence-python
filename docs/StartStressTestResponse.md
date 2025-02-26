# StartStressTestResponse

StartStressTestResponse is a response object returned from the StartStressTest call that contains the job information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | [**JobMetadata**](JobMetadata.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.start_stress_test_response import StartStressTestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StartStressTestResponse from a JSON string
start_stress_test_response_instance = StartStressTestResponse.from_json(json)
# print the JSON string representation of the object
print(StartStressTestResponse.to_json())

# convert the object into a dict
start_stress_test_response_dict = start_stress_test_response_instance.to_dict()
# create an instance of StartStressTestResponse from a dict
start_stress_test_response_from_dict = StartStressTestResponse.from_dict(start_stress_test_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

