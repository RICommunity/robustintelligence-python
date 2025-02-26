# ListFileScanResultsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[FilescanningFileScanResult]**](FilescanningFileScanResult.md) |  | [optional] 
**next_page_token** | **str** | A token representing the next page from the list returned by a ListFileScanResults query. | [optional] 
**has_more** | **bool** | A Boolean that specifies whether there are more File Scan results to return. | [optional] 

## Example

```python
from ri.apiclient.models.list_file_scan_results_response import ListFileScanResultsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListFileScanResultsResponse from a JSON string
list_file_scan_results_response_instance = ListFileScanResultsResponse.from_json(json)
# print the JSON string representation of the object
print(ListFileScanResultsResponse.to_json())

# convert the object into a dict
list_file_scan_results_response_dict = list_file_scan_results_response_instance.to_dict()
# create an instance of ListFileScanResultsResponse from a dict
list_file_scan_results_response_from_dict = ListFileScanResultsResponse.from_dict(list_file_scan_results_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

