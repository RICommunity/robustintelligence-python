# RegisterDataStreamResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_stream_id** | [**ID**](ID.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.register_data_stream_response import RegisterDataStreamResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterDataStreamResponse from a JSON string
register_data_stream_response_instance = RegisterDataStreamResponse.from_json(json)
# print the JSON string representation of the object
print(RegisterDataStreamResponse.to_json())

# convert the object into a dict
register_data_stream_response_dict = register_data_stream_response_instance.to_dict()
# create an instance of RegisterDataStreamResponse from a dict
register_data_stream_response_from_dict = RegisterDataStreamResponse.from_dict(register_data_stream_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

