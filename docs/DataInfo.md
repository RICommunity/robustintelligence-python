# DataInfo

DataInfo specifies the information needed for a dataset.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_info** | [**ConnectionInfo**](ConnectionInfo.md) |  | 
**data_params** | [**DataParams**](DataParams.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.data_info import DataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataInfo from a JSON string
data_info_instance = DataInfo.from_json(json)
# print the JSON string representation of the object
print(DataInfo.to_json())

# convert the object into a dict
data_info_dict = data_info_instance.to_dict()
# create an instance of DataInfo from a dict
data_info_from_dict = DataInfo.from_dict(data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

