# PredictionQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | **str** | Uniquely specifies a Model. | [optional] 
**dataset_id** | **str** | Uniquely specifies a Dataset. | [optional] 

## Example

```python
from ri.apiclient.models.prediction_query import PredictionQuery

# TODO update the JSON string below
json = "{}"
# create an instance of PredictionQuery from a JSON string
prediction_query_instance = PredictionQuery.from_json(json)
# print the JSON string representation of the object
print(PredictionQuery.to_json())

# convert the object into a dict
prediction_query_dict = prediction_query_instance.to_dict()
# create an instance of PredictionQuery from a dict
prediction_query_from_dict = PredictionQuery.from_dict(prediction_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

