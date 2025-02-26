# ri.apiclient.FileUploadApi

All URIs are relative to *http://&lt;platform-domain&gt;.rbst.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_uploaded_file_url**](#delete_uploaded_file_url) | **DELETE** /v1-beta/datasets/upload-url | DeleteUploadedFileURL
[**get_dataset_file_upload_url**](#get_dataset_file_upload_url) | **GET** /v1-beta/datasets/upload-url | GetDatasetFileUploadURL
[**get_dataset_file_upload_url2**](#get_dataset_file_upload_url2) | **POST** /v1-beta/datasets/upload-url | GetDatasetFileUploadURL
[**get_model_directory_upload_urls**](#get_model_directory_upload_urls) | **GET** /v1-beta/models/upload-url | GetModelDirectoryUploadURL
[**get_model_directory_upload_urls2**](#get_model_directory_upload_urls2) | **POST** /v1-beta/models/upload-url | GetModelDirectoryUploadURL
[**list_uploaded_file_urls**](#list_uploaded_file_urls) | **GET** /v1-beta/uploaded-file-urls | ListUploadedFileURLs

# **delete_uploaded_file_url**
> object  = delete_uploaded_file_url()

DeleteUploadedFileURL

Deletes the uploaded dataset at the specified URL from the blob store.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
uploaded_url | **str** | URL of the uploaded file to delete. | 

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

uploaded_url = "uploaded_url_example"  # str

try:
    # DeleteUploadedFileURL
    api_response: object = client.file_upload.delete_uploaded_file_url(uploaded_url)
    print("The response of FileUploadApi->delete_uploaded_file_url:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling FileUploadApi->delete_uploaded_file_url: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_file_upload_url**
> GetDatasetFileUploadURLResponse  = get_dataset_file_upload_url()

GetDatasetFileUploadURL

Returns a pre-signed upload URL for a dataset.  File uploading is not currently supported in a Cloud deployment. Please use an external data source instead.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
file_name | **str** | Path of dataset file on the local file system. | 
upload_path | **str** | Specify a path in the blob store to use for data uploads. | [optional] 

### Return type

[**GetDatasetFileUploadURLResponse**](GetDatasetFileUploadURLResponse.md)

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
from ri.apiclient.models.get_dataset_file_upload_url_response import (
    GetDatasetFileUploadURLResponse,
)
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

file_name = "file_name_example"  # str
upload_path = "upload_path_example"  # str  (optional)

try:
    # GetDatasetFileUploadURL
    api_response: GetDatasetFileUploadURLResponse = (
        client.file_upload.get_dataset_file_upload_url(
            file_name, upload_path=upload_path
        )
    )
    print("The response of FileUploadApi->get_dataset_file_upload_url:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling FileUploadApi->get_dataset_file_upload_url: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_file_upload_url2**
> GetDatasetFileUploadURLResponse  = get_dataset_file_upload_url2()

GetDatasetFileUploadURL

Returns a pre-signed upload URL for a dataset.  File uploading is not currently supported in a Cloud deployment. Please use an external data source instead.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
file_name | **str** | Path of dataset file on the local file system. | 
upload_path | **str** | Specify a path in the blob store to use for data uploads. | [optional] 

### Return type

[**GetDatasetFileUploadURLResponse**](GetDatasetFileUploadURLResponse.md)

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
from ri.apiclient.models.get_dataset_file_upload_url_request import (
    GetDatasetFileUploadURLRequest,
)
from ri.apiclient.models.get_dataset_file_upload_url_response import (
    GetDatasetFileUploadURLResponse,
)
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

file_name = ""  # str
upload_path = ""  # str  (optional)

try:
    # GetDatasetFileUploadURL
    api_response: GetDatasetFileUploadURLResponse = (
        client.file_upload.get_dataset_file_upload_url2(
            file_name, upload_path=upload_path
        )
    )
    print("The response of FileUploadApi->get_dataset_file_upload_url2:\n")
    pprint(api_response)

except ApiException as e:
    print(
        "Exception when calling FileUploadApi->get_dataset_file_upload_url2: %s\n" % e
    )
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_directory_upload_urls**
> GetModelDirectoryUploadURLsResponse  = get_model_directory_upload_urls()

GetModelDirectoryUploadURL

Returns a pre-signed upload URL for a model directory.  File uploading is not currently supported in a Cloud deployment. Please use an external data source instead.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
directory_name | **str** | Path of model directory on local file system. | 
relative_file_paths | [**List[str]**](str.md) | Array of relative paths from the model directory to model files. | 
upload_path | **str** | Specify a path in the blob store to which the model will be uploaded. | [optional] 

### Return type

[**GetModelDirectoryUploadURLsResponse**](GetModelDirectoryUploadURLsResponse.md)

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
from ri.apiclient.models.get_model_directory_upload_urls_response import (
    GetModelDirectoryUploadURLsResponse,
)
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

directory_name = "directory_name_example"  # str
relative_file_paths = ["relative_file_paths_example"]  # List[str]
upload_path = "upload_path_example"  # str  (optional)

try:
    # GetModelDirectoryUploadURL
    api_response: GetModelDirectoryUploadURLsResponse = (
        client.file_upload.get_model_directory_upload_urls(
            directory_name, relative_file_paths, upload_path=upload_path
        )
    )
    print("The response of FileUploadApi->get_model_directory_upload_urls:\n")
    pprint(api_response)

except ApiException as e:
    print(
        "Exception when calling FileUploadApi->get_model_directory_upload_urls: %s\n"
        % e
    )
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_directory_upload_urls2**
> GetModelDirectoryUploadURLsResponse  = get_model_directory_upload_urls2()

GetModelDirectoryUploadURL

Returns a pre-signed upload URL for a model directory.  File uploading is not currently supported in a Cloud deployment. Please use an external data source instead.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
directory_name | **str** | Path of model directory on local file system. | 
relative_file_paths | **List[str]** | Array of relative paths from the model directory to model files. | 
upload_path | **str** | Specify a path in the blob store to which the model will be uploaded. | [optional] 

### Return type

[**GetModelDirectoryUploadURLsResponse**](GetModelDirectoryUploadURLsResponse.md)

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
from ri.apiclient.models.get_model_directory_upload_urls_request import (
    GetModelDirectoryUploadURLsRequest,
)
from ri.apiclient.models.get_model_directory_upload_urls_response import (
    GetModelDirectoryUploadURLsResponse,
)
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

directory_name = ""  # str
relative_file_paths = [""]  # List[str]
upload_path = ""  # str  (optional)

try:
    # GetModelDirectoryUploadURL
    api_response: GetModelDirectoryUploadURLsResponse = (
        client.file_upload.get_model_directory_upload_urls2(
            directory_name, relative_file_paths, upload_path=upload_path
        )
    )
    print("The response of FileUploadApi->get_model_directory_upload_urls2:\n")
    pprint(api_response)

except ApiException as e:
    print(
        "Exception when calling FileUploadApi->get_model_directory_upload_urls2: %s\n"
        % e
    )
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_uploaded_file_urls**
> ListUploadedFileURLsResponse  = list_uploaded_file_urls()

ListUploadedFileURLs

List up to 1000 blob store URLs for uploaded files.  File uploading is not currently supported in a Cloud deployment. Please use an external data source instead.

### Parameters

This endpoint does not need any parameters.
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

### Return type

[**ListUploadedFileURLsResponse**](ListUploadedFileURLsResponse.md)

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
from ri.apiclient.models.list_uploaded_file_urls_response import (
    ListUploadedFileURLsResponse,
)
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)


try:
    # ListUploadedFileURLs
    api_response: ListUploadedFileURLsResponse = (
        client.file_upload.list_uploaded_file_urls()
    )
    print("The response of FileUploadApi->list_uploaded_file_urls:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling FileUploadApi->list_uploaded_file_urls: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

