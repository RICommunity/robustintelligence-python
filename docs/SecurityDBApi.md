# ri.apiclient.SecurityDBApi

All URIs are relative to *http://&lt;platform-domain&gt;.rbst.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_model_security_report**](#get_model_security_report) | **GET** /v1-beta/security-report/model | GetModelSecurityReport
[**list_model_security_reports**](#list_model_security_reports) | **GET** /v1-beta/security-report/models | ListModelSecurityReports

# **get_model_security_report**
> GetModelSecurityReportResponse  = get_model_security_report()

GetModelSecurityReport

Returns the supply chain risk report for a Hugging Face model.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
repo_id | **str** | The ID of the model repository on Hugging Face. | 

### Return type

[**GetModelSecurityReportResponse**](GetModelSecurityReportResponse.md)

### Authorization


[rime-api-key](../README.md#rime-api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### Example
```python

host_name = "http://<platform-domain>.rbst.io"

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rime-api-key
rime_api_key = os.environ["API_KEY"]

```

```python
import ri.apiclient
from ri import RIClient
from ri.apiclient.models.get_model_security_report_response import GetModelSecurityReportResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

repo_id = 'repo_id_example'  # str 

try:
    # GetModelSecurityReport
    api_response: GetModelSecurityReportResponse = client.SecurityDBApi.get_model_security_report(repo_id)
    print("The response of SecurityDBApi->get_model_security_report:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling SecurityDBApi->get_model_security_report: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_model_security_reports**
> ListModelSecurityReportsResponse  = list_model_security_reports()

ListModelSecurityReports

Returns all supply chain risk reports for the workspace.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page_token | **str** | A token representing one page from the list returned by a ListModelSecurityReports API. The ListModelSecurityReports API returns a page_token when there is more than one page of results. | [optional] 
page_size | **str** | The maximum number of objects to return in a single page. Maximum page size is 1000. | [optional] 

### Return type

[**ListModelSecurityReportsResponse**](ListModelSecurityReportsResponse.md)

### Authorization


[rime-api-key](../README.md#rime-api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### Example
```python

host_name = "http://<platform-domain>.rbst.io"

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rime-api-key
rime_api_key = os.environ["API_KEY"]

```

```python
import ri.apiclient
from ri import RIClient
from ri.apiclient.models.list_model_security_reports_response import ListModelSecurityReportsResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

page_token = 'page_token_example'  # str  (optional)
page_size = 'page_size_example'  # str  (optional)

try:
    # ListModelSecurityReports
    api_response: ListModelSecurityReportsResponse = client.SecurityDBApi.list_model_security_reports(page_token=page_token, page_size=page_size)
    print("The response of SecurityDBApi->list_model_security_reports:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling SecurityDBApi->list_model_security_reports: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

