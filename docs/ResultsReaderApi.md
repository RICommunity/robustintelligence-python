# ri.apiclient.ResultsReaderApi

All URIs are relative to *http://&lt;platform-domain&gt;.rbst.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_test_run**](#delete_test_run) | **DELETE** /v1/test-runs/{testRunId} | DeleteTestRun
[**get_batch_result**](#get_batch_result) | **GET** /v1/test-runs/{testRunId}/batch-result/{testType} | GetBatchResult
[**get_category_results**](#get_category_results) | **GET** /v1/category-results/{testRunId} | GetCategoryResults
[**get_feature_result**](#get_feature_result) | **GET** /v1/test-runs/{testRunId}/feature-result/{urlSafeFeatureId} | GetFeatureResult
[**get_test_config**](#get_test_config) | **GET** /v1-beta/test-runs/{testRunId}/test-config/{configName} | GetTestConfig
[**get_test_run**](#get_test_run) | **GET** /v1/test-runs/{testRunId} | GetTestRun
[**list_batch_results**](#list_batch_results) | **GET** /v1/batch-results | ListBatchResults
[**list_feature_results**](#list_feature_results) | **GET** /v1/feature-results | ListFeatureResults
[**list_monitor_categories**](#list_monitor_categories) | **GET** /v1-beta/test-runs/test-category/monitor | ListMonitorCategories
[**list_summary_tests**](#list_summary_tests) | **GET** /v1/summary-tests | ListSummaryTests
[**list_test_cases**](#list_test_cases) | **GET** /v1/test-cases | ListTestCases
[**list_test_runs**](#list_test_runs) | **GET** /v1/test-runs | ListTestRuns
[**list_validation_categories**](#list_validation_categories) | **GET** /v1-beta/test-runs/test-category/validation | ListValidationCategories
[**rename_test_run**](#rename_test_run) | **POST** /v1/test-runs/rename/{testRunId} | RenameTestRun

# **delete_test_run**
> object  = delete_test_run()

DeleteTestRun

Deletes a specified test run.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
test_run_id | **str** | Uniquely specifies a Test Run to delete. | 

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

test_run_id = 'test_run_id_example'  # str 

try:
    # DeleteTestRun
    api_response: object = client.ResultsReaderApi.delete_test_run(test_run_id)
    print("The response of ResultsReaderApi->delete_test_run:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ResultsReaderApi->delete_test_run: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_batch_result**
> GetBatchResultResponse  = get_batch_result()

GetBatchResult

Gets the batch result for a given Test Run ID and a test type.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
test_run_id | **str** | Uniquely specifies a Test Run. | 
test_type | **str** | The type of test, such as \&quot;Subset Accuracy\&quot; or \&quot;Overall Metrics\&quot;. | 
show_display | **bool** | A Boolean flag that toggles whether to return display HTML. info with message. | [optional] 

### Return type

[**GetBatchResultResponse**](GetBatchResultResponse.md)

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
from ri.apiclient.models.get_batch_result_response import GetBatchResultResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

test_run_id = 'test_run_id_example'  # str 
test_type = 'test_type_example'  # str 
show_display = True  # bool  (optional)

try:
    # GetBatchResult
    api_response: GetBatchResultResponse = client.ResultsReaderApi.get_batch_result(test_run_id, test_type, show_display=show_display)
    print("The response of ResultsReaderApi->get_batch_result:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ResultsReaderApi->get_batch_result: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category_results**
> GetCategoryResultsResponse  = get_category_results()

GetCategoryResults

Returns all category results of a test run.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
test_run_id | **str** | The ID of the test run associated with summary tests. Specify exactly one of the page_token field or this field. | 

### Return type

[**GetCategoryResultsResponse**](GetCategoryResultsResponse.md)

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
from ri.apiclient.models.get_category_results_response import GetCategoryResultsResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

test_run_id = 'test_run_id_example'  # str 

try:
    # GetCategoryResults
    api_response: GetCategoryResultsResponse = client.ResultsReaderApi.get_category_results(test_run_id)
    print("The response of ResultsReaderApi->get_category_results:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ResultsReaderApi->get_category_results: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_result**
> GetFeatureResultResponse  = get_feature_result()

GetFeatureResult

Returns the feature result that matches the specified test run ID and feature ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
test_run_id | **str** | Uniquely specifies a Test Run. | 
url_safe_feature_id | **str** | Uniquely specifies a Feature. | 
show_display | **bool** | A Boolean flag that specifies whether to return display HTML information. | [optional] 

### Return type

[**GetFeatureResultResponse**](GetFeatureResultResponse.md)

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
from ri.apiclient.models.get_feature_result_response import GetFeatureResultResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

test_run_id = 'test_run_id_example'  # str 
url_safe_feature_id = 'url_safe_feature_id_example'  # str 
show_display = True  # bool  (optional)

try:
    # GetFeatureResult
    api_response: GetFeatureResultResponse = client.ResultsReaderApi.get_feature_result(test_run_id, url_safe_feature_id, show_display=show_display)
    print("The response of ResultsReaderApi->get_feature_result:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ResultsReaderApi->get_feature_result: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_config**
> GetTestConfigResponse  = get_test_config()

GetTestConfig

Returns the test configuration of the specified test run as bytes.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
test_run_id | **str** | Uniquely specifies a Test Run. | 
config_name | **str** | The name of the test config requested. | 

### Return type

[**GetTestConfigResponse**](GetTestConfigResponse.md)

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
from ri.apiclient.models.get_test_config_response import GetTestConfigResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

test_run_id = 'test_run_id_example'  # str 
config_name = 'config_name_example'  # str 

try:
    # GetTestConfig
    api_response: GetTestConfigResponse = client.ResultsReaderApi.get_test_config(test_run_id, config_name)
    print("The response of ResultsReaderApi->get_test_config:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ResultsReaderApi->get_test_config: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_run**
> TestrunresultGetTestRunResponse  = get_test_run()

GetTestRun

Returns the test run result detail for a given Test Run ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
test_run_id | **str** | Uniquely specifies a test run. | 

### Return type

[**TestrunresultGetTestRunResponse**](TestrunresultGetTestRunResponse.md)

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
from ri.apiclient.models.testrunresult_get_test_run_response import TestrunresultGetTestRunResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

test_run_id = 'test_run_id_example'  # str 

try:
    # GetTestRun
    api_response: TestrunresultGetTestRunResponse = client.ResultsReaderApi.get_test_run(test_run_id)
    print("The response of ResultsReaderApi->get_test_run:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ResultsReaderApi->get_test_run: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_batch_results**
> ListBatchResultsResponse  = list_batch_results()

ListBatchResults

Returns a paginated list of batch results from a test run.  #### Python pagination example:  ```python all_objects = [] # Required for authentication to all methods in the API. headers = {\"rime-api-key\": \"INSERT_API_TOKEN\"} # TODO page_token = \"\" # Initialize query parameters in a dictionary params = {\"INSERT_QUERY_PARAMETER\": \"INSERT_QUERY_VALUE\"} # TODO # Make requests until all results have been returned. while True:     # If the page_token from a previous response is not empty, we need to specify this     # token as a parameter to the next request in order to return the next page.     if page_token != \"\":         params = {\"page_token\": page_token}     res = requests.get(\"INSERT_METHOD_URI\", params=params, headers=headers) # TODO     if res.status_code != 200 :         raise ValueError(res)     res_json = res.json()     all_objects.extend(res_json['INSERT_OBJECT_KEY']) # TODO     page_token = res_json['nextPageToken']     # If all results have been returned, res_json['hasMore'] is false.     if not res_json[\"hasMore\"]:         break ```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
test_run_id | **str** | The ID of the Test Run associated with batch results. Specify exactly one of the pageToken field or this field. | [optional] 
page_token | **str** | A token representing one page from the list returned by a ListBatchResults query. The ListBatchResults query returns a page_token when there is more than one page of results. Specify exactly one of the testRunId field or this field. | [optional] 
page_size | **str** | The maximum number of Batch Result objects to return in a single page. | [optional] 
show_display | **bool** | A Boolean that toggles whether to return display html info. | [optional] 

### Return type

[**ListBatchResultsResponse**](ListBatchResultsResponse.md)

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
from ri.apiclient.models.list_batch_results_response import ListBatchResultsResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

test_run_id = 'test_run_id_example'  # str  (optional)
page_token = 'page_token_example'  # str  (optional)
page_size = 'page_size_example'  # str  (optional)
show_display = True  # bool  (optional)

try:
    # ListBatchResults
    api_response: ListBatchResultsResponse = client.ResultsReaderApi.list_batch_results(test_run_id=test_run_id, page_token=page_token, page_size=page_size, show_display=show_display)
    print("The response of ResultsReaderApi->list_batch_results:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ResultsReaderApi->list_batch_results: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_feature_results**
> ListFeatureResultsResponse  = list_feature_results()

ListFeatureResults

List all feature results from a test run.  #### Python pagination example:  ```python all_objects = [] # Required for authentication to all methods in the API. headers = {\"rime-api-key\": \"INSERT_API_TOKEN\"} # TODO page_token = \"\" # Initialize query parameters in a dictionary params = {\"INSERT_QUERY_PARAMETER\": \"INSERT_QUERY_VALUE\"} # TODO # Make requests until all results have been returned. while True:     # If the page_token from a previous response is not empty, we need to specify this     # token as a parameter to the next request in order to return the next page.     if page_token != \"\":         params = {\"page_token\": page_token}     res = requests.get(\"INSERT_METHOD_URI\", params=params, headers=headers) # TODO     if res.status_code != 200 :         raise ValueError(res)     res_json = res.json()     all_objects.extend(res_json['INSERT_OBJECT_KEY']) # TODO     page_token = res_json['nextPageToken']     # If all results have been returned, res_json['hasMore'] is false.     if not res_json[\"hasMore\"]:         break ```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
test_run_id | **str** | The ID of the Test Run associated with feature results. Specify exactly one of the page_token field or this field. | [optional] 
page_token | **str** | A token representing one page from the list returned by a ListFeatureResults query. The ListFeatureResults query returns a page_token when there is more than one page of results. Specify exactly one of the testRunId field or this field. | [optional] 
page_size | **str** | The maximum number of Feature Result objects to return in a single page. | [optional] 
show_display | **bool** | A Boolean that specifies whether to return display HTML information. | [optional] 

### Return type

[**ListFeatureResultsResponse**](ListFeatureResultsResponse.md)

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
from ri.apiclient.models.list_feature_results_response import ListFeatureResultsResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

test_run_id = 'test_run_id_example'  # str  (optional)
page_token = 'page_token_example'  # str  (optional)
page_size = 'page_size_example'  # str  (optional)
show_display = True  # bool  (optional)

try:
    # ListFeatureResults
    api_response: ListFeatureResultsResponse = client.ResultsReaderApi.list_feature_results(test_run_id=test_run_id, page_token=page_token, page_size=page_size, show_display=show_display)
    print("The response of ResultsReaderApi->list_feature_results:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ResultsReaderApi->list_feature_results: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_monitor_categories**
> ListMonitorCategoriesResponse  = list_monitor_categories()

ListMonitorCategories

Returns test categories belongs to monitor.

### Parameters

This endpoint does not need any parameters.
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

### Return type

[**ListMonitorCategoriesResponse**](ListMonitorCategoriesResponse.md)

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
from ri.apiclient.models.list_monitor_categories_response import ListMonitorCategoriesResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)


try:
    # ListMonitorCategories
    api_response: ListMonitorCategoriesResponse = client.ResultsReaderApi.list_monitor_categories()
    print("The response of ResultsReaderApi->list_monitor_categories:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ResultsReaderApi->list_monitor_categories: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_summary_tests**
> ListSummaryTestsResponse  = list_summary_tests()

ListSummaryTests

Returns a paginated list of the summary tests of a test run. DEPRECATED: Use GetCategoryResults instead, the API request and response are the same. This method will be removed in the future.  #### Python pagination example:  ```python all_objects = [] # Required for authentication to all methods in the API. headers = {\"rime-api-key\": \"INSERT_API_TOKEN\"} # TODO page_token = \"\" # Initialize query parameters in a dictionary params = {\"INSERT_QUERY_PARAMETER\": \"INSERT_QUERY_VALUE\"} # TODO # Make requests until all results have been returned. while True:     # If the page_token from a previous response is not empty, we need to specify this     # token as a parameter to the next request in order to return the next page.     if page_token != \"\":         params = {\"page_token\": page_token}     res = requests.get(\"INSERT_METHOD_URI\", params=params, headers=headers) # TODO     if res.status_code != 200 :         raise ValueError(res)     res_json = res.json()     all_objects.extend(res_json['INSERT_OBJECT_KEY']) # TODO     page_token = res_json['nextPageToken']     # If all results have been returned, res_json['hasMore'] is false.     if not res_json[\"hasMore\"]:         break ```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_test_run_id | **str** | The ID of the test run associated with summary tests. Specify exactly one of the page_token field or this field. | [optional] 
page_token | **str** | A token representing one page from the list returned by a ListSummaryTests query. The ListSummaryTests query returns a page_token when there is more than one page of results. Specify exactly one of the query.testRunId field or this field. | [optional] 
page_size | **str** | The maximum number of Summary Test objects to return in a single page. | [optional] 

### Return type

[**ListSummaryTestsResponse**](ListSummaryTestsResponse.md)

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
from ri.apiclient.models.list_summary_tests_response import ListSummaryTestsResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

query_test_run_id = 'query_test_run_id_example'  # str  (optional)
page_token = 'page_token_example'  # str  (optional)
page_size = 'page_size_example'  # str  (optional)

try:
    # ListSummaryTests
    api_response: ListSummaryTestsResponse = client.ResultsReaderApi.list_summary_tests(query_test_run_id=query_test_run_id, page_token=page_token, page_size=page_size)
    print("The response of ResultsReaderApi->list_summary_tests:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ResultsReaderApi->list_summary_tests: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_test_cases**
> ListTestCasesResponse  = list_test_cases()

ListTestCases

Returns a paginated list of the test cases in a test run. Specify a set of test types to filter the list by test types.  #### Python pagination example:  ```python all_objects = [] # Required for authentication to all methods in the API. headers = {\"rime-api-key\": \"INSERT_API_TOKEN\"} # TODO page_token = \"\" # Initialize query parameters in a dictionary params = {\"INSERT_QUERY_PARAMETER\": \"INSERT_QUERY_VALUE\"} # TODO # Make requests until all results have been returned. while True:     # If the page_token from a previous response is not empty, we need to specify this     # token as a parameter to the next request in order to return the next page.     if page_token != \"\":         params = {\"page_token\": page_token}     res = requests.get(\"INSERT_METHOD_URI\", params=params, headers=headers) # TODO     if res.status_code != 200 :         raise ValueError(res)     res_json = res.json()     all_objects.extend(res_json['INSERT_OBJECT_KEY']) # TODO     page_token = res_json['nextPageToken']     # If all results have been returned, res_json['hasMore'] is false.     if not res_json[\"hasMore\"]:         break ```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
list_test_cases_query_test_run_id | **str** | Uniquely specifies a Test Run associated with test cases. Specify exactly one of the page_token field or this field. | [optional] 
list_test_cases_query_test_types | [**List[str]**](str.md) | Optional filter for test types. | [optional] 
list_test_cases_query_url_safe_feature_ids | [**List[str]**](str.md) | Optional filter for features.  &#x60;test_types&#x60; and &#x60;url_safe_feature_ids&#x60; are applied as &#39;In&#39; filters.  Filters are not applied to empty slices. | [optional] 
page_token | **str** | A token representing one page from the list returned by a ListTestCases query. The ListTestCases query returns a page_token when there is more than one page of results. Specify exactly one of the ListTestCasesQuery.testRunId field or this field. | [optional] 
page_size | **str** | The maximum number of Test Case objects to return in a single page. | [optional] 
show_display | **bool** | A Boolean flag that specifies whether to return display HTML information with the message. | [optional] 

### Return type

[**ListTestCasesResponse**](ListTestCasesResponse.md)

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
from ri.apiclient.models.list_test_cases_response import ListTestCasesResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

list_test_cases_query_test_run_id = 'list_test_cases_query_test_run_id_example'  # str  (optional)
list_test_cases_query_test_types = ['list_test_cases_query_test_types_example']  # List[str]  (optional)
list_test_cases_query_url_safe_feature_ids = ['list_test_cases_query_url_safe_feature_ids_example']  # List[str]  (optional)
page_token = 'page_token_example'  # str  (optional)
page_size = 'page_size_example'  # str  (optional)
show_display = True  # bool  (optional)

try:
    # ListTestCases
    api_response: ListTestCasesResponse = client.ResultsReaderApi.list_test_cases(list_test_cases_query_test_run_id=list_test_cases_query_test_run_id, list_test_cases_query_test_types=list_test_cases_query_test_types, list_test_cases_query_url_safe_feature_ids=list_test_cases_query_url_safe_feature_ids, page_token=page_token, page_size=page_size, show_display=show_display)
    print("The response of ResultsReaderApi->list_test_cases:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ResultsReaderApi->list_test_cases: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_test_runs**
> TestrunresultListTestRunsResponse  = list_test_runs()

ListTestRuns

Lists all test runs belonging to a project.  #### Python pagination example:  ```python all_objects = [] # Required for authentication to all methods in the API. headers = {\"rime-api-key\": \"INSERT_API_TOKEN\"} # TODO page_token = \"\" # Initialize query parameters in a dictionary params = {\"INSERT_QUERY_PARAMETER\": \"INSERT_QUERY_VALUE\"} # TODO # Make requests until all results have been returned. while True:     # If the page_token from a previous response is not empty, we need to specify this     # token as a parameter to the next request in order to return the next page.     if page_token != \"\":         params = {\"page_token\": page_token}     res = requests.get(\"INSERT_METHOD_URI\", params=params, headers=headers) # TODO     if res.status_code != 200 :         raise ValueError(res)     res_json = res.json()     all_objects.extend(res_json['INSERT_OBJECT_KEY']) # TODO     page_token = res_json['nextPageToken']     # If all results have been returned, res_json['hasMore'] is false.     if not res_json[\"hasMore\"]:         break ```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id | **str** | The field is deprecated in v2.2. Use first_page_query.project_id instead. The field will be removed after v2.3. The ID of the project containing the requested test runs. Specify exactly one of the page_token field or this field. | [optional] 
page_token | **str** | A token representing one page from the list returned by a ListTestRuns query. The ListTestRuns query returns a page_token when there is more than one page of results. Specify exactly one of the projectId field or this field. | [optional] 
first_page_query_project_id_uuid | **str** | Unique object ID. | [optional] 
first_page_query_testing_type | **str** | The test type of Test Runs to request. Defaults to Stress Testing.   - TEST_TYPE_STRESS_TESTING_UNSPECIFIED: Default type as stress testing | [optional] [default to TEST_TYPE_STRESS_TESTING_UNSPECIFIED]
first_page_query_schedule_id_uuid | **str** | Unique object ID. | [optional] 
page_size | **str** | The maximum number of Test Run objects to return in a single page. | [optional] 

### Return type

[**TestrunresultListTestRunsResponse**](TestrunresultListTestRunsResponse.md)

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
from ri.apiclient.models.testrunresult_list_test_runs_response import TestrunresultListTestRunsResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

project_id = 'project_id_example'  # str  (optional)
page_token = 'page_token_example'  # str  (optional)
first_page_query_project_id_uuid = 'first_page_query_project_id_uuid_example'  # str  (optional)
first_page_query_testing_type = TEST_TYPE_STRESS_TESTING_UNSPECIFIED  # str  (optional) (default to TEST_TYPE_STRESS_TESTING_UNSPECIFIED)
first_page_query_schedule_id_uuid = 'first_page_query_schedule_id_uuid_example'  # str  (optional)
page_size = 'page_size_example'  # str  (optional)

try:
    # ListTestRuns
    api_response: TestrunresultListTestRunsResponse = client.ResultsReaderApi.list_test_runs(project_id=project_id, page_token=page_token, first_page_query_project_id_uuid=first_page_query_project_id_uuid, first_page_query_testing_type=first_page_query_testing_type, first_page_query_schedule_id_uuid=first_page_query_schedule_id_uuid, page_size=page_size)
    print("The response of ResultsReaderApi->list_test_runs:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ResultsReaderApi->list_test_runs: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_validation_categories**
> ListValidationCategoriesResponse  = list_validation_categories()

ListValidationCategories

Returns test categories belongs to validation.

### Parameters

This endpoint does not need any parameters.
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

### Return type

[**ListValidationCategoriesResponse**](ListValidationCategoriesResponse.md)

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
from ri.apiclient.models.list_validation_categories_response import ListValidationCategoriesResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)


try:
    # ListValidationCategories
    api_response: ListValidationCategoriesResponse = client.ResultsReaderApi.list_validation_categories()
    print("The response of ResultsReaderApi->list_validation_categories:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ResultsReaderApi->list_validation_categories: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_test_run**
> RenameTestRunResponse  = rename_test_run()

RenameTestRun

Updates the name of a test run.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
test_run_id | **str** | Uniquely specifies a Test Run to rename. | 
name | **str** | The new name of the Test Run. | [optional] 

### Return type

[**RenameTestRunResponse**](RenameTestRunResponse.md)

### Authorization


[rime-api-key](../README.md#rime-api-key)

### HTTP request headers

- **Content-Type**: application/json
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
from ri.apiclient.models.rename_test_run_request import RenameTestRunRequest
from ri.apiclient.models.rename_test_run_response import RenameTestRunResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

test_run_id = 'test_run_id_example'  # str 
name = ''  # str  (optional)

try:
    # RenameTestRun
    api_response: RenameTestRunResponse = client.ResultsReaderApi.rename_test_run(test_run_id, name=name)
    print("The response of ResultsReaderApi->rename_test_run:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ResultsReaderApi->rename_test_run: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

