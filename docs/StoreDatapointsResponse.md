# StoreDatapointsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datapoint_ids** | [**List[ID]**](ID.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.store_datapoints_response import StoreDatapointsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StoreDatapointsResponse from a JSON string
store_datapoints_response_instance = StoreDatapointsResponse.from_json(json)
# print the JSON string representation of the object
print(StoreDatapointsResponse.to_json())

# convert the object into a dict
store_datapoints_response_dict = store_datapoints_response_instance.to_dict()
# create an instance of StoreDatapointsResponse from a dict
store_datapoints_response_from_dict = StoreDatapointsResponse.from_dict(store_datapoints_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

