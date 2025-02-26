# ri.apiclient.FeatureFlagApi

All URIs are relative to *http://&lt;platform-domain&gt;.rbst.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_limit_status**](#get_limit_status) | **GET** /v1/feature-flags/{customerName}/limits/{limit} | GetLimitStatus
[**list_enabled_features**](#list_enabled_features) | **GET** /v1/feature-flags/{customerName}/features | ListEnabledFeatures

# **get_limit_status**
> GetLimitStatusResponse  = get_limit_status()

GetLimitStatus

Returns the status of a specified limit in this deployment's license.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
customer_name | **str** | Name of the customer to query. | 
limit | **str** | Specifies which limit to query. | 

### Return type

[**GetLimitStatusResponse**](GetLimitStatusResponse.md)

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
from ri.apiclient.models.get_limit_status_response import GetLimitStatusResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

customer_name = 'customer_name_example'  # str 
limit = 'limit_example'  # str 

try:
    # GetLimitStatus
    api_response: GetLimitStatusResponse = client.FeatureFlagApi.get_limit_status(customer_name, limit)
    print("The response of FeatureFlagApi->get_limit_status:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling FeatureFlagApi->get_limit_status: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_enabled_features**
> ListEnabledFeaturesResponse  = list_enabled_features()

ListEnabledFeatures

Returns all features enabled in license for a customer.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
customer_name | **str** | Name of the customer to query. | 

### Return type

[**ListEnabledFeaturesResponse**](ListEnabledFeaturesResponse.md)

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
from ri.apiclient.models.list_enabled_features_response import ListEnabledFeaturesResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

customer_name = 'customer_name_example'  # str 

try:
    # ListEnabledFeatures
    api_response: ListEnabledFeaturesResponse = client.FeatureFlagApi.list_enabled_features(customer_name)
    print("The response of FeatureFlagApi->list_enabled_features:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling FeatureFlagApi->list_enabled_features: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

