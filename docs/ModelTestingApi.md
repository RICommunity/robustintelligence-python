# ri.apiclient.ModelTestingApi

All URIs are relative to *http://&lt;platform-domain&gt;.rbst.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**start_continuous_test**](#start_continuous_test) | **POST** /v1/continuous-tests/{firewallId.uuid} | StartContinuousTest
[**start_file_scan**](#start_file_scan) | **POST** /v1/file-scans | StartFileScan
[**start_file_scan2**](#start_file_scan2) | **POST** /v1-beta/file-scans | StartFileScan
[**start_stress_test**](#start_stress_test) | **POST** /v1/stress-tests/{projectId.uuid} | StartStressTest

# **start_continuous_test**
> StartContinuousTestResponse  = start_continuous_test()

StartContinuousTest

Starts a Continuous Test and returns a Job object containing metadata for the Test Run.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
firewall_id_uuid | **str** | Unique object ID. | 
firewall_id | **object** | Uniquely specifies a Firewall. | [optional] 
test_run_incremental_config | [**TestRunIncrementalConfig**](TestRunIncrementalConfig.md) |  | [optional] 
override_existing_bins | **bool** |  | [optional] 
agent_id | [**ID**](ID.md) |  | [optional] 
experimental_fields | **Dict[str, object]** | Fields that enable experimental functionality.  WARNING: these fields are experimental; ie, their functionality may not be reliable or backwards-compatible. Do not use these fields in production. | [optional] 

### Return type

[**StartContinuousTestResponse**](StartContinuousTestResponse.md)

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
from ri.apiclient.models.start_continuous_test_request import StartContinuousTestRequest
from ri.apiclient.models.start_continuous_test_response import StartContinuousTestResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

firewall_id_uuid = 'firewall_id_uuid_example'  # str 
firewall_id = ri.apiclient.models.uniquely_specifies_a_firewall/.Uniquely specifies a Firewall.()  # object  (optional)
test_run_incremental_config = TestRunIncrementalConfig()  # TestRunIncrementalConfig  (optional)
override_existing_bins = True  # bool  (optional)
agent_id = ID()  # ID  (optional)
experimental_fields = {
                    'key' : None
                    }  # Dict[str, object]  (optional)

try:
    # StartContinuousTest
    api_response: StartContinuousTestResponse = client.model_testing.start_continuous_test(firewall_id_uuid, firewall_id=firewall_id, test_run_incremental_config=test_run_incremental_config, override_existing_bins=override_existing_bins, agent_id=agent_id, experimental_fields=experimental_fields)
    print("The response of ModelTestingApi->start_continuous_test:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ModelTestingApi->start_continuous_test: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_file_scan**
> StartFileScanResponse  = start_file_scan()

StartFileScan

Starts a File Scan for the specified model.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id | [**ID**](ID.md) |  | 
model_id | [**ID**](ID.md) |  | 
run_time_info | [**RunTimeInfo**](RunTimeInfo.md) |  | [optional] 
agent_id | [**ID**](ID.md) |  | [optional] 

### Return type

[**StartFileScanResponse**](StartFileScanResponse.md)

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
from ri.apiclient.models.start_file_scan_request import StartFileScanRequest
from ri.apiclient.models.start_file_scan_response import StartFileScanResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

project_id = ID()  # ID
model_id = ID()  # ID
run_time_info = RunTimeInfo()  # RunTimeInfo  (optional)
agent_id = ID()  # ID  (optional)

try:
    # StartFileScan
    api_response: StartFileScanResponse = client.model_testing.start_file_scan(
        project_id, model_id, run_time_info=run_time_info, agent_id=agent_id
    )
    print("The response of ModelTestingApi->start_file_scan:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ModelTestingApi->start_file_scan: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_file_scan2**
> StartFileScanResponse  = start_file_scan2()

StartFileScan

Starts a File Scan for the specified model.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id | [**ID**](ID.md) |  | 
model_id | [**ID**](ID.md) |  | 
run_time_info | [**RunTimeInfo**](RunTimeInfo.md) |  | [optional] 
agent_id | [**ID**](ID.md) |  | [optional] 

### Return type

[**StartFileScanResponse**](StartFileScanResponse.md)

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
from ri.apiclient.models.start_file_scan_request import StartFileScanRequest
from ri.apiclient.models.start_file_scan_response import StartFileScanResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

project_id = ID()  # ID
model_id = ID()  # ID
run_time_info = RunTimeInfo()  # RunTimeInfo  (optional)
agent_id = ID()  # ID  (optional)

try:
    # StartFileScan
    api_response: StartFileScanResponse = client.model_testing.start_file_scan2(
        project_id, model_id, run_time_info=run_time_info, agent_id=agent_id
    )
    print("The response of ModelTestingApi->start_file_scan2:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ModelTestingApi->start_file_scan2: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_stress_test**
> StartStressTestResponse  = start_stress_test()

StartStressTest

Starts a Stress Test and returns a Job object containing metadata for the Test Run.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id_uuid | **str** | Unique object ID. | 
project_id | **object** | Uniquely specifies a Project. | [optional] 
test_run_config | [**TestRunConfig**](TestRunConfig.md) |  | [optional] 
agent_id | [**ID**](ID.md) |  | [optional] 
experimental_fields | **Dict[str, object]** | Fields that enable experimental functionality.  WARNING: these fields are experimental; ie, their functionality may not be reliable or backwards-compatible. Do not use these fields in production. | [optional] 

### Return type

[**StartStressTestResponse**](StartStressTestResponse.md)

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
from ri.apiclient.models.start_stress_test_request import StartStressTestRequest
from ri.apiclient.models.start_stress_test_response import StartStressTestResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

project_id_uuid = 'project_id_uuid_example'  # str 
project_id = ri.apiclient.models.uniquely_specifies_a_project/.Uniquely specifies a Project.()  # object  (optional)
test_run_config = TestRunConfig()  # TestRunConfig  (optional)
agent_id = ID()  # ID  (optional)
experimental_fields = {
                    'key' : None
                    }  # Dict[str, object]  (optional)

try:
    # StartStressTest
    api_response: StartStressTestResponse = client.model_testing.start_stress_test(project_id_uuid, project_id=project_id, test_run_config=test_run_config, agent_id=agent_id, experimental_fields=experimental_fields)
    print("The response of ModelTestingApi->start_stress_test:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ModelTestingApi->start_stress_test: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

