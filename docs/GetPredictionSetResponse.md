# GetPredictionSetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prediction** | [**PredictionPrediction**](PredictionPrediction.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.get_prediction_set_response import GetPredictionSetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPredictionSetResponse from a JSON string
get_prediction_set_response_instance = GetPredictionSetResponse.from_json(json)
# print the JSON string representation of the object
print(GetPredictionSetResponse.to_json())

# convert the object into a dict
get_prediction_set_response_dict = get_prediction_set_response_instance.to_dict()
# create an instance of GetPredictionSetResponse from a dict
get_prediction_set_response_from_dict = GetPredictionSetResponse.from_dict(get_prediction_set_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

