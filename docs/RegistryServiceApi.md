# ri.apiclient.RegistryServiceApi

All URIs are relative to *http://&lt;platform-domain&gt;.rbst.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_dataset**](#delete_dataset) | **DELETE** /v1/registry/dataset/{datasetId} | DeleteDataset
[**delete_model**](#delete_model) | **DELETE** /v1/registry/model/{modelId.uuid} | DeleteModel
[**delete_prediction_set**](#delete_prediction_set) | **DELETE** /v1/registry/prediction/{modelId.uuid}/{datasetId} | DeletePredictionSet
[**get_dataset**](#get_dataset) | **GET** /v1/registry/dataset | GetDataset
[**get_model**](#get_model) | **GET** /v1/registry/model | GetModel
[**get_prediction_set**](#get_prediction_set) | **GET** /v1/registry/prediction/{modelId.uuid}/{datasetId} | GetPredictionSet
[**list_datasets**](#list_datasets) | **GET** /v1/registry/{projectId.uuid}/dataset | ListDatasets
[**list_models**](#list_models) | **GET** /v1/registry/{projectId.uuid}/model | ListModels
[**list_prediction_sets**](#list_prediction_sets) | **GET** /v1/registry/{projectId.uuid}/prediction | ListPredictionSets
[**register_dataset**](#register_dataset) | **POST** /v1/registry/{projectId.uuid}/dataset | RegisterDataset
[**register_model**](#register_model) | **POST** /v1/registry/{projectId.uuid}/model | RegisterModel
[**register_prediction_set**](#register_prediction_set) | **POST** /v1/registry/{projectId.uuid}/model/{modelId.uuid}/dataset/{datasetId}/prediction | RegisterPredictionSet

# **delete_dataset**
> object  = delete_dataset()

DeleteDataset

Delete a Dataset from the Registry.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dataset_id | **str** | Uniquely specifies a Dataset. | 

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

dataset_id = 'dataset_id_example'  # str 

try:
    # DeleteDataset
    api_response: object = client.RegistryServiceApi.delete_dataset(dataset_id)
    print("The response of RegistryServiceApi->delete_dataset:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling RegistryServiceApi->delete_dataset: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_model**
> object  = delete_model()

DeleteModel

Delete a Model from the Registry.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
model_id_uuid | **str** | Unique object ID. | 

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

model_id_uuid = 'model_id_uuid_example'  # str 

try:
    # DeleteModel
    api_response: object = client.RegistryServiceApi.delete_model(model_id_uuid)
    print("The response of RegistryServiceApi->delete_model:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling RegistryServiceApi->delete_model: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_prediction_set**
> object  = delete_prediction_set()

DeletePredictionSet

Delete the Prediction set corresponding to a specified Model and Dataset.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
model_id_uuid | **str** | Unique object ID. | 
dataset_id | **str** | Uniquely specifies a Dataset. | 

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

model_id_uuid = 'model_id_uuid_example'  # str 
dataset_id = 'dataset_id_example'  # str 

try:
    # DeletePredictionSet
    api_response: object = client.RegistryServiceApi.delete_prediction_set(model_id_uuid, dataset_id)
    print("The response of RegistryServiceApi->delete_prediction_set:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling RegistryServiceApi->delete_prediction_set: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset**
> GetDatasetResponse  = get_dataset()

GetDataset

Returns information about a registered Dataset. Allows for searching by ID or name.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dataset_id | **str** | Uniquely specifies a Dataset. | [optional] 
dataset_name | **str** | Unique name of a Dataset. | [optional] 

### Return type

[**GetDatasetResponse**](GetDatasetResponse.md)

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
from ri.apiclient.models.get_dataset_response import GetDatasetResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

dataset_id = 'dataset_id_example'  # str  (optional)
dataset_name = 'dataset_name_example'  # str  (optional)

try:
    # GetDataset
    api_response: GetDatasetResponse = client.RegistryServiceApi.get_dataset(dataset_id=dataset_id, dataset_name=dataset_name)
    print("The response of RegistryServiceApi->get_dataset:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling RegistryServiceApi->get_dataset: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model**
> GetModelResponse  = get_model()

GetModel

Returns information about a registered Model. Allows for searching by ID or name.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
model_id_uuid | **str** | Unique object ID. | [optional] 
model_name | **str** | Unique name of a Model. | [optional] 

### Return type

[**GetModelResponse**](GetModelResponse.md)

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
from ri.apiclient.models.get_model_response import GetModelResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

model_id_uuid = 'model_id_uuid_example'  # str  (optional)
model_name = 'model_name_example'  # str  (optional)

try:
    # GetModel
    api_response: GetModelResponse = client.RegistryServiceApi.get_model(model_id_uuid=model_id_uuid, model_name=model_name)
    print("The response of RegistryServiceApi->get_model:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling RegistryServiceApi->get_model: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prediction_set**
> GetPredictionSetResponse  = get_prediction_set()

GetPredictionSet

Returns information about a registered Prediction set.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
model_id_uuid | **str** | Unique object ID. | 
dataset_id | **str** | Uniquely specifies a Dataset. | 

### Return type

[**GetPredictionSetResponse**](GetPredictionSetResponse.md)

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
from ri.apiclient.models.get_prediction_set_response import GetPredictionSetResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

model_id_uuid = 'model_id_uuid_example'  # str 
dataset_id = 'dataset_id_example'  # str 

try:
    # GetPredictionSet
    api_response: GetPredictionSetResponse = client.RegistryServiceApi.get_prediction_set(model_id_uuid, dataset_id)
    print("The response of RegistryServiceApi->get_prediction_set:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling RegistryServiceApi->get_prediction_set: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_datasets**
> ListDatasetsResponse  = list_datasets()

ListDatasets

List all Datasets in the Registry with optional filters.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id_uuid | **str** | Unique object ID. | 
first_page_req_scheduled_ct_intervals_start_time | **datetime** |  | [optional] 
first_page_req_scheduled_ct_intervals_end_time | **datetime** |  | [optional] 
page_token | **str** | Specifies a page of the list returned by a ListDatasets query. The ListDatasets query returns a pageToken when there is more than one page of results. Specify either this field or the firstPageReq field. | [optional] 
page_size | **str** | The maximum number of Dataset objects to return in a single page. | [optional] 

### Return type

[**ListDatasetsResponse**](ListDatasetsResponse.md)

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
from ri.apiclient.models.list_datasets_response import ListDatasetsResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

project_id_uuid = 'project_id_uuid_example'  # str 
first_page_req_scheduled_ct_intervals_start_time = '2013-10-20T19:20:30+01:00'  # datetime  (optional)
first_page_req_scheduled_ct_intervals_end_time = '2013-10-20T19:20:30+01:00'  # datetime  (optional)
page_token = 'page_token_example'  # str  (optional)
page_size = 'page_size_example'  # str  (optional)

try:
    # ListDatasets
    api_response: ListDatasetsResponse = client.RegistryServiceApi.list_datasets(project_id_uuid, first_page_req_scheduled_ct_intervals_start_time=first_page_req_scheduled_ct_intervals_start_time, first_page_req_scheduled_ct_intervals_end_time=first_page_req_scheduled_ct_intervals_end_time, page_token=page_token, page_size=page_size)
    print("The response of RegistryServiceApi->list_datasets:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling RegistryServiceApi->list_datasets: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_models**
> ListModelsResponse  = list_models()

ListModels

List all Models in the Registry of the specified Project.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id_uuid | **str** | Unique object ID. | 
page_token | **str** | Specifies a page of the list returned by a ListModels query. The ListModels query returns a pageToken when there is more than one page of results. Specify either this field or the firstPageReq field. | [optional] 
page_size | **str** | The maximum number of Model objects to return in a single page. | [optional] 

### Return type

[**ListModelsResponse**](ListModelsResponse.md)

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
from ri.apiclient.models.list_models_response import ListModelsResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

project_id_uuid = 'project_id_uuid_example'  # str 
page_token = 'page_token_example'  # str  (optional)
page_size = 'page_size_example'  # str  (optional)

try:
    # ListModels
    api_response: ListModelsResponse = client.RegistryServiceApi.list_models(project_id_uuid, page_token=page_token, page_size=page_size)
    print("The response of RegistryServiceApi->list_models:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling RegistryServiceApi->list_models: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_prediction_sets**
> ListPredictionSetsResponse  = list_prediction_sets()

ListPredictionSets

List all Prediction sets in the Registry with optional filters.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id_uuid | **str** | Unique object ID. | 
first_page_req_model_id | **str** | Uniquely specifies a Model. | [optional] 
first_page_req_dataset_id | **str** | Uniquely specifies a Dataset. | [optional] 
page_token | **str** | Specifies a page of the list returned by a ListPredictions query. The ListPredictions query returns a pageToken when there is more than one page of results. Specify either this field or the firstPageReq field. | [optional] 
page_size | **str** | The maximum number of Prediction objects to return in a single page. | [optional] 

### Return type

[**ListPredictionSetsResponse**](ListPredictionSetsResponse.md)

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
from ri.apiclient.models.list_prediction_sets_response import ListPredictionSetsResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

project_id_uuid = 'project_id_uuid_example'  # str 
first_page_req_model_id = 'first_page_req_model_id_example'  # str  (optional)
first_page_req_dataset_id = 'first_page_req_dataset_id_example'  # str  (optional)
page_token = 'page_token_example'  # str  (optional)
page_size = 'page_size_example'  # str  (optional)

try:
    # ListPredictionSets
    api_response: ListPredictionSetsResponse = client.RegistryServiceApi.list_prediction_sets(project_id_uuid, first_page_req_model_id=first_page_req_model_id, first_page_req_dataset_id=first_page_req_dataset_id, page_token=page_token, page_size=page_size)
    print("The response of RegistryServiceApi->list_prediction_sets:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling RegistryServiceApi->list_prediction_sets: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_dataset**
> RegisterDatasetResponse  = register_dataset()

RegisterDataset

Register a new Dataset for the specified Project.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id_uuid | **str** | Unique object ID. | 
project_id | **object** | Uniquely specifies a Project. | [optional] 
name | **str** | Unique name of the Dataset. | 
metadata | [**Metadata**](Metadata.md) |  | [optional] 
integration_id | [**ID**](ID.md) |  | [optional] 
data_info | [**DataInfo**](DataInfo.md) |  | 
ct_info | [**CTInfo**](CTInfo.md) |  | [optional] 
skip_validation | **bool** | The parameter is deprecated since 2.7, and does not have any effect. Will always validate the dataset you are registering. Validation ensures that the dataset is valid for Robust Intelligence&#39;s systems. | [optional] 
agent_id | [**ID**](ID.md) |  | [optional] 

### Return type

[**RegisterDatasetResponse**](RegisterDatasetResponse.md)

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
from ri.apiclient.models.register_dataset_request import RegisterDatasetRequest
from ri.apiclient.models.register_dataset_response import RegisterDatasetResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

project_id_uuid = 'project_id_uuid_example'  # str 
project_id = ri.apiclient.models.uniquely_specifies_a_project/.Uniquely specifies a Project.()  # object  (optional)
name = ''  # str 
metadata = Metadata()  # Metadata  (optional)
integration_id = ID()  # ID  (optional)
data_info = DataInfo()  # DataInfo 
ct_info = CTInfo()  # CTInfo  (optional)
skip_validation = True  # bool  (optional)
agent_id = ID()  # ID  (optional)

try:
    # RegisterDataset
    api_response: RegisterDatasetResponse = client.RegistryServiceApi.register_dataset(project_id_uuid, project_id=project_id, name, metadata=metadata, integration_id=integration_id, data_info, ct_info=ct_info, skip_validation=skip_validation, agent_id=agent_id)
    print("The response of RegistryServiceApi->register_dataset:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling RegistryServiceApi->register_dataset: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_model**
> RegisterModelResponse  = register_model()

RegisterModel

Register a new Model for the specified Project.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id_uuid | **str** | Unique object ID. | 
project_id | **object** | Uniquely specifies a Project. | [optional] 
name | **str** | Unique name of the Model. | 
metadata | [**Metadata**](Metadata.md) |  | [optional] 
external_id | **str** | External ID that can be used to identify the model. | [optional] 
model_info | [**ModelInfo**](ModelInfo.md) |  | [optional] 
integration_id | [**ID**](ID.md) |  | [optional] 
skip_validation | **bool** | The parameter is deprecated since 2.7, and does not have any effect. Will always validate the model you are registering. Validation ensures that the model is valid for Robust Intelligence&#39;s systems. | [optional] 
agent_id | [**ID**](ID.md) |  | [optional] 
model_endpoint_integration_id | [**ID**](ID.md) |  | [optional] 

### Return type

[**RegisterModelResponse**](RegisterModelResponse.md)

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
from ri.apiclient.models.register_model_request import RegisterModelRequest
from ri.apiclient.models.register_model_response import RegisterModelResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

project_id_uuid = 'project_id_uuid_example'  # str 
project_id = ri.apiclient.models.uniquely_specifies_a_project/.Uniquely specifies a Project.()  # object  (optional)
name = ''  # str 
metadata = Metadata()  # Metadata  (optional)
external_id = ''  # str  (optional)
model_info = ModelInfo()  # ModelInfo  (optional)
integration_id = ID()  # ID  (optional)
skip_validation = True  # bool  (optional)
agent_id = ID()  # ID  (optional)
model_endpoint_integration_id = ID()  # ID  (optional)

try:
    # RegisterModel
    api_response: RegisterModelResponse = client.RegistryServiceApi.register_model(project_id_uuid, project_id=project_id, name, metadata=metadata, external_id=external_id, model_info=model_info, integration_id=integration_id, skip_validation=skip_validation, agent_id=agent_id, model_endpoint_integration_id=model_endpoint_integration_id)
    print("The response of RegistryServiceApi->register_model:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling RegistryServiceApi->register_model: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_prediction_set**
> RegisterPredictionSetResponse  = register_prediction_set()

RegisterPredictionSet

Register a Prediction set corresponding to a specified Model and Dataset.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id_uuid | **str** | Unique object ID. | 
model_id_uuid | **str** | Unique object ID. | 
dataset_id | **str** | Uniquely specifies a Dataset. | 
project_id | **object** | Uniquely specifies a Project. | [optional] 
model_id | **object** | Uniquely specifies a Model. | [optional] 
metadata | [**Metadata**](Metadata.md) |  | [optional] 
integration_id | [**ID**](ID.md) |  | [optional] 
pred_info | [**PredInfo**](PredInfo.md) |  | [optional] 
skip_validation | **bool** | The parameter is deprecated since 2.7, and does not have any effect. Will always validate the predictions you are registering. Validation ensures that the predictions is valid for Robust Intelligence&#39;s systems. | [optional] 
agent_id | [**ID**](ID.md) |  | [optional] 

### Return type

[**RegisterPredictionSetResponse**](RegisterPredictionSetResponse.md)

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
from ri.apiclient.models.register_prediction_set_request import RegisterPredictionSetRequest
from ri.apiclient.models.register_prediction_set_response import RegisterPredictionSetResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

project_id_uuid = 'project_id_uuid_example'  # str 
model_id_uuid = 'model_id_uuid_example'  # str 
dataset_id = 'dataset_id_example'  # str 
project_id = ri.apiclient.models.uniquely_specifies_a_project/.Uniquely specifies a Project.()  # object  (optional)
model_id = ri.apiclient.models.uniquely_specifies_a_model/.Uniquely specifies a Model.()  # object  (optional)
metadata = Metadata()  # Metadata  (optional)
integration_id = ID()  # ID  (optional)
pred_info = PredInfo()  # PredInfo  (optional)
skip_validation = True  # bool  (optional)
agent_id = ID()  # ID  (optional)

try:
    # RegisterPredictionSet
    api_response: RegisterPredictionSetResponse = client.RegistryServiceApi.register_prediction_set(project_id_uuid, model_id_uuid, dataset_id, project_id=project_id, model_id=model_id, metadata=metadata, integration_id=integration_id, pred_info=pred_info, skip_validation=skip_validation, agent_id=agent_id)
    print("The response of RegistryServiceApi->register_prediction_set:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling RegistryServiceApi->register_prediction_set: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

