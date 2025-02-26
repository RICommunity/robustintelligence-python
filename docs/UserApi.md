# ri.apiclient.UserApi

All URIs are relative to *http://&lt;platform-domain&gt;.rbst.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_token**](#create_api_token) | **POST** /v1/users/api-tokens | CreateAPIToken
[**create_user**](#create_user) | **POST** /v1/users | CreateUser
[**delete_api_token**](#delete_api_token) | **DELETE** /v1/users/api-tokens/{id.uuid} | DeleteAPIToken
[**delete_user**](#delete_user) | **DELETE** /v1/users/{userId.uuid} | DeleteUser
[**get_user**](#get_user) | **GET** /v1/users/{userId.uuid} | GetUser
[**list_api_tokens**](#list_api_tokens) | **GET** /v1/users/api-tokens | ListAPITokens
[**list_current_user_roles**](#list_current_user_roles) | **GET** /v1/users/roles | ListCurrentUserRoles
[**list_users**](#list_users) | **GET** /v1/users | ListUsers
[**reset_password**](#reset_password) | **POST** /v1/users/reset-password/{userId.uuid} | ResetPassword
[**update_agent_api_token**](#update_agent_api_token) | **PUT** /v1/users/agent-api-tokens | UpdateAgentAPIToken
[**update_user**](#update_user) | **PUT** /v1/users/{user.id.uuid} | UpdateUser

# **create_api_token**
> CreateAPITokenResponse  = create_api_token()

CreateAPIToken

Create a new API token.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | **str** | Name of the API token. | 
workspace_id | [**ID**](ID.md) |  | [optional] 
token_type | [**TokenType**](TokenType.md) |  | [optional] [default to TOKEN_TYPE_UNSPECIFIED]
agent_id | [**ID**](ID.md) |  | [optional] 
expiry_days | **int** |  | [optional] 

### Return type

[**CreateAPITokenResponse**](CreateAPITokenResponse.md)

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
from ri.apiclient.models.create_api_token_request import CreateAPITokenRequest
from ri.apiclient.models.create_api_token_response import CreateAPITokenResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

name = ""  # str
workspace_id = ID()  # ID  (optional)
token_type = TokenType()  # TokenType  (optional) (default to TOKEN_TYPE_UNSPECIFIED)
agent_id = ID()  # ID  (optional)
expiry_days = 56  # int  (optional)

try:
    # CreateAPIToken
    api_response: CreateAPITokenResponse = client.user.create_api_token(
        name,
        workspace_id=workspace_id,
        token_type=token_type,
        agent_id=agent_id,
        expiry_days=expiry_days,
    )
    print("The response of UserApi->create_api_token:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling UserApi->create_api_token: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> CreateUserResponse  = create_user()

CreateUser

Creates a user.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
email | **str** | The email address of the user. | 
password | **str** | The password of the user. This password will be changed on the first login. | 
full_name | **str** | The full name of the user. | 
org_role | [**ActorRole**](ActorRole.md) |  | [optional] [default to ACTOR_ROLE_UNSPECIFIED]

### Return type

[**CreateUserResponse**](CreateUserResponse.md)

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
from ri.apiclient.models.create_user_request import CreateUserRequest
from ri.apiclient.models.create_user_response import CreateUserResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

email = ""  # str
password = ""  # str
full_name = ""  # str
org_role = ActorRole()  # ActorRole  (optional) (default to ACTOR_ROLE_UNSPECIFIED)

try:
    # CreateUser
    api_response: CreateUserResponse = client.user.create_user(
        email, password, full_name, org_role=org_role
    )
    print("The response of UserApi->create_user:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling UserApi->create_user: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_token**
> object  = delete_api_token()

DeleteAPIToken

Delete an API token by ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id_uuid | **str** | Unique object ID. | 

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

id_uuid = "id_uuid_example"  # str

try:
    # DeleteAPIToken
    api_response: object = client.user.delete_api_token(id_uuid)
    print("The response of UserApi->delete_api_token:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling UserApi->delete_api_token: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> object  = delete_user()

DeleteUser

Delete the user with the specified ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

user_id_uuid = "user_id_uuid_example"  # str

try:
    # DeleteUser
    api_response: object = client.user.delete_user(user_id_uuid)
    print("The response of UserApi->delete_user:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling UserApi->delete_user: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> GetUserResponse  = get_user()

GetUser

Return the user with the specified ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
user_id_uuid | **str** | Unique object ID. | 
oidc_id_token | **str** | ID of the OIDC provider token. | [optional] 

### Return type

[**GetUserResponse**](GetUserResponse.md)

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
from ri.apiclient.models.get_user_response import GetUserResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

user_id_uuid = "user_id_uuid_example"  # str
oidc_id_token = "oidc_id_token_example"  # str  (optional)

try:
    # GetUser
    api_response: GetUserResponse = client.user.get_user(
        user_id_uuid, oidc_id_token=oidc_id_token
    )
    print("The response of UserApi->get_user:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling UserApi->get_user: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_tokens**
> ListAPITokensResponse  = list_api_tokens()

ListAPITokens

List all API tokens for a Workspace.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page_size | **str** | The maximum number of API Token objects to return in a single page. | [optional] 
workspace_id_uuid | **str** | Unique object ID. | [optional] 
page_token | **str** | Specifies a page of the list returned by a ListAPITokens query. The ListAPITokens query returns a pageToken when there is more than one page of results. | [optional] 
first_page_query_token_type | **str** | Specifies the type of token. The query filters for results that match the specified type. | [optional] [default to TOKEN_TYPE_UNSPECIFIED]

### Return type

[**ListAPITokensResponse**](ListAPITokensResponse.md)

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
from ri.apiclient.models.list_api_tokens_response import ListAPITokensResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

page_size = "page_size_example"  # str  (optional)
workspace_id_uuid = "workspace_id_uuid_example"  # str  (optional)
page_token = "page_token_example"  # str  (optional)
first_page_query_token_type = (
    TOKEN_TYPE_UNSPECIFIED  # str  (optional) (default to TOKEN_TYPE_UNSPECIFIED)
)

try:
    # ListAPITokens
    api_response: ListAPITokensResponse = client.user.list_api_tokens(
        page_size=page_size,
        workspace_id_uuid=workspace_id_uuid,
        page_token=page_token,
        first_page_query_token_type=first_page_query_token_type,
    )
    print("The response of UserApi->list_api_tokens:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling UserApi->list_api_tokens: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_current_user_roles**
> ListCurrentUserRolesResponse  = list_current_user_roles()

ListCurrentUserRoles

Returns the list of roles of the logged in user.

### Parameters

This endpoint does not need any parameters.
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

### Return type

[**ListCurrentUserRolesResponse**](ListCurrentUserRolesResponse.md)

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
from ri.apiclient.models.list_current_user_roles_response import (
    ListCurrentUserRolesResponse,
)
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)


try:
    # ListCurrentUserRoles
    api_response: ListCurrentUserRolesResponse = client.user.list_current_user_roles()
    print("The response of UserApi->list_current_user_roles:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling UserApi->list_current_user_roles: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> ListUsersResponse  = list_users()

ListUsers

List all users.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page_token | **str** | Specifies a page of the list returned by a ListUsers query. The ListUsers query returns a pageToken when there is more than one page of results. Specify either this field or the firstPageQuery field. | [optional] 
page_size | **str** | The maximum number of User objects to return in a single page. | [optional] 

### Return type

[**ListUsersResponse**](ListUsersResponse.md)

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
from ri.apiclient.models.list_users_response import ListUsersResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

page_token = "page_token_example"  # str  (optional)
page_size = "page_size_example"  # str  (optional)

try:
    # ListUsers
    api_response: ListUsersResponse = client.user.list_users(
        page_token=page_token, page_size=page_size
    )
    print("The response of UserApi->list_users:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling UserApi->list_users: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> object  = reset_password()

ResetPassword

Reset the password of a user with the specified ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
user_id_uuid | **str** | Unique object ID. | 
user_id | **object** | Unique ID of an object in RIME. | [optional] 
old_password | **str** |  | [optional] 
new_password | **str** |  | 

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
from ri.apiclient.models.reset_password_request import ResetPasswordRequest
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

user_id_uuid = 'user_id_uuid_example'  # str 
user_id = {} # object  (optional)
old_password = ''  # str  (optional)
new_password = ''  # str 

try:
    # ResetPassword
    api_response: object = client.user.reset_password(user_id_uuid, user_id=user_id, old_password=old_password, new_password)
    print("The response of UserApi->reset_password:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling UserApi->reset_password: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agent_api_token**
> UpdateAgentAPITokenResponse  = update_agent_api_token()

UpdateAgentAPIToken

Refreshes an agent's API token.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
agent_id | [**ID**](ID.md) |  | 

### Return type

[**UpdateAgentAPITokenResponse**](UpdateAgentAPITokenResponse.md)

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
from ri.apiclient.models.update_agent_api_token_request import (
    UpdateAgentAPITokenRequest,
)
from ri.apiclient.models.update_agent_api_token_response import (
    UpdateAgentAPITokenResponse,
)
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

agent_id = ID()  # ID

try:
    # UpdateAgentAPIToken
    api_response: UpdateAgentAPITokenResponse = client.user.update_agent_api_token(
        agent_id
    )
    print("The response of UserApi->update_agent_api_token:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling UserApi->update_agent_api_token: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> object  = update_user()

UpdateUser

Update a user with the specified ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
user_id_uuid | **str** | Unique object ID. | 
user | [**UpdateUserRequestUser**](UpdateUserRequestUser.md) |  | [optional] 
mask | [**UserWriteMask**](UserWriteMask.md) |  | [optional] 

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
from ri.apiclient.models.update_user_request import UpdateUserRequest
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

user_id_uuid = "user_id_uuid_example"  # str
user = UpdateUserRequestUser()  # UpdateUserRequestUser  (optional)
mask = UserWriteMask()  # UserWriteMask  (optional)

try:
    # UpdateUser
    api_response: object = client.user.update_user(user_id_uuid, user=user, mask=mask)
    print("The response of UserApi->update_user:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling UserApi->update_user: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

