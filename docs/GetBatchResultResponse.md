# GetBatchResultResponse

GetBatchResultResponse returns the batch result for a test run as requested.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_batch** | [**TestrunresultTestBatchResult**](TestrunresultTestBatchResult.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.get_batch_result_response import GetBatchResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBatchResultResponse from a JSON string
get_batch_result_response_instance = GetBatchResultResponse.from_json(json)
# print the JSON string representation of the object
print(GetBatchResultResponse.to_json())

# convert the object into a dict
get_batch_result_response_dict = get_batch_result_response_instance.to_dict()
# create an instance of GetBatchResultResponse from a dict
get_batch_result_response_from_dict = GetBatchResultResponse.from_dict(get_batch_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

