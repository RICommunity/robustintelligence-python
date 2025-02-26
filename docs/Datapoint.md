# Datapoint

Datapoint contains the DatapointRow and additional metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datapoint_id** | [**ID**](ID.md) |  | [optional] 
**data_stream_id** | [**ID**](ID.md) |  | [optional] 
**datapoint** | [**DatapointRow**](DatapointRow.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.datapoint import Datapoint

# TODO update the JSON string below
json = "{}"
# create an instance of Datapoint from a JSON string
datapoint_instance = Datapoint.from_json(json)
# print the JSON string representation of the object
print(Datapoint.to_json())

# convert the object into a dict
datapoint_dict = datapoint_instance.to_dict()
# create an instance of Datapoint from a dict
datapoint_from_dict = Datapoint.from_dict(datapoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

