# GetLimitStatusResponse

GetLimitStatusResponse contains the limit status of a requested limit for a customer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit_status** | [**LimitStatus**](LimitStatus.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.get_limit_status_response import GetLimitStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLimitStatusResponse from a JSON string
get_limit_status_response_instance = GetLimitStatusResponse.from_json(json)
# print the JSON string representation of the object
print(GetLimitStatusResponse.to_json())

# convert the object into a dict
get_limit_status_response_dict = get_limit_status_response_instance.to_dict()
# create an instance of GetLimitStatusResponse from a dict
get_limit_status_response_from_dict = GetLimitStatusResponse.from_dict(get_limit_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

