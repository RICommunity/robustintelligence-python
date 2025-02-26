# SecurityEventDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**SecurityEventType**](SecurityEventType.md) |  | [optional] [default to SecurityEventType.UNSPECIFIED]
**effect_on_model** | **List[str]** |  | [optional] 
**possible_intent** | **List[str]** |  | [optional] 
**evidence** | **List[str]** |  | [optional] 
**recommendations** | **List[str]** |  | [optional] 
**datapoints** | [**List[FlaggedDatapoint]**](FlaggedDatapoint.md) | Include descriptions of all the flagged datapoints for the attack. | [optional] 

## Example

```python
from ri.apiclient.models.security_event_details import SecurityEventDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityEventDetails from a JSON string
security_event_details_instance = SecurityEventDetails.from_json(json)
# print the JSON string representation of the object
print(SecurityEventDetails.to_json())

# convert the object into a dict
security_event_details_dict = security_event_details_instance.to_dict()
# create an instance of SecurityEventDetails from a dict
security_event_details_from_dict = SecurityEventDetails.from_dict(
    security_event_details_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

