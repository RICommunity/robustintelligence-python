# ri.apiclient.WorkspaceServiceApi

All URIs are relative to *http://&lt;platform-domain&gt;.rbst.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_users_to_workspace**](#add_users_to_workspace) | **POST** /v1/workspace/{workspaceId.uuid}/users | AddUsersToWorkspace
[**create_workspace**](#create_workspace) | **POST** /v1/workspace | CreateWorkspace
[**delete_workspace**](#delete_workspace) | **DELETE** /v1/workspace/{workspaceId.uuid} | DeleteWorkspace
[**get_workspace**](#get_workspace) | **GET** /v1/workspace/{workspaceId.uuid} | GetWorkspace
[**list_project_tags_in_workspace**](#list_project_tags_in_workspace) | **GET** /v1/workspace/{workspaceId.uuid}/tags/project | ListProjectTagsInWorkspace
[**list_users_of_workspace**](#list_users_of_workspace) | **GET** /v1/workspace/{workspaceId.uuid}/users | ListUsersOfWorkspace
[**list_workspaces**](#list_workspaces) | **GET** /v1/workspace | ListWorkspaces
[**remove_user_from_workspace**](#remove_user_from_workspace) | **DELETE** /v1/workspace/{workspaceId.uuid}/users/{userId.uuid} | RemoveUserFromWorkspace
[**update_user_of_workspace**](#update_user_of_workspace) | **PUT** /v1/workspace/{workspaceId.uuid}/users/{user.userId.uuid} | UpdateUserOfWorkspace
[**update_workspace**](#update_workspace) | **PUT** /v1/workspace/{workspace.workspaceId.uuid} | UpdateWorkspace

# **add_users_to_workspace**
> object  = add_users_to_workspace()

AddUsersToWorkspace

Grants Users permissions to a Workspace.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
workspace_id_uuid | **str** | Unique object ID. | 
workspace_id | **object** | Unique ID of an object in RIME. | [optional] 
users | [**List[UserWithRole]**](List.md) | List of Users to add to the Workspace. | 

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
from ri.apiclient.models.add_users_to_workspace_request import AddUsersToWorkspaceRequest
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

workspace_id_uuid = 'workspace_id_uuid_example'  # str 
workspace_id = ri.apiclient.models.workspace_id.workspaceId()  # object  (optional)
users = List[UserWithRole]()  # List[UserWithRole] 

try:
    # AddUsersToWorkspace
    api_response: object = client.WorkspaceServiceApi.add_users_to_workspace(workspace_id_uuid, workspace_id=workspace_id, users)
    print("The response of WorkspaceServiceApi->add_users_to_workspace:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling WorkspaceServiceApi->add_users_to_workspace: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workspace**
> CreateWorkspaceResponse  = create_workspace()

CreateWorkspace

Create a new Workspace.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | **str** | Name of the Workspace. | 
agent_ids | [**List[ID]**](List.md) | List of Agent IDs to be added to the Workspace. | [optional] 
default_agent_id | [**ID**](ID.md) |  | [optional] 
description | **str** | Description of the Workspace. | [optional] 
results_retention_in_days | **int** |  | [optional] 

### Return type

[**CreateWorkspaceResponse**](CreateWorkspaceResponse.md)

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
from ri.apiclient.models.create_workspace_request import CreateWorkspaceRequest
from ri.apiclient.models.create_workspace_response import CreateWorkspaceResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

name = ''  # str 
agent_ids = List[ID]()  # List[ID]  (optional)
default_agent_id = ID()  # ID  (optional)
description = ''  # str  (optional)
results_retention_in_days = 56  # int  (optional)

try:
    # CreateWorkspace
    api_response: CreateWorkspaceResponse = client.WorkspaceServiceApi.create_workspace(name, agent_ids=agent_ids, default_agent_id=default_agent_id, description=description, results_retention_in_days=results_retention_in_days)
    print("The response of WorkspaceServiceApi->create_workspace:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling WorkspaceServiceApi->create_workspace: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace**
> object  = delete_workspace()

DeleteWorkspace

Deletes an existing Workspace by ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
workspace_id_uuid | **str** | Unique object ID. | 

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

workspace_id_uuid = 'workspace_id_uuid_example'  # str 

try:
    # DeleteWorkspace
    api_response: object = client.WorkspaceServiceApi.delete_workspace(workspace_id_uuid)
    print("The response of WorkspaceServiceApi->delete_workspace:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling WorkspaceServiceApi->delete_workspace: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace**
> GetWorkspaceResponse  = get_workspace()

GetWorkspace

Return a Workspace by ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
workspace_id_uuid | **str** | Unique object ID. | 

### Return type

[**GetWorkspaceResponse**](GetWorkspaceResponse.md)

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
from ri.apiclient.models.get_workspace_response import GetWorkspaceResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

workspace_id_uuid = 'workspace_id_uuid_example'  # str 

try:
    # GetWorkspace
    api_response: GetWorkspaceResponse = client.WorkspaceServiceApi.get_workspace(workspace_id_uuid)
    print("The response of WorkspaceServiceApi->get_workspace:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling WorkspaceServiceApi->get_workspace: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_tags_in_workspace**
> ListProjectTagsInWorkspaceResponse  = list_project_tags_in_workspace()

ListProjectTagsInWorkspace

List the union of all tags in all projects in the workspace

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
workspace_id_uuid | **str** | Unique object ID. | 

### Return type

[**ListProjectTagsInWorkspaceResponse**](ListProjectTagsInWorkspaceResponse.md)

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
from ri.apiclient.models.list_project_tags_in_workspace_response import ListProjectTagsInWorkspaceResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

workspace_id_uuid = 'workspace_id_uuid_example'  # str 

try:
    # ListProjectTagsInWorkspace
    api_response: ListProjectTagsInWorkspaceResponse = client.WorkspaceServiceApi.list_project_tags_in_workspace(workspace_id_uuid)
    print("The response of WorkspaceServiceApi->list_project_tags_in_workspace:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling WorkspaceServiceApi->list_project_tags_in_workspace: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users_of_workspace**
> ListUsersOfWorkspaceResponse  = list_users_of_workspace()

ListUsersOfWorkspace

Lists all Users that have permissions to a Workspace.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
workspace_id_uuid | **str** | Unique object ID. | 
page_token | **str** | Specifies a page of the list returned by a ListUsersOfWorkspace query. The ListUsersOfWorkspace query returns a pageToken when there is more than one page of results. | [optional] 
page_size | **str** | The maximum number of User objects to return in a single page. | [optional] 

### Return type

[**ListUsersOfWorkspaceResponse**](ListUsersOfWorkspaceResponse.md)

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
from ri.apiclient.models.list_users_of_workspace_response import ListUsersOfWorkspaceResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

workspace_id_uuid = 'workspace_id_uuid_example'  # str 
page_token = 'page_token_example'  # str  (optional)
page_size = 'page_size_example'  # str  (optional)

try:
    # ListUsersOfWorkspace
    api_response: ListUsersOfWorkspaceResponse = client.WorkspaceServiceApi.list_users_of_workspace(workspace_id_uuid, page_token=page_token, page_size=page_size)
    print("The response of WorkspaceServiceApi->list_users_of_workspace:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling WorkspaceServiceApi->list_users_of_workspace: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workspaces**
> ListWorkspacesResponse  = list_workspaces()

ListWorkspaces

List Workspaces with optional filter.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page_size | **str** | The maximum number of Workspace objects to return in a single page. | [optional] 
page_token | **str** | Specifies a page of the list returned by a ListWorkspaces query. The ListWorkspaces query returns a pageToken when there is more than one page of results. | [optional] 

### Return type

[**ListWorkspacesResponse**](ListWorkspacesResponse.md)

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
from ri.apiclient.models.list_workspaces_response import ListWorkspacesResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

page_size = 'page_size_example'  # str  (optional)
page_token = 'page_token_example'  # str  (optional)

try:
    # ListWorkspaces
    api_response: ListWorkspacesResponse = client.WorkspaceServiceApi.list_workspaces(page_size=page_size, page_token=page_token)
    print("The response of WorkspaceServiceApi->list_workspaces:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling WorkspaceServiceApi->list_workspaces: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_from_workspace**
> object  = remove_user_from_workspace()

RemoveUserFromWorkspace

Removes a User from a Workspace.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
workspace_id_uuid | **str** | Unique object ID. | 
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

workspace_id_uuid = 'workspace_id_uuid_example'  # str 
user_id_uuid = 'user_id_uuid_example'  # str 

try:
    # RemoveUserFromWorkspace
    api_response: object = client.WorkspaceServiceApi.remove_user_from_workspace(workspace_id_uuid, user_id_uuid)
    print("The response of WorkspaceServiceApi->remove_user_from_workspace:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling WorkspaceServiceApi->remove_user_from_workspace: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_of_workspace**
> object  = update_user_of_workspace()

UpdateUserOfWorkspace

Updates the permission of a specified User for a Workspace.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
workspace_id_uuid | **str** | Unique object ID. | 
user_user_id_uuid | **str** | Unique object ID. | 
workspace_id | **object** | Unique ID of an object in RIME. | [optional] 
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
from ri.apiclient.models.update_user_of_workspace_request import UpdateUserOfWorkspaceRequest
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

workspace_id_uuid = 'workspace_id_uuid_example'  # str 
user_user_id_uuid = 'user_user_id_uuid_example'  # str 
workspace_id = ri.apiclient.models.workspace_id.workspaceId()  # object  (optional)
user = UpdateUserOfProjectRequestUser()  # UpdateUserOfProjectRequestUser  (optional)

try:
    # UpdateUserOfWorkspace
    api_response: object = client.WorkspaceServiceApi.update_user_of_workspace(workspace_id_uuid, user_user_id_uuid, workspace_id=workspace_id, user=user)
    print("The response of WorkspaceServiceApi->update_user_of_workspace:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling WorkspaceServiceApi->update_user_of_workspace: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workspace**
> object  = update_workspace()

UpdateWorkspace

Updates an existing Workspace by ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
workspace_workspace_id_uuid | **str** | Unique object ID. | 
workspace | [**UpdateWorkspaceRequestWorkspace**](UpdateWorkspaceRequestWorkspace.md) |  | [optional] 
workspace_write_mask | [**WorkspaceWriteMask**](WorkspaceWriteMask.md) |  | [optional] 

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
from ri.apiclient.models.update_workspace_request import UpdateWorkspaceRequest
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

workspace_workspace_id_uuid = 'workspace_workspace_id_uuid_example'  # str 
workspace = UpdateWorkspaceRequestWorkspace()  # UpdateWorkspaceRequestWorkspace  (optional)
workspace_write_mask = WorkspaceWriteMask()  # WorkspaceWriteMask  (optional)

try:
    # UpdateWorkspace
    api_response: object = client.WorkspaceServiceApi.update_workspace(workspace_workspace_id_uuid, workspace=workspace, workspace_write_mask=workspace_write_mask)
    print("The response of WorkspaceServiceApi->update_workspace:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling WorkspaceServiceApi->update_workspace: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

