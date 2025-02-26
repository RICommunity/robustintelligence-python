# ModelSecurityReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repo_id** | **str** | The ID of the model repository on Hugging Face. | [optional] 
**description** | **str** | Description of the availability of the security report such as &#39;Scan completed&#39; or &#39;Scan in progress. Please check back later for results&#39;. | [optional] 
**repo_metadata** | [**SecuritydbRepoMetadata**](SecuritydbRepoMetadata.md) |  | [optional] 
**file_scan_result** | [**SecuritydbFileScanResult**](SecuritydbFileScanResult.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.model_security_report import ModelSecurityReport

# TODO update the JSON string below
json = "{}"
# create an instance of ModelSecurityReport from a JSON string
model_security_report_instance = ModelSecurityReport.from_json(json)
# print the JSON string representation of the object
print(ModelSecurityReport.to_json())

# convert the object into a dict
model_security_report_dict = model_security_report_instance.to_dict()
# create an instance of ModelSecurityReport from a dict
model_security_report_from_dict = ModelSecurityReport.from_dict(model_security_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

