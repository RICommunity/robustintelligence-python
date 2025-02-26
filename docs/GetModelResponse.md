# GetModelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | [**ModelWithOwnerDetails**](ModelWithOwnerDetails.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.get_model_response import GetModelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetModelResponse from a JSON string
get_model_response_instance = GetModelResponse.from_json(json)
# print the JSON string representation of the object
print(GetModelResponse.to_json())

# convert the object into a dict
get_model_response_dict = get_model_response_instance.to_dict()
# create an instance of GetModelResponse from a dict
get_model_response_from_dict = GetModelResponse.from_dict(get_model_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

