# DatacollectorPrediction

Prediction contains the prediction of a model for a datapoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datapoint_id** | [**ID**](ID.md) |  | [optional] 
**model_id** | [**ID**](ID.md) |  | [optional] 
**data_stream_id** | [**ID**](ID.md) |  | [optional] 
**prediction** | **bytearray** |  | [optional] 
**timestamp** | **datetime** | The timestamp of the datapoint is stored in the prediction for fast querying. | [optional] 

## Example

```python
from ri.apiclient.models.datacollector_prediction import DatacollectorPrediction

# TODO update the JSON string below
json = "{}"
# create an instance of DatacollectorPrediction from a JSON string
datacollector_prediction_instance = DatacollectorPrediction.from_json(json)
# print the JSON string representation of the object
print(DatacollectorPrediction.to_json())

# convert the object into a dict
datacollector_prediction_dict = datacollector_prediction_instance.to_dict()
# create an instance of DatacollectorPrediction from a dict
datacollector_prediction_from_dict = DatacollectorPrediction.from_dict(datacollector_prediction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

