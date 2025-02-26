# DataCollectorInfo

DataCollectorInfo provides the information needed to load a data stream from a data collector.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_stream_id** | [**ID**](ID.md) |  | 

## Example

```python
from ri.apiclient.models.data_collector_info import DataCollectorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataCollectorInfo from a JSON string
data_collector_info_instance = DataCollectorInfo.from_json(json)
# print the JSON string representation of the object
print(DataCollectorInfo.to_json())

# convert the object into a dict
data_collector_info_dict = data_collector_info_instance.to_dict()
# create an instance of DataCollectorInfo from a dict
data_collector_info_from_dict = DataCollectorInfo.from_dict(data_collector_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

