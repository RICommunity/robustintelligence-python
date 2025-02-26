# ri.apiclient.RIMEInfoApi

All URIs are relative to *http://&lt;platform-domain&gt;.rbst.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rime_info**](#get_rime_info) | **GET** /v1/rime-info | GetRIMEInfo

# **get_rime_info**
> GetRIMEInfoResponse  = get_rime_info()

GetRIMEInfo

Returns information about the Robust Intelligence cluster you are querying.

### Parameters

This endpoint does not need any parameters.
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

### Return type

[**GetRIMEInfoResponse**](GetRIMEInfoResponse.md)

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
from ri.apiclient.models.get_rime_info_response import GetRIMEInfoResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)


try:
    # GetRIMEInfo
    api_response: GetRIMEInfoResponse = client.RIMEInfoApi.get_rime_info()
    print("The response of RIMEInfoApi->get_rime_info:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling RIMEInfoApi->get_rime_info: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

