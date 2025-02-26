# ri.apiclient.DataCollectorApi

All URIs are relative to *http://&lt;platform-domain&gt;.rbst.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_datapoints**](#get_datapoints) | **GET** /v1-beta/data-collector/datapoints/{dataStreamId.uuid} | GetDatapoints
[**get_predictions**](#get_predictions) | **GET** /v1-beta/data-collector/predictions/{modelId.uuid}/{dataStreamId.uuid} | GetPredictions
[**register_data_stream**](#register_data_stream) | **POST** /v1-beta/data-collector/datastream/{projectId.uuid} | RegisterDataStream
[**store_datapoints**](#store_datapoints) | **PUT** /v1-beta/data-collector/data/{dataStreamId.uuid} | StoreDatapoints
[**store_predictions**](#store_predictions) | **PUT** /v1-beta/data-collector/predictions/{modelId.uuid} | StorePredictions

# **get_datapoints**
> StreamResultOfGetDatapointsResponse  = get_datapoints()

GetDatapoints

GetDatapoints returns all datapoints from a time period.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
data_stream_id_uuid | **str** | Unique object ID. | 
time_interval_start_time | **datetime** |  | [optional] 
time_interval_end_time | **datetime** |  | [optional] 

### Return type

[**StreamResultOfGetDatapointsResponse**](StreamResultOfGetDatapointsResponse.md)

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
from ri.apiclient.models.stream_result_of_get_datapoints_response import StreamResultOfGetDatapointsResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

data_stream_id_uuid = 'data_stream_id_uuid_example'  # str 
time_interval_start_time = '2013-10-20T19:20:30+01:00'  # datetime  (optional)
time_interval_end_time = '2013-10-20T19:20:30+01:00'  # datetime  (optional)

try:
    # GetDatapoints
    api_response: StreamResultOfGetDatapointsResponse = client.DataCollectorApi.get_datapoints(data_stream_id_uuid, time_interval_start_time=time_interval_start_time, time_interval_end_time=time_interval_end_time)
    print("The response of DataCollectorApi->get_datapoints:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling DataCollectorApi->get_datapoints: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_predictions**
> StreamResultOfGetPredictionsResponse  = get_predictions()

GetPredictions

GetPredictions returns all predictions from a time period

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
model_id_uuid | **str** | Unique object ID. | 
data_stream_id_uuid | **str** | Unique object ID. | 
time_interval_start_time | **datetime** |  | [optional] 
time_interval_end_time | **datetime** |  | [optional] 

### Return type

[**StreamResultOfGetPredictionsResponse**](StreamResultOfGetPredictionsResponse.md)

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
from ri.apiclient.models.stream_result_of_get_predictions_response import StreamResultOfGetPredictionsResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

model_id_uuid = 'model_id_uuid_example'  # str 
data_stream_id_uuid = 'data_stream_id_uuid_example'  # str 
time_interval_start_time = '2013-10-20T19:20:30+01:00'  # datetime  (optional)
time_interval_end_time = '2013-10-20T19:20:30+01:00'  # datetime  (optional)

try:
    # GetPredictions
    api_response: StreamResultOfGetPredictionsResponse = client.DataCollectorApi.get_predictions(model_id_uuid, data_stream_id_uuid, time_interval_start_time=time_interval_start_time, time_interval_end_time=time_interval_end_time)
    print("The response of DataCollectorApi->get_predictions:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling DataCollectorApi->get_predictions: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_data_stream**
> RegisterDataStreamResponse  = register_data_stream()

RegisterDataStream

Registers a new data stream. A data stream is a location where data points are stored. All data points that are in the same registered data set must be stored in the same data stream.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id_uuid | **str** | Unique object ID. | 
project_id | **object** | Uniquely specifies a Project. | [optional] 

### Return type

[**RegisterDataStreamResponse**](RegisterDataStreamResponse.md)

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
from ri.apiclient.models.register_data_stream_request import RegisterDataStreamRequest
from ri.apiclient.models.register_data_stream_response import RegisterDataStreamResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

project_id_uuid = 'project_id_uuid_example'  # str 
project_id = ri.apiclient.models.uniquely_specifies_a_project/.Uniquely specifies a Project.()  # object  (optional)

try:
    # RegisterDataStream
    api_response: RegisterDataStreamResponse = client.DataCollectorApi.register_data_stream(project_id_uuid, project_id=project_id)
    print("The response of DataCollectorApi->register_data_stream:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling DataCollectorApi->register_data_stream: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_datapoints**
> StoreDatapointsResponse  = store_datapoints()

StoreDatapoints

Store multiple new datapoints into a data stream.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
data_stream_id_uuid | **str** | Unique object ID. | 
data_stream_id | **object** | Uniquely specifies a data stream. | [optional] 
datapoints | [**List[DatapointRow]**](List.md) | The datapoints to store. | [optional] 

### Return type

[**StoreDatapointsResponse**](StoreDatapointsResponse.md)

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
from ri.apiclient.models.store_datapoints_request import StoreDatapointsRequest
from ri.apiclient.models.store_datapoints_response import StoreDatapointsResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

data_stream_id_uuid = 'data_stream_id_uuid_example'  # str 
data_stream_id = ri.apiclient.models.uniquely_specifies_a_data_stream/.Uniquely specifies a data stream.()  # object  (optional)
datapoints = List[DatapointRow]()  # List[DatapointRow]  (optional)

try:
    # StoreDatapoints
    api_response: StoreDatapointsResponse = client.DataCollectorApi.store_datapoints(data_stream_id_uuid, data_stream_id=data_stream_id, datapoints=datapoints)
    print("The response of DataCollectorApi->store_datapoints:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling DataCollectorApi->store_datapoints: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_predictions**
> object  = store_predictions()

StorePredictions

Store multiple new predictions.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
model_id_uuid | **str** | Unique object ID. | 
model_id | **object** | Uniquely specifies a Model. | [optional] 
predictions | [**List[StorePredictionsRequestPrediction]**](List.md) |  | 

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
from ri.apiclient.models.store_predictions_request import StorePredictionsRequest
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

model_id_uuid = 'model_id_uuid_example'  # str 
model_id = ri.apiclient.models.uniquely_specifies_a_model/.Uniquely specifies a Model.()  # object  (optional)
predictions = List[StorePredictionsRequestPrediction]()  # List[StorePredictionsRequestPrediction] 

try:
    # StorePredictions
    api_response: object = client.DataCollectorApi.store_predictions(model_id_uuid, model_id=model_id, predictions)
    print("The response of DataCollectorApi->store_predictions:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling DataCollectorApi->store_predictions: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

