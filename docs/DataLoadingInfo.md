# DataLoadingInfo

DataLoadingInfo provides the information needed to load a data file with extra parameters and loading function.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The path to the python file containing the data loading function. | 
**load_func_name** | **str** | The name of the function that loads the data. | 
**loader_kwargs_json** | **str** | This is a JSON-serialized string from a map. | [optional] 
**data_endpoint_integration_id** | [**ID**](ID.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.data_loading_info import DataLoadingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataLoadingInfo from a JSON string
data_loading_info_instance = DataLoadingInfo.from_json(json)
# print the JSON string representation of the object
print(DataLoadingInfo.to_json())

# convert the object into a dict
data_loading_info_dict = data_loading_info_instance.to_dict()
# create an instance of DataLoadingInfo from a dict
data_loading_info_from_dict = DataLoadingInfo.from_dict(data_loading_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

