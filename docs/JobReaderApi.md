# ri.apiclient.JobReaderApi

All URIs are relative to *http://&lt;platform-domain&gt;.rbst.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_job**](#cancel_job) | **POST** /v1/jobs/cancel/{jobId} | CancelJob
[**get_job**](#get_job) | **GET** /v1/jobs/{jobId} | GetJob
[**get_project_id**](#get_project_id) | **GET** /v1/jobs/{jobId}/project-id | GetProjectID
[**get_test_run_id**](#get_test_run_id) | **GET** /v1/jobs/{jobId}/test-run-id | GetTestRunID
[**list_gai_test_job**](#list_gai_test_job) | **GET** /v1-beta/jobs/generative/workspaces/{workspaceId.uuid} | ListGAITestJob is a method to list all GAI test jobs for a given workspace.
[**list_jobs_for_project**](#list_jobs_for_project) | **GET** /v1/jobs/project/{projectId.uuid} | ListJobsForProject

# **cancel_job**
> object  = cancel_job()

CancelJob

Cancels the job with the specified ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
job_id | **str** | Unique job ID of job to be cancelled. | 

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

job_id = 'job_id_example'  # str 

try:
    # CancelJob
    api_response: object = client.JobReaderApi.cancel_job(job_id)
    print("The response of JobReaderApi->cancel_job:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling JobReaderApi->cancel_job: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> GetJobResponse  = get_job()

GetJob

Get a single job by ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
job_id | **str** | Unique job ID | 
view | **str** | Specifies how much information about the job to retrieve. The default behavior is the Basic view.   - JOB_VIEW_BASIC: Server responses only include basic information about the job, including type, status, and some job data.  - JOB_VIEW_FULL: Server responses include all available information about the job, including progress. Has greater performance requirements than the Basic view. | [optional] [default to JOB_VIEW_UNSPECIFIED]

### Return type

[**GetJobResponse**](GetJobResponse.md)

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
from ri.apiclient.models.get_job_response import GetJobResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

job_id = 'job_id_example'  # str 
view = JOB_VIEW_UNSPECIFIED  # str  (optional) (default to JOB_VIEW_UNSPECIFIED)

try:
    # GetJob
    api_response: GetJobResponse = client.JobReaderApi.get_job(job_id, view=view)
    print("The response of JobReaderApi->get_job:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling JobReaderApi->get_job: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_id**
> GetProjectIDResponse  = get_project_id()

GetProjectID

Returns the project ID of the project running the job with the specified job ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
job_id | **str** | Unique job ID belonging to the project. | 

### Return type

[**GetProjectIDResponse**](GetProjectIDResponse.md)

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
from ri.apiclient.models.get_project_id_response import GetProjectIDResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

job_id = 'job_id_example'  # str 

try:
    # GetProjectID
    api_response: GetProjectIDResponse = client.JobReaderApi.get_project_id(job_id)
    print("The response of JobReaderApi->get_project_id:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling JobReaderApi->get_project_id: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_run_id**
> GetTestRunIDResponse  = get_test_run_id()

GetTestRunID

Returns a test run ID based on a specified job ID. The job ID must be for a completed stress test job.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
job_id | **str** | Unique job ID associated with the test run. | 

### Return type

[**GetTestRunIDResponse**](GetTestRunIDResponse.md)

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
from ri.apiclient.models.get_test_run_id_response import GetTestRunIDResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

job_id = 'job_id_example'  # str 

try:
    # GetTestRunID
    api_response: GetTestRunIDResponse = client.JobReaderApi.get_test_run_id(job_id)
    print("The response of JobReaderApi->get_test_run_id:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling JobReaderApi->get_test_run_id: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_gai_test_job**
> ListGAITestJobResponse  = list_gai_test_job()

ListGAITestJob is a method to list all GAI test jobs for a given workspace.

They will be sorted in descending order by creation time.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
workspace_id_uuid | **str** | Unique object ID. | 
first_page_query_selected_statuses | [**List[str]**](str.md) | Specifies a set of statuses. The query only returns results with a status in the specified set. Specify no statuses to return all results.   - JOB_STATUS_PENDING: Resources have been created for the job but the job has not started yet.  - JOB_STATUS_FAILED: Blanket status for user or system-related job failure.  - JOB_STATUS_REQUESTED: The job descriptor exists but has no resources allocated. Jobs that remain in this status without moving to the PENDING status are at risk of entering the FAILED status.  - JOB_STATUS_CANCELLED: Job has been cancelled. Cancelled jobs cannot be recovered. | [optional] 
page_token | **str** | The ListJobs query returns a pageToken after the first request. | [optional] 
page_size | **str** | The maximum number of Job objects to return in a single page. | [optional] 
view | **str** | Specifies how much information about each job to retrieve.   - JOB_VIEW_BASIC: Server responses only include basic information about the job, including type, status, and some job data.  - JOB_VIEW_FULL: Server responses include all available information about the job, including progress. Has greater performance requirements than the Basic view. | [optional] [default to JOB_VIEW_UNSPECIFIED]

### Return type

[**ListGAITestJobResponse**](ListGAITestJobResponse.md)

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
from ri.apiclient.models.list_gai_test_job_response import ListGAITestJobResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

workspace_id_uuid = 'workspace_id_uuid_example'  # str 
first_page_query_selected_statuses = ['first_page_query_selected_statuses_example']  # List[str]  (optional)
page_token = 'page_token_example'  # str  (optional)
page_size = 'page_size_example'  # str  (optional)
view = JOB_VIEW_UNSPECIFIED  # str  (optional) (default to JOB_VIEW_UNSPECIFIED)

try:
    # ListGAITestJob is a method to list all GAI test jobs for a given workspace.
    api_response: ListGAITestJobResponse = client.JobReaderApi.list_gai_test_job(workspace_id_uuid, first_page_query_selected_statuses=first_page_query_selected_statuses, page_token=page_token, page_size=page_size, view=view)
    print("The response of JobReaderApi->list_gai_test_job:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling JobReaderApi->list_gai_test_job: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_jobs_for_project**
> ListJobsForProjectResponse  = list_jobs_for_project()

ListJobsForProject

Returns a paginated list of jobs for a given project. The list can be filtered by job type and status.  #### Python pagination example:  ```python all_objects = [] # Required for authentication to all methods in the API. headers = {\"rime-api-key\": \"INSERT_API_TOKEN\"} # TODO page_token = \"\" # Initialize query parameters in a dictionary params = {\"INSERT_QUERY_PARAMETER\": \"INSERT_QUERY_VALUE\"} # TODO # Make requests until all results have been returned. while True:     # If the page_token from a previous response is not empty, we need to specify this     # token as a parameter to the next request in order to return the next page.     if page_token != \"\":         params = {\"page_token\": page_token}     res = requests.get(\"INSERT_METHOD_URI\", params=params, headers=headers) # TODO     if res.status_code != 200 :         raise ValueError(res)     res_json = res.json()     all_objects.extend(res_json['INSERT_OBJECT_KEY']) # TODO     page_token = res_json['nextPageToken']     # If all results have been returned, res_json['hasMore'] is false.     if not res_json[\"hasMore\"]:         break ```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id_uuid | **str** | Unique object ID. | 
first_page_query_selected_statuses | [**List[str]**](str.md) | Specifies a set of statuses. The query only returns results with a status in the specified set. Specify no statuses to return all results.   - JOB_STATUS_PENDING: Resources have been created for the job but the job has not started yet.  - JOB_STATUS_FAILED: Blanket status for user or system-related job failure.  - JOB_STATUS_REQUESTED: The job descriptor exists but has no resources allocated. Jobs that remain in this status without moving to the PENDING status are at risk of entering the FAILED status.  - JOB_STATUS_CANCELLED: Job has been cancelled. Cancelled jobs cannot be recovered. | [optional] 
first_page_query_selected_types | [**List[str]**](str.md) | Specifies a set of types. The query only returns jobs with types in the specified set. Specify no types to return all results. Job types not tied to projects will not be returned. | [optional] 
page_token | **str** | The ListJobs query returns a pageToken after the first request. | [optional] 
page_size | **str** | The maximum number of Job objects to return in a single page. | [optional] 
view | **str** | Specifies how much information about each job to retrieve.   - JOB_VIEW_BASIC: Server responses only include basic information about the job, including type, status, and some job data.  - JOB_VIEW_FULL: Server responses include all available information about the job, including progress. Has greater performance requirements than the Basic view. | [optional] [default to JOB_VIEW_UNSPECIFIED]

### Return type

[**ListJobsForProjectResponse**](ListJobsForProjectResponse.md)

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
from ri.apiclient.models.list_jobs_for_project_response import ListJobsForProjectResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

project_id_uuid = 'project_id_uuid_example'  # str 
first_page_query_selected_statuses = ['first_page_query_selected_statuses_example']  # List[str]  (optional)
first_page_query_selected_types = ['first_page_query_selected_types_example']  # List[str]  (optional)
page_token = 'page_token_example'  # str  (optional)
page_size = 'page_size_example'  # str  (optional)
view = JOB_VIEW_UNSPECIFIED  # str  (optional) (default to JOB_VIEW_UNSPECIFIED)

try:
    # ListJobsForProject
    api_response: ListJobsForProjectResponse = client.JobReaderApi.list_jobs_for_project(project_id_uuid, first_page_query_selected_statuses=first_page_query_selected_statuses, first_page_query_selected_types=first_page_query_selected_types, page_token=page_token, page_size=page_size, view=view)
    print("The response of JobReaderApi->list_jobs_for_project:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling JobReaderApi->list_jobs_for_project: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

