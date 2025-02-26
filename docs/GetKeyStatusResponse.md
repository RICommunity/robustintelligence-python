# GetKeyStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**KeyStatus**](KeyStatus.md) |  | [optional] [default to KeyStatus.UNSPECIFIED]

## Example

```python
from ri.apiclient.models.get_key_status_response import GetKeyStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetKeyStatusResponse from a JSON string
get_key_status_response_instance = GetKeyStatusResponse.from_json(json)
# print the JSON string representation of the object
print(GetKeyStatusResponse.to_json())

# convert the object into a dict
get_key_status_response_dict = get_key_status_response_instance.to_dict()
# create an instance of GetKeyStatusResponse from a dict
get_key_status_response_from_dict = GetKeyStatusResponse.from_dict(get_key_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

