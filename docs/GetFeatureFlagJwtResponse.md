# GetFeatureFlagJwtResponse

GetFeatureFlagJwtResponse is the response to get the Feature Flag JWT token that returns the signed JWT token of the customer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signed_jwt_token_str** | **str** | The signed JWT token of the customer. | [optional] 

## Example

```python
from ri.apiclient.models.get_feature_flag_jwt_response import GetFeatureFlagJwtResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFeatureFlagJwtResponse from a JSON string
get_feature_flag_jwt_response_instance = GetFeatureFlagJwtResponse.from_json(json)
# print the JSON string representation of the object
print(GetFeatureFlagJwtResponse.to_json())

# convert the object into a dict
get_feature_flag_jwt_response_dict = get_feature_flag_jwt_response_instance.to_dict()
# create an instance of GetFeatureFlagJwtResponse from a dict
get_feature_flag_jwt_response_from_dict = GetFeatureFlagJwtResponse.from_dict(get_feature_flag_jwt_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

