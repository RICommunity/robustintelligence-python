# ri.apiclient.ImageRegistryApi

All URIs are relative to *http://&lt;platform-domain&gt;.rbst.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_image**](#create_image) | **POST** /v1/images | CreateImage
[**delete_image**](#delete_image) | **DELETE** /v1/images/{name} | DeleteImage
[**get_image**](#get_image) | **GET** /v1/images/{name} | GetImage
[**list_images**](#list_images) | **GET** /v1/images | ListImages
[**list_images2**](#list_images2) | **POST** /v1/images/list | ListImages

# **create_image**
> CreateImageResponse  = create_image()

CreateImage

Creates a new Managed Image with a unique name.  Managed images are not currently supported in a Cloud deployment. Please reach out to Robust Intelligence for support if this functionality is required for your deployment.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | **str** | Name of the Managed Image.  Name must match the regexp described in managed_image.proto  for &#x60;ManagedImage.name&#x60;. | 
pip_requirements | [**List[PipRequirement]**](List.md) | List of &#x60;pip&#x60; requirements that specify the customization used for this Image. | 
package_requirements | [**List[PackageRequirement]**](List.md) | List of system requirements that specify the customization used for this Image. | [optional] 
python_version | **str** | The version of the Python interpreter to use. | [optional] 

### Return type

[**CreateImageResponse**](CreateImageResponse.md)

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
from ri.apiclient.models.create_image_request import CreateImageRequest
from ri.apiclient.models.create_image_response import CreateImageResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

name = ''  # str 
pip_requirements = List[PipRequirement]()  # List[PipRequirement] 
package_requirements = List[PackageRequirement]()  # List[PackageRequirement]  (optional)
python_version = ''  # str  (optional)

try:
    # CreateImage
    api_response: CreateImageResponse = client.ImageRegistryApi.create_image(name, pip_requirements, package_requirements=package_requirements, python_version=python_version)
    print("The response of ImageRegistryApi->create_image:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ImageRegistryApi->create_image: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_image**
> object  = delete_image()

DeleteImage

Deletes a specified Managed Image.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | **str** | Name of existing Managed Image to delete.  This name must match the regexp described in managed_image.proto  for &#x60;ManagedImage.name&#x60;. | 

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

name = 'name_example'  # str 

try:
    # DeleteImage
    api_response: object = client.ImageRegistryApi.delete_image(name)
    print("The response of ImageRegistryApi->delete_image:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ImageRegistryApi->delete_image: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image**
> GetImageResponse  = get_image()

GetImage

Returns the definition of a specified Managed Image.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | **str** | Name of the existing Managed Image.  Name must match the regexp described in managed_image.proto  for &#x60;ManagedImage.name&#x60;. | 

### Return type

[**GetImageResponse**](GetImageResponse.md)

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
from ri.apiclient.models.get_image_response import GetImageResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

name = 'name_example'  # str 

try:
    # GetImage
    api_response: GetImageResponse = client.ImageRegistryApi.get_image(name)
    print("The response of ImageRegistryApi->get_image:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ImageRegistryApi->get_image: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_images**
> ListImagesResponse  = list_images()

ListImages

List all Managed Images that match a specified set of constraints.  #### Python pagination example:  ```python all_objects = [] # Required for authentication to all methods in the API. headers = {\"rime-api-key\": \"INSERT_API_TOKEN\"} # TODO page_token = \"\" # Initialize query parameters in a dictionary params = {\"INSERT_QUERY_PARAMETER\": \"INSERT_QUERY_VALUE\"} # TODO # Make requests until all results have been returned. while True:     # If the page_token from a previous response is not empty, we need to specify this     # token as a parameter to the next request in order to return the next page.     if page_token != \"\":         params = {\"page_token\": page_token}     res = requests.get(\"INSERT_METHOD_URI\", params=params, headers=headers) # TODO     if res.status_code != 200 :         raise ValueError(res)     res_json = res.json()     all_objects.extend(res_json['INSERT_OBJECT_KEY']) # TODO     page_token = res_json['nextPageToken']     # If all results have been returned, res_json['hasMore'] is false.     if not res_json[\"hasMore\"]:         break ```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page_token | **str** | Specifies a page of the list returned by a ListImages query. The ListImages query returns a pageToken when there is more than one page of results. | [optional] 
page_size | **str** | The maximum number of Image objects to return in a single page. | [optional] 

### Return type

[**ListImagesResponse**](ListImagesResponse.md)

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
from ri.apiclient.models.list_images_response import ListImagesResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

page_token = 'page_token_example'  # str  (optional)
page_size = 'page_size_example'  # str  (optional)

try:
    # ListImages
    api_response: ListImagesResponse = client.ImageRegistryApi.list_images(page_token=page_token, page_size=page_size)
    print("The response of ImageRegistryApi->list_images:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ImageRegistryApi->list_images: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_images2**
> ListImagesResponse  = list_images2()

ListImages

List all Managed Images that match a specified set of constraints.  #### Python pagination example:  ```python all_objects = [] # Required for authentication to all methods in the API. headers = {\"rime-api-key\": \"INSERT_API_TOKEN\"} # TODO page_token = \"\" # Initialize query parameters in a dictionary params = {\"INSERT_QUERY_PARAMETER\": \"INSERT_QUERY_VALUE\"} # TODO # Make requests until all results have been returned. while True:     # If the page_token from a previous response is not empty, we need to specify this     # token as a parameter to the next request in order to return the next page.     if page_token != \"\":         params = {\"page_token\": page_token}     res = requests.get(\"INSERT_METHOD_URI\", params=params, headers=headers) # TODO     if res.status_code != 200 :         raise ValueError(res)     res_json = res.json()     all_objects.extend(res_json['INSERT_OBJECT_KEY']) # TODO     page_token = res_json['nextPageToken']     # If all results have been returned, res_json['hasMore'] is false.     if not res_json[\"hasMore\"]:         break ```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page_token | **str** | Specifies a page of the list returned by a ListImages query. The ListImages query returns a pageToken when there is more than one page of results. | [optional] 
page_size | **str** | The maximum number of Image objects to return in a single page. | [optional] 
pip_libraries | [**List[PipLibraryFilter]**](List.md) | Optional. Filters the list for libraries that are installed on the Managed Image. The filter is only active when the list is not empty. When this filter is specified, do not include a pageToken field in the request. | [optional] 

### Return type

[**ListImagesResponse**](ListImagesResponse.md)

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
from ri.apiclient.models.list_images_request import ListImagesRequest
from ri.apiclient.models.list_images_response import ListImagesResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

page_token = ''  # str  (optional)
page_size = ''  # str  (optional)
pip_libraries = List[PipLibraryFilter]()  # List[PipLibraryFilter]  (optional)

try:
    # ListImages
    api_response: ListImagesResponse = client.ImageRegistryApi.list_images2(page_token=page_token, page_size=page_size, pip_libraries=pip_libraries)
    print("The response of ImageRegistryApi->list_images2:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ImageRegistryApi->list_images2: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

