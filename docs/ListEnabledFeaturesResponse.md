# ListEnabledFeaturesResponse

ListEnabledFeaturesResponse contains all enabled features for a customer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_name** | **str** | Tthe customer to retrieve feature flags for. | [optional] 
**enabled_features** | [**List[LicenseFeature]**](LicenseFeature.md) | The set of enabled features. | [optional] 

## Example

```python
from ri.apiclient.models.list_enabled_features_response import ListEnabledFeaturesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListEnabledFeaturesResponse from a JSON string
list_enabled_features_response_instance = ListEnabledFeaturesResponse.from_json(json)
# print the JSON string representation of the object
print(ListEnabledFeaturesResponse.to_json())

# convert the object into a dict
list_enabled_features_response_dict = list_enabled_features_response_instance.to_dict()
# create an instance of ListEnabledFeaturesResponse from a dict
list_enabled_features_response_from_dict = ListEnabledFeaturesResponse.from_dict(list_enabled_features_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

