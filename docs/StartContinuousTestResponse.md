# StartContinuousTestResponse

StartContinuousTestResponse is the response object returned from StartContinuousTest that contains the job info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | [**JobMetadata**](JobMetadata.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.start_continuous_test_response import StartContinuousTestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StartContinuousTestResponse from a JSON string
start_continuous_test_response_instance = StartContinuousTestResponse.from_json(json)
# print the JSON string representation of the object
print(StartContinuousTestResponse.to_json())

# convert the object into a dict
start_continuous_test_response_dict = start_continuous_test_response_instance.to_dict()
# create an instance of StartContinuousTestResponse from a dict
start_continuous_test_response_from_dict = StartContinuousTestResponse.from_dict(start_continuous_test_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

