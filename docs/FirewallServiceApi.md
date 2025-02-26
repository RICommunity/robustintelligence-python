# ri.apiclient.FirewallServiceApi

All URIs are relative to *http://&lt;platform-domain&gt;.rbst.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_firewall**](#create_firewall) | **POST** /v1/firewall | CreateFirewall
[**delete_firewall**](#delete_firewall) | **DELETE** /v1/firewall/{firewallId.uuid} | DeleteFirewall
[**get_firewall**](#get_firewall) | **GET** /v1/firewall/{firewallId.uuid} | GetFirewall
[**get_url**](#get_url) | **GET** /v1-beta/firewall/{firewallId.uuid}/url | GetURL
[**update_firewall**](#update_firewall) | **PUT** /v1/firewall/{firewall.firewallId.uuid} | UpdateFirewall

# **create_firewall**
> CreateFirewallResponse  = create_firewall()

CreateFirewall

Creates a firewall with the required fields. This service is deprecated in Robust Intelligence v2.2 and will not be supported from v2.4.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id | [**ID**](ID.md) |  | 
model_id | [**ID**](ID.md) |  | 
bin_size | **str** | Duration of each bin size of continuous tests. | 
ref_data_id | **str** | Uniquely specifies a reference data set. | 
scheduled_ct_parameters | [**ScheduledCTParameters**](ScheduledCTParameters.md) |  | [optional] 

### Return type

[**CreateFirewallResponse**](CreateFirewallResponse.md)

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
from ri.apiclient.models.create_firewall_request import CreateFirewallRequest
from ri.apiclient.models.create_firewall_response import CreateFirewallResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

project_id = ID()  # ID 
model_id = ID()  # ID 
bin_size = ''  # str 
ref_data_id = ''  # str 
scheduled_ct_parameters = ScheduledCTParameters()  # ScheduledCTParameters  (optional)

try:
    # CreateFirewall
    api_response: CreateFirewallResponse = client.FirewallServiceApi.create_firewall(project_id, model_id, bin_size, ref_data_id, scheduled_ct_parameters=scheduled_ct_parameters)
    print("The response of FirewallServiceApi->create_firewall:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling FirewallServiceApi->create_firewall: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_firewall**
> object  = delete_firewall()

DeleteFirewall

Deletes the firewall with the specified ID. This service is deprecated in Robust Intelligence v2.2 and will not be supported from v2.4.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
firewall_id_uuid | **str** | Unique object ID. | 

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

firewall_id_uuid = 'firewall_id_uuid_example'  # str 

try:
    # DeleteFirewall
    api_response: object = client.FirewallServiceApi.delete_firewall(firewall_id_uuid)
    print("The response of FirewallServiceApi->delete_firewall:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling FirewallServiceApi->delete_firewall: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firewall**
> GetFirewallResponse  = get_firewall()

GetFirewall

Gets the firewall that matches the specified ID. This service is deprecated in Robust Intelligence v2.2 and will not be supported from v2.4.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
firewall_id_uuid | **str** | Unique object ID. | 

### Return type

[**GetFirewallResponse**](GetFirewallResponse.md)

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
from ri.apiclient.models.get_firewall_response import GetFirewallResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

firewall_id_uuid = 'firewall_id_uuid_example'  # str 

try:
    # GetFirewall
    api_response: GetFirewallResponse = client.FirewallServiceApi.get_firewall(firewall_id_uuid)
    print("The response of FirewallServiceApi->get_firewall:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling FirewallServiceApi->get_firewall: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_url**
> GetURLResponse  = get_url()

GetURL

Returns the URL for the specified Firewall in the Robust Intelligence web application. This service is deprecated in Robust Intelligence v2.2 and will not be supported from v2.4.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
firewall_id_uuid | **str** | Unique object ID. | 

### Return type

[**GetURLResponse**](GetURLResponse.md)

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
from ri.apiclient.models.get_url_response import GetURLResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

firewall_id_uuid = 'firewall_id_uuid_example'  # str 

try:
    # GetURL
    api_response: GetURLResponse = client.FirewallServiceApi.get_url(firewall_id_uuid)
    print("The response of FirewallServiceApi->get_url:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling FirewallServiceApi->get_url: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_firewall**
> UpdateFirewallResponse  = update_firewall()

UpdateFirewall

Updates a firewall's editable fields. This service is deprecated in Robust Intelligence v2.2 and will not be supported from v2.4.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
firewall_firewall_id_uuid | **str** | Unique object ID. | 
firewall_id | [**ID**](ID.md) |  | 
firewall | [**UpdateFirewallRequestFirewall**](UpdateFirewallRequestFirewall.md) |  | [optional] 
mask | **str** | Field mask specifies which fields of the firewall to update. | [optional] 

### Return type

[**UpdateFirewallResponse**](UpdateFirewallResponse.md)

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
from ri.apiclient.models.update_firewall_request import UpdateFirewallRequest
from ri.apiclient.models.update_firewall_response import UpdateFirewallResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

firewall_firewall_id_uuid = 'firewall_firewall_id_uuid_example'  # str 
firewall_id = ID()  # ID 
firewall = UpdateFirewallRequestFirewall()  # UpdateFirewallRequestFirewall  (optional)
mask = ''  # str  (optional)

try:
    # UpdateFirewall
    api_response: UpdateFirewallResponse = client.FirewallServiceApi.update_firewall(firewall_firewall_id_uuid, firewall_id, firewall=firewall, mask=mask)
    print("The response of FirewallServiceApi->update_firewall:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling FirewallServiceApi->update_firewall: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

