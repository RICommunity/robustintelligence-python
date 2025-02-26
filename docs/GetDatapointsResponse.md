# GetDatapointsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datapoints** | [**List[Datapoint]**](Datapoint.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.get_datapoints_response import GetDatapointsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatapointsResponse from a JSON string
get_datapoints_response_instance = GetDatapointsResponse.from_json(json)
# print the JSON string representation of the object
print(GetDatapointsResponse.to_json())

# convert the object into a dict
get_datapoints_response_dict = get_datapoints_response_instance.to_dict()
# create an instance of GetDatapointsResponse from a dict
get_datapoints_response_from_dict = GetDatapointsResponse.from_dict(get_datapoints_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

