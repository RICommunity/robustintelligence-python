# ri.apiclient.CustomerManagedKeyServiceApi

All URIs are relative to *http://&lt;platform-domain&gt;.rbst.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer_managed_key**](#create_customer_managed_key) | **POST** /v1-beta/customer-managed-key | CreateCustomerManagedKey
[**delete_customer_managed_key**](#delete_customer_managed_key) | **DELETE** /v1-beta/customer-managed-key | DeleteCustomerManagedKey
[**get_customer_managed_key**](#get_customer_managed_key) | **GET** /v1-beta/customer-managed-key | GetCustomerManagedKey
[**get_key_status**](#get_key_status) | **GET** /v1-beta/customer-managed-key/status | GetKeyStatus

# **create_customer_managed_key**
> CreateCustomerManagedKeyResponse  = create_customer_managed_key()

CreateCustomerManagedKey

Creates a new customer managed key. At most one key can exist per deployment.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
cmk_config | [**CustomerManagedKeyConfig**](CustomerManagedKeyConfig.md) |  | 

### Return type

[**CreateCustomerManagedKeyResponse**](CreateCustomerManagedKeyResponse.md)

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
from ri.apiclient.models.create_customer_managed_key_request import CreateCustomerManagedKeyRequest
from ri.apiclient.models.create_customer_managed_key_response import CreateCustomerManagedKeyResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

cmk_config = CustomerManagedKeyConfig()  # CustomerManagedKeyConfig 

try:
    # CreateCustomerManagedKey
    api_response: CreateCustomerManagedKeyResponse = client.CustomerManagedKeyServiceApi.create_customer_managed_key(cmk_config)
    print("The response of CustomerManagedKeyServiceApi->create_customer_managed_key:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling CustomerManagedKeyServiceApi->create_customer_managed_key: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer_managed_key**
> object  = delete_customer_managed_key()

DeleteCustomerManagedKey

Delete the customer managed key.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
cmk_config_key_provider | **str** |  - KEY_PROVIDER_AWS_KMS: AWS Key Management Service | [default to KEY_PROVIDER_UNSPECIFIED]
cmk_config_kms_key_arn | **str** | The ARN of the AWS KMS key to use as the customer managed key. | 

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

cmk_config_key_provider = KEY_PROVIDER_UNSPECIFIED  # str  (default to KEY_PROVIDER_UNSPECIFIED)
cmk_config_kms_key_arn = 'cmk_config_kms_key_arn_example'  # str 

try:
    # DeleteCustomerManagedKey
    api_response: object = client.CustomerManagedKeyServiceApi.delete_customer_managed_key(cmk_config_key_provider, cmk_config_kms_key_arn)
    print("The response of CustomerManagedKeyServiceApi->delete_customer_managed_key:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling CustomerManagedKeyServiceApi->delete_customer_managed_key: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_managed_key**
> GetCustomerManagedKeyResponse  = get_customer_managed_key()

GetCustomerManagedKey

Returns a customer managed key if one has been created.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
cmk_config_key_provider | **str** |  - KEY_PROVIDER_AWS_KMS: AWS Key Management Service | [default to KEY_PROVIDER_UNSPECIFIED]
cmk_config_kms_key_arn | **str** | The ARN of the AWS KMS key to use as the customer managed key. | 

### Return type

[**GetCustomerManagedKeyResponse**](GetCustomerManagedKeyResponse.md)

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
from ri.apiclient.models.get_customer_managed_key_response import GetCustomerManagedKeyResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

cmk_config_key_provider = KEY_PROVIDER_UNSPECIFIED  # str  (default to KEY_PROVIDER_UNSPECIFIED)
cmk_config_kms_key_arn = 'cmk_config_kms_key_arn_example'  # str 

try:
    # GetCustomerManagedKey
    api_response: GetCustomerManagedKeyResponse = client.CustomerManagedKeyServiceApi.get_customer_managed_key(cmk_config_key_provider, cmk_config_kms_key_arn)
    print("The response of CustomerManagedKeyServiceApi->get_customer_managed_key:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling CustomerManagedKeyServiceApi->get_customer_managed_key: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_key_status**
> GetKeyStatusResponse  = get_key_status()

GetKeyStatus

Return whether the customer managed key is active or revoked.

### Parameters

This endpoint does not need any parameters.
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

### Return type

[**GetKeyStatusResponse**](GetKeyStatusResponse.md)

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
from ri.apiclient.models.get_key_status_response import GetKeyStatusResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)


try:
    # GetKeyStatus
    api_response: GetKeyStatusResponse = client.CustomerManagedKeyServiceApi.get_key_status()
    print("The response of CustomerManagedKeyServiceApi->get_key_status:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling CustomerManagedKeyServiceApi->get_key_status: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

