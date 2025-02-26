# FlaggedDatapoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_id** | **str** |  | [optional] 
**row_timestamp** | **datetime** |  | [optional] 

## Example

```python
from ri.apiclient.models.flagged_datapoint import FlaggedDatapoint

# TODO update the JSON string below
json = "{}"
# create an instance of FlaggedDatapoint from a JSON string
flagged_datapoint_instance = FlaggedDatapoint.from_json(json)
# print the JSON string representation of the object
print(FlaggedDatapoint.to_json())

# convert the object into a dict
flagged_datapoint_dict = flagged_datapoint_instance.to_dict()
# create an instance of FlaggedDatapoint from a dict
flagged_datapoint_from_dict = FlaggedDatapoint.from_dict(flagged_datapoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

