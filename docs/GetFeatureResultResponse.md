# GetFeatureResultResponse

GetFeatureResultResponse returns the feature result as requested.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_result** | [**TestFeatureResult**](TestFeatureResult.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.get_feature_result_response import GetFeatureResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFeatureResultResponse from a JSON string
get_feature_result_response_instance = GetFeatureResultResponse.from_json(json)
# print the JSON string representation of the object
print(GetFeatureResultResponse.to_json())

# convert the object into a dict
get_feature_result_response_dict = get_feature_result_response_instance.to_dict()
# create an instance of GetFeatureResultResponse from a dict
get_feature_result_response_from_dict = GetFeatureResultResponse.from_dict(get_feature_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

