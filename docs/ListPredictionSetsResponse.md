# ListPredictionSetsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**predictions** | [**List[PredictionPrediction]**](PredictionPrediction.md) |  | [optional] 
**next_page_token** | **str** |  | [optional] 
**has_more** | **bool** |  | [optional] 

## Example

```python
from ri.apiclient.models.list_prediction_sets_response import ListPredictionSetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListPredictionSetsResponse from a JSON string
list_prediction_sets_response_instance = ListPredictionSetsResponse.from_json(json)
# print the JSON string representation of the object
print(ListPredictionSetsResponse.to_json())

# convert the object into a dict
list_prediction_sets_response_dict = list_prediction_sets_response_instance.to_dict()
# create an instance of ListPredictionSetsResponse from a dict
list_prediction_sets_response_from_dict = ListPredictionSetsResponse.from_dict(list_prediction_sets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

