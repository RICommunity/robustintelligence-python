# FileScanQuery

Query message for selecting File Scan results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | [**ID**](ID.md) |  | 
**model_id** | [**ID**](ID.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.file_scan_query import FileScanQuery

# TODO update the JSON string below
json = "{}"
# create an instance of FileScanQuery from a JSON string
file_scan_query_instance = FileScanQuery.from_json(json)
# print the JSON string representation of the object
print(FileScanQuery.to_json())

# convert the object into a dict
file_scan_query_dict = file_scan_query_instance.to_dict()
# create an instance of FileScanQuery from a dict
file_scan_query_from_dict = FileScanQuery.from_dict(file_scan_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

