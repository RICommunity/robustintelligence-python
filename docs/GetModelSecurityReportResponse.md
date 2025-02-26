# GetModelSecurityReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_security_report** | [**ModelSecurityReport**](ModelSecurityReport.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.get_model_security_report_response import GetModelSecurityReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetModelSecurityReportResponse from a JSON string
get_model_security_report_response_instance = GetModelSecurityReportResponse.from_json(json)
# print the JSON string representation of the object
print(GetModelSecurityReportResponse.to_json())

# convert the object into a dict
get_model_security_report_response_dict = get_model_security_report_response_instance.to_dict()
# create an instance of GetModelSecurityReportResponse from a dict
get_model_security_report_response_from_dict = GetModelSecurityReportResponse.from_dict(get_model_security_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

