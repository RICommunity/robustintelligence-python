# SecuritydbFileScanResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_update_time** | **datetime** | The time when the result was updated. | [optional] 
**file_security_reports** | [**List[SecuritydbFileSecurityReport]**](SecuritydbFileSecurityReport.md) | The security reports for the files that were scanned. | [optional] 
**scanned_file_paths** | **List[str]** | The list of files that were scanned. | [optional] 
**severity** | [**GenerativeSeverity**](GenerativeSeverity.md) |  | [optional] [default to GenerativeSeverity.NONE]

## Example

```python
from ri.apiclient.models.securitydb_file_scan_result import SecuritydbFileScanResult

# TODO update the JSON string below
json = "{}"
# create an instance of SecuritydbFileScanResult from a JSON string
securitydb_file_scan_result_instance = SecuritydbFileScanResult.from_json(json)
# print the JSON string representation of the object
print(SecuritydbFileScanResult.to_json())

# convert the object into a dict
securitydb_file_scan_result_dict = securitydb_file_scan_result_instance.to_dict()
# create an instance of SecuritydbFileScanResult from a dict
securitydb_file_scan_result_from_dict = SecuritydbFileScanResult.from_dict(
    securitydb_file_scan_result_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

