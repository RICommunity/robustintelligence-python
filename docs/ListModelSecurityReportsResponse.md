# ListModelSecurityReportsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_security_reports** | [**List[ModelSecurityReport]**](ModelSecurityReport.md) | The list of security reports for the models. | [optional] 
**next_page_token** | **str** | A token to retrieve the next page of results. | [optional] 
**has_more** | **bool** | A boolean flag that specifies whether there are more results to return. | [optional] 

## Example

```python
from ri.apiclient.models.list_model_security_reports_response import ListModelSecurityReportsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListModelSecurityReportsResponse from a JSON string
list_model_security_reports_response_instance = ListModelSecurityReportsResponse.from_json(json)
# print the JSON string representation of the object
print(ListModelSecurityReportsResponse.to_json())

# convert the object into a dict
list_model_security_reports_response_dict = list_model_security_reports_response_instance.to_dict()
# create an instance of ListModelSecurityReportsResponse from a dict
list_model_security_reports_response_from_dict = ListModelSecurityReportsResponse.from_dict(list_model_security_reports_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

