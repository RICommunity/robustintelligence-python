# GetFileScanResultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_scan_result** | [**FilescanningFileScanResult**](FilescanningFileScanResult.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.get_file_scan_result_response import GetFileScanResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFileScanResultResponse from a JSON string
get_file_scan_result_response_instance = GetFileScanResultResponse.from_json(json)
# print the JSON string representation of the object
print(GetFileScanResultResponse.to_json())

# convert the object into a dict
get_file_scan_result_response_dict = get_file_scan_result_response_instance.to_dict()
# create an instance of GetFileScanResultResponse from a dict
get_file_scan_result_response_from_dict = GetFileScanResultResponse.from_dict(get_file_scan_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

