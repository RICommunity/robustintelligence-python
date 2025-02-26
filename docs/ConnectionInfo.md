# ConnectionInfo

ConnectionInfo specifies how to connect to a data source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_file** | [**DataFileInfo**](DataFileInfo.md) |  | [optional] 
**data_loading** | [**DataLoadingInfo**](DataLoadingInfo.md) |  | [optional] 
**data_collector** | [**DataCollectorInfo**](DataCollectorInfo.md) |  | [optional] 
**databricks** | [**DatabricksInfo**](DatabricksInfo.md) |  | [optional] 
**hugging_face** | [**HuggingFaceDataInfo**](HuggingFaceDataInfo.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.connection_info import ConnectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionInfo from a JSON string
connection_info_instance = ConnectionInfo.from_json(json)
# print the JSON string representation of the object
print(ConnectionInfo.to_json())

# convert the object into a dict
connection_info_dict = connection_info_instance.to_dict()
# create an instance of ConnectionInfo from a dict
connection_info_from_dict = ConnectionInfo.from_dict(connection_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

