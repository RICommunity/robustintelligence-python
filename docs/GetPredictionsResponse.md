# GetPredictionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**predictions** | [**List[DatacollectorPrediction]**](DatacollectorPrediction.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.get_predictions_response import GetPredictionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPredictionsResponse from a JSON string
get_predictions_response_instance = GetPredictionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetPredictionsResponse.to_json())

# convert the object into a dict
get_predictions_response_dict = get_predictions_response_instance.to_dict()
# create an instance of GetPredictionsResponse from a dict
get_predictions_response_from_dict = GetPredictionsResponse.from_dict(get_predictions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

