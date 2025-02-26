# ListFeatureResultsResponse

ListFeatureResultsResponse returns a list of feature results as requested.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_results** | [**List[TestFeatureResult]**](TestFeatureResult.md) | The list of feature results. | [optional] 
**next_page_token** | **str** | A token representing the next page from the list returned by a ListFeatureResults query. | [optional] 
**has_more** | **bool** | A Boolean flag that specifies whether there are more feature results to return. | [optional] 

## Example

```python
from ri.apiclient.models.list_feature_results_response import ListFeatureResultsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListFeatureResultsResponse from a JSON string
list_feature_results_response_instance = ListFeatureResultsResponse.from_json(json)
# print the JSON string representation of the object
print(ListFeatureResultsResponse.to_json())

# convert the object into a dict
list_feature_results_response_dict = list_feature_results_response_instance.to_dict()
# create an instance of ListFeatureResultsResponse from a dict
list_feature_results_response_from_dict = ListFeatureResultsResponse.from_dict(list_feature_results_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

