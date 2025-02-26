# PredInfo

PredInfo specifies the information needed for a prediction set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_info** | [**ConnectionInfo**](ConnectionInfo.md) |  | 
**pred_params** | [**PredictionParams**](PredictionParams.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.pred_info import PredInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PredInfo from a JSON string
pred_info_instance = PredInfo.from_json(json)
# print the JSON string representation of the object
print(PredInfo.to_json())

# convert the object into a dict
pred_info_dict = pred_info_instance.to_dict()
# create an instance of PredInfo from a dict
pred_info_from_dict = PredInfo.from_dict(pred_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

