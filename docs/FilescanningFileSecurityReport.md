# FilescanningFileSecurityReport

The security report for a single file in the model repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | The name of the file that was scanned. | 
**path** | **str** | The path of the file that was scanned. | [optional] 
**size** | **str** | The size of the file in bytes. | [optional] 
**sha256** | **str** | The sha256 of the file that was scanned. | [optional] 
**creation_time** | **datetime** | The time when the file was created. | [optional] 
**last_modified_time** | **datetime** | The time when the file was last modified. | [optional] 
**dependencies** | **List[str]** | The list of all dependencies in the file. | [optional] 
**unexpected_dependencies** | **List[str]** | The list of unexpected dependencies. | [optional] 
**unsafe_dependencies** | **List[str]** | The list of unsafe dependencies. | [optional] 

## Example

```python
from ri.apiclient.models.filescanning_file_security_report import FilescanningFileSecurityReport

# TODO update the JSON string below
json = "{}"
# create an instance of FilescanningFileSecurityReport from a JSON string
filescanning_file_security_report_instance = FilescanningFileSecurityReport.from_json(json)
# print the JSON string representation of the object
print(FilescanningFileSecurityReport.to_json())

# convert the object into a dict
filescanning_file_security_report_dict = filescanning_file_security_report_instance.to_dict()
# create an instance of FilescanningFileSecurityReport from a dict
filescanning_file_security_report_from_dict = FilescanningFileSecurityReport.from_dict(filescanning_file_security_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

