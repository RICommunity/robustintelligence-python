# FilescanningFileScanResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_scan_id** | [**ID**](ID.md) |  | 
**project_id** | [**ID**](ID.md) |  | 
**model_id** | [**ID**](ID.md) |  | 
**rime_agent_version** | **str** | The version of the RIME agent that was used to scan the model. | [optional] 
**upload_time** | **datetime** | The time when the file scan result was uploaded. | [optional] 
**file_security_reports** | [**List[FilescanningFileSecurityReport]**](FilescanningFileSecurityReport.md) | The security reports for the files that were scanned. | [optional] 
**repo_metadata** | [**FilescanningRepoMetadata**](FilescanningRepoMetadata.md) |  | [optional] 
**unscanned_file_paths** | **List[str]** | The list of files that were not scanned. | [optional] 
**severity** | [**RimeSeverity**](RimeSeverity.md) |  | [optional] [default to RimeSeverity.UNSPECIFIED]

## Example

```python
from ri.apiclient.models.filescanning_file_scan_result import FilescanningFileScanResult

# TODO update the JSON string below
json = "{}"
# create an instance of FilescanningFileScanResult from a JSON string
filescanning_file_scan_result_instance = FilescanningFileScanResult.from_json(json)
# print the JSON string representation of the object
print(FilescanningFileScanResult.to_json())

# convert the object into a dict
filescanning_file_scan_result_dict = filescanning_file_scan_result_instance.to_dict()
# create an instance of FilescanningFileScanResult from a dict
filescanning_file_scan_result_from_dict = FilescanningFileScanResult.from_dict(
    filescanning_file_scan_result_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

