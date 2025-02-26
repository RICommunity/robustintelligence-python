# ScheduledCTParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eval_data_integration_id** | [**ID**](ID.md) |  | [optional] 
**eval_data_info** | [**DataInfo**](DataInfo.md) |  | 
**eval_pred_integration_id** | [**ID**](ID.md) |  | [optional] 
**eval_pred_info** | [**PredInfo**](PredInfo.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.scheduled_ct_parameters import ScheduledCTParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledCTParameters from a JSON string
scheduled_ct_parameters_instance = ScheduledCTParameters.from_json(json)
# print the JSON string representation of the object
print(ScheduledCTParameters.to_json())

# convert the object into a dict
scheduled_ct_parameters_dict = scheduled_ct_parameters_instance.to_dict()
# create an instance of ScheduledCTParameters from a dict
scheduled_ct_parameters_from_dict = ScheduledCTParameters.from_dict(
    scheduled_ct_parameters_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

