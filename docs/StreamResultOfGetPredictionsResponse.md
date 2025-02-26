# StreamResultOfGetPredictionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**GetPredictionsResponse**](GetPredictionsResponse.md) |  | [optional] 
**error** | [**RpcStatus**](RpcStatus.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.stream_result_of_get_predictions_response import StreamResultOfGetPredictionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StreamResultOfGetPredictionsResponse from a JSON string
stream_result_of_get_predictions_response_instance = StreamResultOfGetPredictionsResponse.from_json(json)
# print the JSON string representation of the object
print(StreamResultOfGetPredictionsResponse.to_json())

# convert the object into a dict
stream_result_of_get_predictions_response_dict = stream_result_of_get_predictions_response_instance.to_dict()
# create an instance of StreamResultOfGetPredictionsResponse from a dict
stream_result_of_get_predictions_response_from_dict = StreamResultOfGetPredictionsResponse.from_dict(stream_result_of_get_predictions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

