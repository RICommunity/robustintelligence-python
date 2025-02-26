# PredictionPrediction

Prediction represents a full entry in the Predictions Registry, with info, metadata, and tags used to identify the predictions both internally and to an external user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | **str** | The dataset_id and model_id are used to uniquely identify a prediction. These must be provided by the user. | [optional] 
**model_id** | [**ID**](ID.md) |  | [optional] 
**project_ids** | [**List[ID]**](ID.md) | For now, a pred will only have one project_id associated with it. We make this an array to allow pred&#39;s to be shared in the future. | [optional] 
**creator_id** | [**ID**](ID.md) |  | [optional] 
**creation_time** | **datetime** |  | [optional] 
**user_metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**integration_id** | [**ID**](ID.md) |  | [optional] 
**pred_info** | [**PredInfo**](PredInfo.md) |  | [optional] 
**validity_status** | [**ValidityStatus**](ValidityStatus.md) |  | [optional] [default to ValidityStatus.UNSPECIFIED]
**marked_for_delete_at** | **datetime** | If marked_for_delete_at is set, the document will be deleted after a TTL. | [optional] 
**validity_status_message** | **str** | Information about the validity status of the predictions, such as why it is invalid. A Case where this would be populated is when the ValidityStatus is not explicitly set to valid by the XP validation task and additional details are required to convey to the user why the predictions are not valid. | [optional] 

## Example

```python
from ri.apiclient.models.prediction_prediction import PredictionPrediction

# TODO update the JSON string below
json = "{}"
# create an instance of PredictionPrediction from a JSON string
prediction_prediction_instance = PredictionPrediction.from_json(json)
# print the JSON string representation of the object
print(PredictionPrediction.to_json())

# convert the object into a dict
prediction_prediction_dict = prediction_prediction_instance.to_dict()
# create an instance of PredictionPrediction from a dict
prediction_prediction_from_dict = PredictionPrediction.from_dict(prediction_prediction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

