# ri.apiclient.ProjectServiceApi

All URIs are relative to *http://&lt;platform-domain&gt;.rbst.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_schedule_for_project**](#activate_schedule_for_project) | **PUT** /v1-beta/projects/{projectId.uuid}/schedule/{scheduleId.uuid}/activate | ActivateScheduleForProject
[**add_users_to_project**](#add_users_to_project) | **POST** /v1/projects/{projectId.uuid}/role/users | AddUsersToProject
[**create_project**](#create_project) | **POST** /v1/projects | CreateProject
[**deactivate_schedule_for_project**](#deactivate_schedule_for_project) | **PUT** /v1-beta/projects/{projectId.uuid}/schedule/{scheduleId.uuid}/deactivate | DeactivateScheduleForProject
[**delete_project**](#delete_project) | **DELETE** /v1/projects/{projectId.uuid} | DeleteProject
[**get_project**](#get_project) | **GET** /v1/projects/{projectId.uuid} | GetProject
[**get_project_url**](#get_project_url) | **GET** /v1/projects/{projectId.uuid}/url | GetProjectURL
[**get_workspace_roles_for_project**](#get_workspace_roles_for_project) | **GET** /v1/projects/{projectId.uuid}/role/workspace | GetWorkspaceRoleForProject
[**list_projects**](#list_projects) | **GET** /v1/projects | ListProjects
[**list_users_of_project**](#list_users_of_project) | **GET** /v1/projects/{projectId.uuid}/role/users | ListUsersOfProject
[**remove_user_from_project**](#remove_user_from_project) | **DELETE** /v1/projects/{projectId.uuid}/role/users/{userId.uuid} | RemoveUserFromProject
[**update_project**](#update_project) | **PUT** /v1/projects/{projectId.uuid} | UpdateProject
[**update_user_of_project**](#update_user_of_project) | **PUT** /v1/projects/{projectId.uuid}/role/users/{user.userId.uuid} | UpdateUserOfProject
[**update_workspace_roles_for_project**](#update_workspace_roles_for_project) | **PUT** /v1/projects/{projectId.uuid}/role/workspace | UpdateWorkspaceRoleForProject

# **activate_schedule_for_project**
> ActivateScheduleForProjectResponse  = activate_schedule_for_project()

ActivateScheduleForProject

Add a Schedule to run automatic tests for a Project.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id_uuid | **str** | Unique object ID. | 
schedule_id_uuid | **str** | Unique object ID. | 
project_id | **object** | Unique ID of an object in RIME. | [optional] 
schedule_id | **object** | Unique ID of an object in RIME. | [optional] 

### Return type

[**ActivateScheduleForProjectResponse**](ActivateScheduleForProjectResponse.md)

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
from ri.apiclient.models.activate_schedule_for_project_request import (
    ActivateScheduleForProjectRequest,
)
from ri.apiclient.models.activate_schedule_for_project_response import (
    ActivateScheduleForProjectResponse,
)
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

project_id_uuid = "project_id_uuid_example"  # str
schedule_id_uuid = "schedule_id_uuid_example"  # str
project_id = {}  # object  (optional)
schedule_id = {}  # object  (optional)

try:
    # ActivateScheduleForProject
    api_response: ActivateScheduleForProjectResponse = (
        client.project_service.activate_schedule_for_project(
            project_id_uuid,
            schedule_id_uuid,
            project_id=project_id,
            schedule_id=schedule_id,
        )
    )
    print("The response of ProjectServiceApi->activate_schedule_for_project:\n")
    pprint(api_response)

except ApiException as e:
    print(
        "Exception when calling ProjectServiceApi->activate_schedule_for_project: %s\n"
        % e
    )
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_users_to_project**
> object  = add_users_to_project()

AddUsersToProject

Grants existing Organization users permissions to a Project for a given Project ID, based on the pairs of role and User ID provided in the request.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id_uuid | **str** | Unique object ID. | 
project_id | **object** | Uniquely specifies a Project. | [optional] 
users | [**List[UserWithRole]**](List.md) | Pairs of users and their roles for the Project. | [optional] 

### Return type

**object**

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
from ri.apiclient.models.add_users_to_project_request import AddUsersToProjectRequest
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

project_id_uuid = 'project_id_uuid_example'  # str 
project_id = ri.apiclient.models.uniquely_specifies_a_project/.Uniquely specifies a Project.()  # object  (optional)
users = List[UserWithRole]  # List[UserWithRole]  (optional)

try:
    # AddUsersToProject
    api_response: object = client.project_service.add_users_to_project(project_id_uuid, project_id=project_id, users=users)
    print("The response of ProjectServiceApi->add_users_to_project:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ProjectServiceApi->add_users_to_project: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> CreateProjectResponse  = create_project()

CreateProject

Creates a Project with required fields. Project is an organizational entity under a Workspace that contains Test Runs, Continuous Tests, and Stress Tests, along with their configurations.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | **str** |  | 
description | **str** |  | 
use_case | **str** |  | [optional] 
ethical_consideration | **str** |  | [optional] 
workspace_id | [**ID**](ID.md) |  | [optional] 
model_task | [**ModelTask**](ModelTask.md) |  | [default to MODEL_TASK_UNSPECIFIED]
tags | **List[str]** | List of tags associated with the Project to help organizing Projects. | [optional] 
profiling_config | [**ProfilingConfig**](ProfilingConfig.md) |  | [optional] 
is_published | **bool** | Published projects are shown on the Workspace overview page. | [optional] 
run_time_info | [**RunTimeInfo**](RunTimeInfo.md) |  | [optional] 

### Return type

[**CreateProjectResponse**](CreateProjectResponse.md)

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
from ri.apiclient.models.create_project_request import CreateProjectRequest
from ri.apiclient.models.create_project_response import CreateProjectResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

name = ''  # str 
description = ''  # str 
use_case = ''  # str  (optional)
ethical_consideration = ''  # str  (optional)
workspace_id = ID()  # ID  (optional)
model_task = ModelTask()  # ModelTask  (default to MODEL_TASK_UNSPECIFIED)
tags = [
                    ''
                    ]  # List[str]  (optional)
profiling_config = ProfilingConfig()  # ProfilingConfig  (optional)
is_published = True  # bool  (optional)
run_time_info = RunTimeInfo()  # RunTimeInfo  (optional)

try:
    # CreateProject
    api_response: CreateProjectResponse = client.project_service.create_project(name, description, use_case=use_case, ethical_consideration=ethical_consideration, workspace_id=workspace_id, model_task, tags=tags, profiling_config=profiling_config, is_published=is_published, run_time_info=run_time_info)
    print("The response of ProjectServiceApi->create_project:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ProjectServiceApi->create_project: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_schedule_for_project**
> object  = deactivate_schedule_for_project()

DeactivateScheduleForProject

Remove a Schedule from a Project.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id_uuid | **str** | Unique object ID. | 
schedule_id_uuid | **str** | Unique object ID. | 
project_id | **object** | Unique ID of an object in RIME. | [optional] 
schedule_id | **object** | Unique ID of an object in RIME. | [optional] 

### Return type

**object**

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
from ri.apiclient.models.activate_schedule_for_project_request import (
    ActivateScheduleForProjectRequest,
)
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

project_id_uuid = "project_id_uuid_example"  # str
schedule_id_uuid = "schedule_id_uuid_example"  # str
project_id = {}  # object  (optional)
schedule_id = {}  # object  (optional)

try:
    # DeactivateScheduleForProject
    api_response: object = client.project_service.deactivate_schedule_for_project(
        project_id_uuid,
        schedule_id_uuid,
        project_id=project_id,
        schedule_id=schedule_id,
    )
    print("The response of ProjectServiceApi->deactivate_schedule_for_project:\n")
    pprint(api_response)

except ApiException as e:
    print(
        "Exception when calling ProjectServiceApi->deactivate_schedule_for_project: %s\n"
        % e
    )
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> object  = delete_project()

DeleteProject

Deletes a Project for a given Project ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id_uuid | **str** | Unique object ID. | 

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

project_id_uuid = "project_id_uuid_example"  # str

try:
    # DeleteProject
    api_response: object = client.project_service.delete_project(project_id_uuid)
    print("The response of ProjectServiceApi->delete_project:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ProjectServiceApi->delete_project: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> GetProjectResponse  = get_project()

GetProject

Returns a Project for a given Project ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id_uuid | **str** | Unique object ID. | 

### Return type

[**GetProjectResponse**](GetProjectResponse.md)

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
from ri.apiclient.models.get_project_response import GetProjectResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

project_id_uuid = "project_id_uuid_example"  # str

try:
    # GetProject
    api_response: GetProjectResponse = client.project_service.get_project(
        project_id_uuid
    )
    print("The response of ProjectServiceApi->get_project:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_project: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_url**
> GetProjectURLResponse  = get_project_url()

GetProjectURL

Return the URL of a Project for a given Project ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id_uuid | **str** | Unique object ID. | 

### Return type

[**GetProjectURLResponse**](GetProjectURLResponse.md)

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
from ri.apiclient.models.get_project_url_response import GetProjectURLResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

project_id_uuid = "project_id_uuid_example"  # str

try:
    # GetProjectURL
    api_response: GetProjectURLResponse = client.project_service.get_project_url(
        project_id_uuid
    )
    print("The response of ProjectServiceApi->get_project_url:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_project_url: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_roles_for_project**
> GetWorkspaceRolesForProjectResponse  = get_workspace_roles_for_project()

GetWorkspaceRoleForProject

Returns the permissions of the Workspace members for a Project given Project ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id_uuid | **str** | Unique object ID. | 

### Return type

[**GetWorkspaceRolesForProjectResponse**](GetWorkspaceRolesForProjectResponse.md)

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
from ri.apiclient.models.get_workspace_roles_for_project_response import (
    GetWorkspaceRolesForProjectResponse,
)
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

project_id_uuid = "project_id_uuid_example"  # str

try:
    # GetWorkspaceRoleForProject
    api_response: GetWorkspaceRolesForProjectResponse = (
        client.project_service.get_workspace_roles_for_project(project_id_uuid)
    )
    print("The response of ProjectServiceApi->get_workspace_roles_for_project:\n")
    pprint(api_response)

except ApiException as e:
    print(
        "Exception when calling ProjectServiceApi->get_workspace_roles_for_project: %s\n"
        % e
    )
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects**
> ListProjectsResponse  = list_projects()

ListProjects

Returns a paginated list of Projects for a given Workspace ID. Filters out Projects that the user does not have access to. The list is sorted by the last test run time field of each Project.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
workspace_id_uuid | **str** | Unique object ID. | [optional] 
first_page_query_is_published | **bool** | Optional: If true, return published projects. If false, return unpublished projects. If not specified, return all projects. | [optional] 
first_page_query_creation_time_range_start_time | **datetime** |  | [optional] 
first_page_query_creation_time_range_end_time | **datetime** |  | [optional] 
first_page_query_last_test_run_time_range_start_time | **datetime** |  | [optional] 
first_page_query_last_test_run_time_range_end_time | **datetime** |  | [optional] 
first_page_query_stress_test_categories | [**List[str]**](str.md) | Optional: When specified, return all projects whose ST categories are a superset of the ST categories provided here. | [optional] 
first_page_query_continuous_test_categories | [**List[str]**](str.md) | Optional: When specified, return all projects whose CT categories are a superset of the CT categories provided here. | [optional] 
first_page_query_owner_email | **str** | Optional: When specified, return all projects whose owner email matches. | [optional] 
first_page_query_model_tasks | [**List[str]**](str.md) | Optional: When specified, return all projects whose model task is the provided model task. | [optional] 
first_page_query_status | **str** | Optional: When specified, return all projects whose status is the provided status. | [optional] [default to PROJECT_STATUS_UNSPECIFIED]
first_page_query_sort_sort_order | **str** |  | [optional] [default to ORDER_UNSPECIFIED]
first_page_query_sort_sort_by | **str** |  | [optional] 
first_page_query_search_expression | **str** |  | [optional] 
first_page_query_search_search_fields | [**List[str]**](str.md) |  | [optional] 
page_token | **str** | Specifies a page of the list returned by a ListProjects query. The ListProjects query returns a pageToken when there is more than one page of results. Specify either this field or the firstPageQuery field. | [optional] 
page_size | **str** | The maximum number of Project objects to return in a single page. | [optional] 

### Return type

[**ListProjectsResponse**](ListProjectsResponse.md)

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
from ri.apiclient.models.list_projects_response import ListProjectsResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

workspace_id_uuid = "workspace_id_uuid_example"  # str  (optional)
first_page_query_is_published = True  # bool  (optional)
first_page_query_creation_time_range_start_time = (
    "2013-10-20T19:20:30+01:00"  # datetime  (optional)
)
first_page_query_creation_time_range_end_time = (
    "2013-10-20T19:20:30+01:00"  # datetime  (optional)
)
first_page_query_last_test_run_time_range_start_time = (
    "2013-10-20T19:20:30+01:00"  # datetime  (optional)
)
first_page_query_last_test_run_time_range_end_time = (
    "2013-10-20T19:20:30+01:00"  # datetime  (optional)
)
first_page_query_stress_test_categories = [
    "first_page_query_stress_test_categories_example"
]  # List[str]  (optional)
first_page_query_continuous_test_categories = [
    "first_page_query_continuous_test_categories_example"
]  # List[str]  (optional)
first_page_query_owner_email = "first_page_query_owner_email_example"  # str  (optional)
first_page_query_model_tasks = [
    "first_page_query_model_tasks_example"
]  # List[str]  (optional)
first_page_query_status = PROJECT_STATUS_UNSPECIFIED  # str  (optional) (default to PROJECT_STATUS_UNSPECIFIED)
first_page_query_sort_sort_order = (
    ORDER_UNSPECIFIED  # str  (optional) (default to ORDER_UNSPECIFIED)
)
first_page_query_sort_sort_by = (
    "first_page_query_sort_sort_by_example"  # str  (optional)
)
first_page_query_search_expression = (
    "first_page_query_search_expression_example"  # str  (optional)
)
first_page_query_search_search_fields = [
    "first_page_query_search_search_fields_example"
]  # List[str]  (optional)
page_token = "page_token_example"  # str  (optional)
page_size = "page_size_example"  # str  (optional)

try:
    # ListProjects
    api_response: ListProjectsResponse = client.project_service.list_projects(
        workspace_id_uuid=workspace_id_uuid,
        first_page_query_is_published=first_page_query_is_published,
        first_page_query_creation_time_range_start_time=first_page_query_creation_time_range_start_time,
        first_page_query_creation_time_range_end_time=first_page_query_creation_time_range_end_time,
        first_page_query_last_test_run_time_range_start_time=first_page_query_last_test_run_time_range_start_time,
        first_page_query_last_test_run_time_range_end_time=first_page_query_last_test_run_time_range_end_time,
        first_page_query_stress_test_categories=first_page_query_stress_test_categories,
        first_page_query_continuous_test_categories=first_page_query_continuous_test_categories,
        first_page_query_owner_email=first_page_query_owner_email,
        first_page_query_model_tasks=first_page_query_model_tasks,
        first_page_query_status=first_page_query_status,
        first_page_query_sort_sort_order=first_page_query_sort_sort_order,
        first_page_query_sort_sort_by=first_page_query_sort_sort_by,
        first_page_query_search_expression=first_page_query_search_expression,
        first_page_query_search_search_fields=first_page_query_search_search_fields,
        page_token=page_token,
        page_size=page_size,
    )
    print("The response of ProjectServiceApi->list_projects:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ProjectServiceApi->list_projects: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users_of_project**
> ListUsersOfProjectResponse  = list_users_of_project()

ListUsersOfProject

Lists the users and their roles of a Project for a given Project ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id_uuid | **str** | Unique object ID. | 
page_token | **str** | Specifies a page of the list returned by a ListUsersOfProject query. The ListUsersOfProject query returns a pageToken when there is more than one page of results. | [optional] 
page_size | **str** | The maximum number of User objects to return in a single page. | [optional] 

### Return type

[**ListUsersOfProjectResponse**](ListUsersOfProjectResponse.md)

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
from ri.apiclient.models.list_users_of_project_response import (
    ListUsersOfProjectResponse,
)
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

project_id_uuid = "project_id_uuid_example"  # str
page_token = "page_token_example"  # str  (optional)
page_size = "page_size_example"  # str  (optional)

try:
    # ListUsersOfProject
    api_response: ListUsersOfProjectResponse = (
        client.project_service.list_users_of_project(
            project_id_uuid, page_token=page_token, page_size=page_size
        )
    )
    print("The response of ProjectServiceApi->list_users_of_project:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ProjectServiceApi->list_users_of_project: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_from_project**
> object  = remove_user_from_project()

RemoveUserFromProject

Removes all existing permissions of a user from a Project given Project ID and User ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id_uuid | **str** | Unique object ID. | 
user_id_uuid | **str** | Unique object ID. | 

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

project_id_uuid = "project_id_uuid_example"  # str
user_id_uuid = "user_id_uuid_example"  # str

try:
    # RemoveUserFromProject
    api_response: object = client.project_service.remove_user_from_project(
        project_id_uuid, user_id_uuid
    )
    print("The response of ProjectServiceApi->remove_user_from_project:\n")
    pprint(api_response)

except ApiException as e:
    print(
        "Exception when calling ProjectServiceApi->remove_user_from_project: %s\n" % e
    )
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> UpdateProjectResponse  = update_project()

UpdateProject

Updates a Project for a given Project ID. Only updates the fields specified in the FieldMask.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id_uuid | **str** | Unique object ID. | 
project_id | **object** | Uniquely specifies a Project to update. | [optional] 
project | [**Project**](Project.md) |  | 
mask | **str** |  | [optional] 

### Return type

[**UpdateProjectResponse**](UpdateProjectResponse.md)

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
from ri.apiclient.models.update_project_request import UpdateProjectRequest
from ri.apiclient.models.update_project_response import UpdateProjectResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

project_id_uuid = 'project_id_uuid_example'  # str 
project_id = ri.apiclient.models.uniquely_specifies_a_project_to_update/.Uniquely specifies a Project to update.()  # object  (optional)
project = Project()  # Project 
mask = ''  # str  (optional)

try:
    # UpdateProject
    api_response: UpdateProjectResponse = client.project_service.update_project(project_id_uuid, project_id=project_id, project, mask=mask)
    print("The response of ProjectServiceApi->update_project:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ProjectServiceApi->update_project: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_of_project**
> object  = update_user_of_project()

UpdateUserOfProject

Updates the existing permission of a user of a Project given Project ID and User ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id_uuid | **str** | Unique object ID. | 
user_user_id_uuid | **str** | Unique object ID. | 
project_id | **object** | Uniquely specifies a Project. | [optional] 
user | [**UpdateUserOfProjectRequestUser**](UpdateUserOfProjectRequestUser.md) |  | [optional] 

### Return type

**object**

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
from ri.apiclient.models.update_user_of_project_request import UpdateUserOfProjectRequest
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

project_id_uuid = 'project_id_uuid_example'  # str 
user_user_id_uuid = 'user_user_id_uuid_example'  # str 
project_id = ri.apiclient.models.uniquely_specifies_a_project/.Uniquely specifies a Project.()  # object  (optional)
user = UpdateUserOfProjectRequestUser()  # UpdateUserOfProjectRequestUser  (optional)

try:
    # UpdateUserOfProject
    api_response: object = client.project_service.update_user_of_project(project_id_uuid, user_user_id_uuid, project_id=project_id, user=user)
    print("The response of ProjectServiceApi->update_user_of_project:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ProjectServiceApi->update_user_of_project: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workspace_roles_for_project**
> UpdateWorkspaceRolesForProjectResponse  = update_workspace_roles_for_project()

UpdateWorkspaceRoleForProject

Assigns users roles(permissions) on a Project based on their roles in the Workspace that contains the Project.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id_uuid | **str** | Unique object ID. | 
project_id | **object** | Uniquely specifies a Project. | [optional] 
role_pairs | [**List[ParentRoleSubjectRolePair]**](List.md) | The elements of role_pairs maps each Workspace role to a Project role. For example, you can specify that a user with admin rights on a Workspace will get viewer rights on Projects in that Workspace. | 

### Return type

[**UpdateWorkspaceRolesForProjectResponse**](UpdateWorkspaceRolesForProjectResponse.md)

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
from ri.apiclient.models.update_workspace_roles_for_project_request import UpdateWorkspaceRolesForProjectRequest
from ri.apiclient.models.update_workspace_roles_for_project_response import UpdateWorkspaceRolesForProjectResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

project_id_uuid = 'project_id_uuid_example'  # str 
project_id = ri.apiclient.models.uniquely_specifies_a_project/.Uniquely specifies a Project.()  # object  (optional)
role_pairs = List[ParentRoleSubjectRolePair]  # List[ParentRoleSubjectRolePair] 

try:
    # UpdateWorkspaceRoleForProject
    api_response: UpdateWorkspaceRolesForProjectResponse = client.project_service.update_workspace_roles_for_project(project_id_uuid, project_id=project_id, role_pairs)
    print("The response of ProjectServiceApi->update_workspace_roles_for_project:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ProjectServiceApi->update_workspace_roles_for_project: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

