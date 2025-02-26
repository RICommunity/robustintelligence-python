# ri.apiclient.IntegrationServiceApi

All URIs are relative to *http://&lt;platform-domain&gt;.rbst.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configure_integration**](#configure_integration) | **POST** /v1-beta/integrations/{integrationId.uuid} | ConfigureIntegration
[**create_integration**](#create_integration) | **POST** /v1-beta/integrations | CreateIntegration
[**delete_integration**](#delete_integration) | **DELETE** /v1-beta/integrations/{integrationId.uuid} | DeleteIntegration
[**get_integration**](#get_integration) | **GET** /v1-beta/integrations/{integrationId.uuid} | GetIntegration
[**list_workspace_integrations**](#list_workspace_integrations) | **GET** /v1-beta/integrations/workspace/{workspaceId.uuid} | ListWorkspaceIntegrations
[**update_integration**](#update_integration) | **PUT** /v1-beta/integrations/{integration.id.uuid} | UpdateIntegration

# **configure_integration**
> ConfigureIntegrationResponse  = configure_integration()

ConfigureIntegration

Configures the Integration with specified ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
integration_id_uuid | **str** | Unique object ID. | 
integration_id | **object** | Unique ID of an object in RIME. | [optional] 
variables | [**List[ConfigureIntegrationRequestIntegrationVariable]**](List.md) |  | 

### Return type

[**ConfigureIntegrationResponse**](ConfigureIntegrationResponse.md)

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
from ri.apiclient.models.configure_integration_request import ConfigureIntegrationRequest
from ri.apiclient.models.configure_integration_response import ConfigureIntegrationResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

integration_id_uuid = 'integration_id_uuid_example'  # str 
integration_id = ri.apiclient.models.integration_id.integrationId()  # object  (optional)
variables = List[ConfigureIntegrationRequestIntegrationVariable]()  # List[ConfigureIntegrationRequestIntegrationVariable] 

try:
    # ConfigureIntegration
    api_response: ConfigureIntegrationResponse = client.IntegrationServiceApi.configure_integration(integration_id_uuid, integration_id=integration_id, variables)
    print("The response of IntegrationServiceApi->configure_integration:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling IntegrationServiceApi->configure_integration: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_integration**
> CreateIntegrationResponse  = create_integration()

CreateIntegration

Creates a new Integration.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
integration | [**Integration**](Integration.md) |  | [optional] 

### Return type

[**CreateIntegrationResponse**](CreateIntegrationResponse.md)

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
from ri.apiclient.models.create_integration_request import CreateIntegrationRequest
from ri.apiclient.models.create_integration_response import CreateIntegrationResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

integration = Integration()  # Integration  (optional)

try:
    # CreateIntegration
    api_response: CreateIntegrationResponse = client.IntegrationServiceApi.create_integration(integration=integration)
    print("The response of IntegrationServiceApi->create_integration:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling IntegrationServiceApi->create_integration: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_integration**
> object  = delete_integration()

DeleteIntegration

Delete an Integration by specified ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
integration_id_uuid | **str** | Unique object ID. | 

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

integration_id_uuid = 'integration_id_uuid_example'  # str 

try:
    # DeleteIntegration
    api_response: object = client.IntegrationServiceApi.delete_integration(integration_id_uuid)
    print("The response of IntegrationServiceApi->delete_integration:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling IntegrationServiceApi->delete_integration: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integration**
> GetIntegrationResponse  = get_integration()

GetIntegration

Returns an Integration by specified ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
integration_id_uuid | **str** | Unique object ID. | 

### Return type

[**GetIntegrationResponse**](GetIntegrationResponse.md)

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
from ri.apiclient.models.get_integration_response import GetIntegrationResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

integration_id_uuid = 'integration_id_uuid_example'  # str 

try:
    # GetIntegration
    api_response: GetIntegrationResponse = client.IntegrationServiceApi.get_integration(integration_id_uuid)
    print("The response of IntegrationServiceApi->get_integration:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling IntegrationServiceApi->get_integration: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workspace_integrations**
> ListWorkspaceIntegrationsResponse  = list_workspace_integrations()

ListWorkspaceIntegrations

List all Integrations for the Workspace with specified ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
workspace_id_uuid | **str** | Unique object ID. | 

### Return type

[**ListWorkspaceIntegrationsResponse**](ListWorkspaceIntegrationsResponse.md)

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
from ri.apiclient.models.list_workspace_integrations_response import ListWorkspaceIntegrationsResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

workspace_id_uuid = 'workspace_id_uuid_example'  # str 

try:
    # ListWorkspaceIntegrations
    api_response: ListWorkspaceIntegrationsResponse = client.IntegrationServiceApi.list_workspace_integrations(workspace_id_uuid)
    print("The response of IntegrationServiceApi->list_workspace_integrations:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling IntegrationServiceApi->list_workspace_integrations: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_integration**
> UpdateIntegrationResponse  = update_integration()

UpdateIntegration

Update the Integration with specified ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
integration_id_uuid | **str** | Unique object ID. | 
integration | [**UpdateIntegrationRequestIntegration**](UpdateIntegrationRequestIntegration.md) |  | [optional] 
mask | **str** |  | [optional] 

### Return type

[**UpdateIntegrationResponse**](UpdateIntegrationResponse.md)

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
from ri.apiclient.models.update_integration_request import UpdateIntegrationRequest
from ri.apiclient.models.update_integration_response import UpdateIntegrationResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

integration_id_uuid = 'integration_id_uuid_example'  # str 
integration = UpdateIntegrationRequestIntegration()  # UpdateIntegrationRequestIntegration  (optional)
mask = ''  # str  (optional)

try:
    # UpdateIntegration
    api_response: UpdateIntegrationResponse = client.IntegrationServiceApi.update_integration(integration_id_uuid, integration=integration, mask=mask)
    print("The response of IntegrationServiceApi->update_integration:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling IntegrationServiceApi->update_integration: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

