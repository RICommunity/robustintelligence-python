# StreamResultOfGetDatapointsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**GetDatapointsResponse**](GetDatapointsResponse.md) |  | [optional] 
**error** | [**RpcStatus**](RpcStatus.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.stream_result_of_get_datapoints_response import (
    StreamResultOfGetDatapointsResponse,
)

# TODO update the JSON string below
json = "{}"
# create an instance of StreamResultOfGetDatapointsResponse from a JSON string
stream_result_of_get_datapoints_response_instance = (
    StreamResultOfGetDatapointsResponse.from_json(json)
)
# print the JSON string representation of the object
print(StreamResultOfGetDatapointsResponse.to_json())

# convert the object into a dict
stream_result_of_get_datapoints_response_dict = (
    stream_result_of_get_datapoints_response_instance.to_dict()
)
# create an instance of StreamResultOfGetDatapointsResponse from a dict
stream_result_of_get_datapoints_response_from_dict = (
    StreamResultOfGetDatapointsResponse.from_dict(
        stream_result_of_get_datapoints_response_dict
    )
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

