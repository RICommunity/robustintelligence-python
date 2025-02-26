# StorePredictionsRequestPrediction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datapoint_id** | [**ID**](ID.md) |  | 
**prediction** | **bytearray** | A JSON-encoded prediction dictionary. | 

## Example

```python
from ri.apiclient.models.store_predictions_request_prediction import (
    StorePredictionsRequestPrediction,
)

# TODO update the JSON string below
json = "{}"
# create an instance of StorePredictionsRequestPrediction from a JSON string
store_predictions_request_prediction_instance = (
    StorePredictionsRequestPrediction.from_json(json)
)
# print the JSON string representation of the object
print(StorePredictionsRequestPrediction.to_json())

# convert the object into a dict
store_predictions_request_prediction_dict = (
    store_predictions_request_prediction_instance.to_dict()
)
# create an instance of StorePredictionsRequestPrediction from a dict
store_predictions_request_prediction_from_dict = (
    StorePredictionsRequestPrediction.from_dict(
        store_predictions_request_prediction_dict
    )
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

