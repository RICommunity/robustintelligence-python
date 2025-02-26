# SecuritydbFileSecurityReport

The security report for a single file in the model repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filepath** | **str** | The name of the file that was scanned. | 
**size** | **int** | The size of the file in bytes. | [optional] 
**sha256** | **str** | The sha256 of the file that was scanned. | [optional] 
**creation_time** | **datetime** | The time when the file was created. | [optional] 
**last_modified_time** | **datetime** | The time when the file was last modified. | [optional] 
**dependencies** | [**List[Dependency]**](Dependency.md) | The list of all dependencies in the file. | [optional] 
**unsafe_dependencies** | [**List[Dependency]**](Dependency.md) | The list of unsafe dependencies. | [optional] 

## Example

```python
from ri.apiclient.models.securitydb_file_security_report import SecuritydbFileSecurityReport

# TODO update the JSON string below
json = "{}"
# create an instance of SecuritydbFileSecurityReport from a JSON string
securitydb_file_security_report_instance = SecuritydbFileSecurityReport.from_json(json)
# print the JSON string representation of the object
print(SecuritydbFileSecurityReport.to_json())

# convert the object into a dict
securitydb_file_security_report_dict = securitydb_file_security_report_instance.to_dict()
# create an instance of SecuritydbFileSecurityReport from a dict
securitydb_file_security_report_from_dict = SecuritydbFileSecurityReport.from_dict(securitydb_file_security_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

