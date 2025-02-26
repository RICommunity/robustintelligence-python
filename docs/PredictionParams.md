# PredictionParams

PredictionParams specifies how to make predictions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pred_col** | **str** | Column used for predictions. | [optional] 
**timestamp_col** | **str** | Column used for CT timestamp. | [optional] 
**experimental_fields** | **Dict[str, object]** | Fields that enable experimental functionality.  WARNING: these fields are experimental; ie, their functionality may not be reliable or backwards-compatible. Do not use these fields in production. | [optional] 

## Example

```python
from ri.apiclient.models.prediction_params import PredictionParams

# TODO update the JSON string below
json = "{}"
# create an instance of PredictionParams from a JSON string
prediction_params_instance = PredictionParams.from_json(json)
# print the JSON string representation of the object
print(PredictionParams.to_json())

# convert the object into a dict
prediction_params_dict = prediction_params_instance.to_dict()
# create an instance of PredictionParams from a dict
prediction_params_from_dict = PredictionParams.from_dict(prediction_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

