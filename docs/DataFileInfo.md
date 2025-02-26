# DataFileInfo

DataFileInfo specifies how to connect to a data file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The path to the data file. | 
**data_type** | [**DataType**](DataType.md) |  | [optional] [default to DataType.UNSPECIFIED]

## Example

```python
from ri.apiclient.models.data_file_info import DataFileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataFileInfo from a JSON string
data_file_info_instance = DataFileInfo.from_json(json)
# print the JSON string representation of the object
print(DataFileInfo.to_json())

# convert the object into a dict
data_file_info_dict = data_file_info_instance.to_dict()
# create an instance of DataFileInfo from a dict
data_file_info_from_dict = DataFileInfo.from_dict(data_file_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

