# GetURLResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | [**SafeURL**](SafeURL.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.get_url_response import GetURLResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetURLResponse from a JSON string
get_url_response_instance = GetURLResponse.from_json(json)
# print the JSON string representation of the object
print(GetURLResponse.to_json())

# convert the object into a dict
get_url_response_dict = get_url_response_instance.to_dict()
# create an instance of GetURLResponse from a dict
get_url_response_from_dict = GetURLResponse.from_dict(get_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

