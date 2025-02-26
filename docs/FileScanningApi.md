# ri.apiclient.FileScanningApi

All URIs are relative to *http://&lt;platform-domain&gt;.rbst.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_file_scan_result**](#delete_file_scan_result) | **DELETE** /v1/file-scan-results/{fileScanId.uuid} | DeleteFileScanResult
[**delete_file_scan_result2**](#delete_file_scan_result2) | **DELETE** /v1-beta/file-scan-results/{fileScanId.uuid} | DeleteFileScanResult
[**get_file_scan_result**](#get_file_scan_result) | **GET** /v1/file-scan-results/{fileScanId.uuid} | GetFileScanResult
[**get_file_scan_result2**](#get_file_scan_result2) | **GET** /v1-beta/file-scan-results/{fileScanId.uuid} | GetFileScanResult
[**list_file_scan_results**](#list_file_scan_results) | **GET** /v1/file-scan-results | ListFileScanResults
[**list_file_scan_results2**](#list_file_scan_results2) | **GET** /v1-beta/file-scan-results | ListFileScanResults

# **delete_file_scan_result**
> object  = delete_file_scan_result()

DeleteFileScanResult

Deletes a File Scan result by ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
file_scan_id_uuid | **str** | Unique object ID. | 

### Return type

**object**

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
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

file_scan_id_uuid = 'file_scan_id_uuid_example'  # str 

try:
    # DeleteFileScanResult
    api_response: object = client.FileScanningApi.delete_file_scan_result(file_scan_id_uuid)
    print("The response of FileScanningApi->delete_file_scan_result:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling FileScanningApi->delete_file_scan_result: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file_scan_result2**
> object  = delete_file_scan_result2()

DeleteFileScanResult

Deletes a File Scan result by ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
file_scan_id_uuid | **str** | Unique object ID. | 

### Return type

**object**

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
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

file_scan_id_uuid = 'file_scan_id_uuid_example'  # str 

try:
    # DeleteFileScanResult
    api_response: object = client.FileScanningApi.delete_file_scan_result2(file_scan_id_uuid)
    print("The response of FileScanningApi->delete_file_scan_result2:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling FileScanningApi->delete_file_scan_result2: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_scan_result**
> GetFileScanResultResponse  = get_file_scan_result()

GetFileScanResult

Returns a File Scan result by ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
file_scan_id_uuid | **str** | Unique object ID. | 

### Return type

[**GetFileScanResultResponse**](GetFileScanResultResponse.md)

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
from ri.apiclient.models.get_file_scan_result_response import GetFileScanResultResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

file_scan_id_uuid = 'file_scan_id_uuid_example'  # str 

try:
    # GetFileScanResult
    api_response: GetFileScanResultResponse = client.FileScanningApi.get_file_scan_result(file_scan_id_uuid)
    print("The response of FileScanningApi->get_file_scan_result:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling FileScanningApi->get_file_scan_result: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_scan_result2**
> GetFileScanResultResponse  = get_file_scan_result2()

GetFileScanResult

Returns a File Scan result by ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
file_scan_id_uuid | **str** | Unique object ID. | 

### Return type

[**GetFileScanResultResponse**](GetFileScanResultResponse.md)

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
from ri.apiclient.models.get_file_scan_result_response import GetFileScanResultResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

file_scan_id_uuid = 'file_scan_id_uuid_example'  # str 

try:
    # GetFileScanResult
    api_response: GetFileScanResultResponse = client.FileScanningApi.get_file_scan_result2(file_scan_id_uuid)
    print("The response of FileScanningApi->get_file_scan_result2:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling FileScanningApi->get_file_scan_result2: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_file_scan_results**
> ListFileScanResultsResponse  = list_file_scan_results()

ListFileScanResults

Returns a paginated list of all File Scan results for the project.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
first_page_query_project_id_uuid | **str** | Unique object ID. | [optional] 
first_page_query_model_id_uuid | **str** | Unique object ID. | [optional] 
page_token | **str** | Specifies a page of the list returned by a ListFileScan query beyond the first page. | [optional] 
page_size | **str** | Defines the maximum number of results on a given page. API call pagination navigates through the entire set of results in groups of the specified page size. | [optional] 

### Return type

[**ListFileScanResultsResponse**](ListFileScanResultsResponse.md)

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
from ri.apiclient.models.list_file_scan_results_response import ListFileScanResultsResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

first_page_query_project_id_uuid = 'first_page_query_project_id_uuid_example'  # str  (optional)
first_page_query_model_id_uuid = 'first_page_query_model_id_uuid_example'  # str  (optional)
page_token = 'page_token_example'  # str  (optional)
page_size = 'page_size_example'  # str  (optional)

try:
    # ListFileScanResults
    api_response: ListFileScanResultsResponse = client.FileScanningApi.list_file_scan_results(first_page_query_project_id_uuid=first_page_query_project_id_uuid, first_page_query_model_id_uuid=first_page_query_model_id_uuid, page_token=page_token, page_size=page_size)
    print("The response of FileScanningApi->list_file_scan_results:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling FileScanningApi->list_file_scan_results: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_file_scan_results2**
> ListFileScanResultsResponse  = list_file_scan_results2()

ListFileScanResults

Returns a paginated list of all File Scan results for the project.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
first_page_query_project_id_uuid | **str** | Unique object ID. | [optional] 
first_page_query_model_id_uuid | **str** | Unique object ID. | [optional] 
page_token | **str** | Specifies a page of the list returned by a ListFileScan query beyond the first page. | [optional] 
page_size | **str** | Defines the maximum number of results on a given page. API call pagination navigates through the entire set of results in groups of the specified page size. | [optional] 

### Return type

[**ListFileScanResultsResponse**](ListFileScanResultsResponse.md)

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
from ri.apiclient.models.list_file_scan_results_response import ListFileScanResultsResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

first_page_query_project_id_uuid = 'first_page_query_project_id_uuid_example'  # str  (optional)
first_page_query_model_id_uuid = 'first_page_query_model_id_uuid_example'  # str  (optional)
page_token = 'page_token_example'  # str  (optional)
page_size = 'page_size_example'  # str  (optional)

try:
    # ListFileScanResults
    api_response: ListFileScanResultsResponse = client.FileScanningApi.list_file_scan_results2(first_page_query_project_id_uuid=first_page_query_project_id_uuid, first_page_query_model_id_uuid=first_page_query_model_id_uuid, page_token=page_token, page_size=page_size)
    print("The response of FileScanningApi->list_file_scan_results2:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling FileScanningApi->list_file_scan_results2: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

