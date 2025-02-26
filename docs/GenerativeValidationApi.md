# ri.apiclient.GenerativeValidationApi

All URIs are relative to *http://&lt;platform-domain&gt;.rbst.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quick_scan**](#quick_scan) | **POST** /v1-beta/generative/testing/quick | Start Generative AI Validation Quick Scan
[**results**](#results) | **GET** /v1-beta/generative/testing/{testRunId.uuid} | Get Generative AI Validation Results
[**start_generative_test**](#start_generative_test) | **POST** /v1-beta/generative/testing | Start a Generative AI Validation Test
[**test_run**](#test_run) | **GET** /v1-beta/generative/testing/runs/{testRunId.uuid} | Get Generative AI Validation Test Run
[**test_runs**](#test_runs) | **GET** /v1-beta/generative/testing/workspaces/{workspaceId.uuid} | List Generative AI Validation Test Runs

# **quick_scan**
> StartTestResponse  = quick_scan()

Start Generative AI Validation Quick Scan

Starts an AI Validation quick scan on the specified generative model.  Results for this are not comprehensive. The status of the job can be tracked through the [JobReader service](#tag/JobReader). The results can of the test  can be retrieved using the [Results endpoint](#tag/GenerativeModelTesting/operation/Results).

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
url | **str** | Parameters for connecting to the user&#39;s generative model. | [optional] 
http_headers | **Dict[str, str]** |  | [optional] 
endpoint_payload_template | **str** | A string template that will be used to create the json payload sent to the LLM endpoint. This template must contain one and only one variable -- prompt_string. This will be replaced at runtime with the prompt used to send to the model. Used for arbitrary HTTP requests to models.  The template uses \&quot; and \&quot; as the opening and closing delimiters around the prompt_string variable name.  Example: &#39;{ \&quot;prompt\&quot;: \&quot;{{prompt_string}}\&quot; }&#39; Example: &#39;{ \&quot;message\&quot;: { \&quot;llm_prompt\&quot;: \&quot;{{prompt_string}}\&quot; } }&#39; | [optional] 
response_json_path | **str** | A json path specifying where in the HTTP response json payload we can find the LLM&#39;s response string. Note that the path must point to a string value in the json payload. Whitespace and other special characters can be encoded as unicode (\\u0020). Periods in json fields can be escaped with a backslash.  Example (top level field): - Endpoint response json: {\&quot;response\&quot;: \&quot;I am an AI Chatbot, how can I assist you?\&quot;} - response_json_path: \&quot;response\&quot;  Example (nested json field): - Endpoint response json: {\&quot;response\&quot;: {\&quot;llmResponse\&quot;: \&quot;I am an AI Chatbot, how can I assist you?\&quot;}} - response_json_path: \&quot;response.llmResponse\&quot;  Example (extract string from array): - Endpoint response: {\&quot;response\&quot;: {\&quot;options\&quot;: [\&quot;Hi\&quot;, \&quot;Hello there\&quot;], \&quot;count\&quot;: 2}} - response_json_path: \&quot;response.options.1\&quot;  Example (periods in field names): - Endpoint response: {\&quot;llm.response\&quot;: \&quot;hello\&quot;} - response_json_path: \&quot;llm\\\\.response\&quot;  The syntax uses dot notation only, such as \&quot;myfield.myotherfield\&quot; or \&quot;myarray.1\&quot;. | [optional] 
http_auth_integration_id | [**ID**](ID.md) |  | [optional] 
name | **str** | The name to identify the generative model testing job. | [optional] 
mutual_tls_integration_id | [**ID**](ID.md) |  | [optional] 
system_prompt | **str** | The system prompt that is currently active on the provided endpoint. | [optional] 
aws_integration_id | [**ID**](ID.md) |  | [optional] 
model_id | **str** | If aws_integration_id is set, this field will be the model id used for generative validation for bedrock. | [optional] 
body | [**Body**](Body.md) |  | [optional] 
workspace_id | [**ID**](ID.md) |  | [optional] 
agent_id | [**ID**](ID.md) |  | [optional] 

### Return type

[**StartTestResponse**](StartTestResponse.md)

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
from ri.apiclient.models.start_test_request import StartTestRequest
from ri.apiclient.models.start_test_response import StartTestResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

url = ''  # str  (optional)
http_headers = {
                    'key' : ''
                    }  # Dict[str, str]  (optional)
endpoint_payload_template = ''  # str  (optional)
response_json_path = ''  # str  (optional)
http_auth_integration_id = ID()  # ID  (optional)
name = ''  # str  (optional)
mutual_tls_integration_id = ID()  # ID  (optional)
system_prompt = ''  # str  (optional)
aws_integration_id = ID()  # ID  (optional)
model_id = ''  # str  (optional)
body = Body()  # Body  (optional)
workspace_id = ID()  # ID  (optional)
agent_id = ID()  # ID  (optional)

try:
    # Start Generative AI Validation Quick Scan
    api_response: StartTestResponse = client.GenerativeValidationApi.quick_scan(url=url, http_headers=http_headers, endpoint_payload_template=endpoint_payload_template, response_json_path=response_json_path, http_auth_integration_id=http_auth_integration_id, name=name, mutual_tls_integration_id=mutual_tls_integration_id, system_prompt=system_prompt, aws_integration_id=aws_integration_id, model_id=model_id, body=body, workspace_id=workspace_id, agent_id=agent_id)
    print("The response of GenerativeValidationApi->quick_scan:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling GenerativeValidationApi->quick_scan: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **results**
> GetResultsResponse  = results()

Get Generative AI Validation Results

Retrieve the results of a generative model testing for a successful job. This is a paginated API.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
test_run_id_uuid | **str** | Unique object ID. | 
page_token | **str** | A token representing one page from the list returned by a GetResults API. The GetResults API returns a page_token when there is more than one page of results. | [optional] 
page_size | **int** | The maximum number of objects to return in a single page.  Maximum page size is 1000. | [optional] 

### Return type

[**GetResultsResponse**](GetResultsResponse.md)

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
from ri.apiclient.models.get_results_response import GetResultsResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

test_run_id_uuid = 'test_run_id_uuid_example'  # str 
page_token = 'page_token_example'  # str  (optional)
page_size = 56  # int  (optional)

try:
    # Get Generative AI Validation Results
    api_response: GetResultsResponse = client.GenerativeValidationApi.results(test_run_id_uuid, page_token=page_token, page_size=page_size)
    print("The response of GenerativeValidationApi->results:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling GenerativeValidationApi->results: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_generative_test**
> StartTestResponse  = start_generative_test()

Start a Generative AI Validation Test

Starts an AI validation test on the specified generative model. Generative testing is designed to work with a model that is served over an HTTP endpoint that returns JSON. It assumes that the model is a Q&A style model which takes a prompt as an input and returns a single textual response. See the API details for supported features, such as system prompt.  The status of the job can be tracked through the [JobReader service](#tag/JobReader). The results of the test can be retrieved using the [Results endpoint](#tag/GenerativeModelTesting/operation/Results).

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
url | **str** | Parameters for connecting to the user&#39;s generative model. | [optional] 
http_headers | **Dict[str, str]** |  | [optional] 
endpoint_payload_template | **str** | A string template that will be used to create the json payload sent to the LLM endpoint. This template must contain one and only one variable -- prompt_string. This will be replaced at runtime with the prompt used to send to the model. Used for arbitrary HTTP requests to models.  The template uses \&quot; and \&quot; as the opening and closing delimiters around the prompt_string variable name.  Example: &#39;{ \&quot;prompt\&quot;: \&quot;{{prompt_string}}\&quot; }&#39; Example: &#39;{ \&quot;message\&quot;: { \&quot;llm_prompt\&quot;: \&quot;{{prompt_string}}\&quot; } }&#39; | [optional] 
response_json_path | **str** | A json path specifying where in the HTTP response json payload we can find the LLM&#39;s response string. Note that the path must point to a string value in the json payload. Whitespace and other special characters can be encoded as unicode (\\u0020). Periods in json fields can be escaped with a backslash.  Example (top level field): - Endpoint response json: {\&quot;response\&quot;: \&quot;I am an AI Chatbot, how can I assist you?\&quot;} - response_json_path: \&quot;response\&quot;  Example (nested json field): - Endpoint response json: {\&quot;response\&quot;: {\&quot;llmResponse\&quot;: \&quot;I am an AI Chatbot, how can I assist you?\&quot;}} - response_json_path: \&quot;response.llmResponse\&quot;  Example (extract string from array): - Endpoint response: {\&quot;response\&quot;: {\&quot;options\&quot;: [\&quot;Hi\&quot;, \&quot;Hello there\&quot;], \&quot;count\&quot;: 2}} - response_json_path: \&quot;response.options.1\&quot;  Example (periods in field names): - Endpoint response: {\&quot;llm.response\&quot;: \&quot;hello\&quot;} - response_json_path: \&quot;llm\\\\.response\&quot;  The syntax uses dot notation only, such as \&quot;myfield.myotherfield\&quot; or \&quot;myarray.1\&quot;. | [optional] 
http_auth_integration_id | [**ID**](ID.md) |  | [optional] 
name | **str** | The name to identify the generative model testing job. | [optional] 
mutual_tls_integration_id | [**ID**](ID.md) |  | [optional] 
system_prompt | **str** | The system prompt that is currently active on the provided endpoint. | [optional] 
aws_integration_id | [**ID**](ID.md) |  | [optional] 
model_id | **str** | If aws_integration_id is set, this field will be the model id used for generative validation for bedrock. | [optional] 
body | [**Body**](Body.md) |  | [optional] 
workspace_id | [**ID**](ID.md) |  | [optional] 
agent_id | [**ID**](ID.md) |  | [optional] 

### Return type

[**StartTestResponse**](StartTestResponse.md)

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
from ri.apiclient.models.start_test_request import StartTestRequest
from ri.apiclient.models.start_test_response import StartTestResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

url = ''  # str  (optional)
http_headers = {
                    'key' : ''
                    }  # Dict[str, str]  (optional)
endpoint_payload_template = ''  # str  (optional)
response_json_path = ''  # str  (optional)
http_auth_integration_id = ID()  # ID  (optional)
name = ''  # str  (optional)
mutual_tls_integration_id = ID()  # ID  (optional)
system_prompt = ''  # str  (optional)
aws_integration_id = ID()  # ID  (optional)
model_id = ''  # str  (optional)
body = Body()  # Body  (optional)
workspace_id = ID()  # ID  (optional)
agent_id = ID()  # ID  (optional)

try:
    # Start a Generative AI Validation Test
    api_response: StartTestResponse = client.GenerativeValidationApi.start_generative_test(url=url, http_headers=http_headers, endpoint_payload_template=endpoint_payload_template, response_json_path=response_json_path, http_auth_integration_id=http_auth_integration_id, name=name, mutual_tls_integration_id=mutual_tls_integration_id, system_prompt=system_prompt, aws_integration_id=aws_integration_id, model_id=model_id, body=body, workspace_id=workspace_id, agent_id=agent_id)
    print("The response of GenerativeValidationApi->start_generative_test:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling GenerativeValidationApi->start_generative_test: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_run**
> GenerativevalidationGetTestRunResponse  = test_run()

Get Generative AI Validation Test Run

Retrieves a generative validation test run by ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
test_run_id_uuid | **str** | Unique object ID. | 

### Return type

[**GenerativevalidationGetTestRunResponse**](GenerativevalidationGetTestRunResponse.md)

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
from ri.apiclient.models.generativevalidation_get_test_run_response import GenerativevalidationGetTestRunResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

test_run_id_uuid = 'test_run_id_uuid_example'  # str 

try:
    # Get Generative AI Validation Test Run
    api_response: GenerativevalidationGetTestRunResponse = client.GenerativeValidationApi.test_run(test_run_id_uuid)
    print("The response of GenerativeValidationApi->test_run:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling GenerativeValidationApi->test_run: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_runs**
> GenerativevalidationListTestRunsResponse  = test_runs()

List Generative AI Validation Test Runs

Retrieves generative validation test runs for a workspace.  This is a paginated API.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
workspace_id_uuid | **str** | Unique object ID. | 
page_token | **str** | A token representing one page from the list returned by a GetGenerativeModelTestResults API. The GetGenerativeModelTestResults API returns a page_token when there is more than one page of results. | [optional] 
page_size | **int** | The maximum number of objects to return in a single page.  Maximum page size is 1000. | [optional] 

### Return type

[**GenerativevalidationListTestRunsResponse**](GenerativevalidationListTestRunsResponse.md)

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
from ri.apiclient.models.generativevalidation_list_test_runs_response import GenerativevalidationListTestRunsResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

workspace_id_uuid = 'workspace_id_uuid_example'  # str 
page_token = 'page_token_example'  # str  (optional)
page_size = 56  # int  (optional)

try:
    # List Generative AI Validation Test Runs
    api_response: GenerativevalidationListTestRunsResponse = client.GenerativeValidationApi.test_runs(workspace_id_uuid, page_token=page_token, page_size=page_size)
    print("The response of GenerativeValidationApi->test_runs:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling GenerativeValidationApi->test_runs: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

