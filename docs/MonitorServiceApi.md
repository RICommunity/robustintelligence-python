# ri.apiclient.MonitorServiceApi

All URIs are relative to *http://&lt;platform-domain&gt;.rbst.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_monitor**](#create_custom_monitor) | **POST** /v1-beta/custom-monitors/{name} | CreateCustomMonitor
[**delete_custom_monitor**](#delete_custom_monitor) | **DELETE** /v1-beta/custom-monitors/{monitorId.uuid} | DeleteCustomMonitor
[**get_monitor_result**](#get_monitor_result) | **GET** /v1-beta/monitors/result/{monitorId.uuid} | GetMonitorResult
[**list_metric_identifiers**](#list_metric_identifiers) | **GET** /v1-beta/custom-monitors/metrics/{firewallId.uuid} | ListMetricIdentifiers
[**list_monitors**](#list_monitors) | **GET** /v1-beta/monitors/{firewallId.uuid} | ListMonitors
[**update_monitor**](#update_monitor) | **PUT** /v1-beta/monitors/{monitor.id.uuid} | UpdateMonitor

# **create_custom_monitor**
> CreateCustomMonitorResponse  = create_custom_monitor()

CreateCustomMonitor

Create a new custom monitor

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | **str** | The name of the monitor. | 
firewall_id | [**ID**](ID.md) |  | [optional] 
artifact_identifier | [**ArtifactIdentifier**](ArtifactIdentifier.md) |  | [optional] 
aggregation | [**Aggregation**](Aggregation.md) |  | [optional] 
transform | [**Transform**](Transform.md) |  | [optional] 
threshold | [**Threshold**](Threshold.md) |  | [optional] 
notify | **bool** | Whether to notify when the monitor is triggered. | [optional] 

### Return type

[**CreateCustomMonitorResponse**](CreateCustomMonitorResponse.md)

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
from ri.apiclient.models.create_custom_monitor_request import CreateCustomMonitorRequest
from ri.apiclient.models.create_custom_monitor_response import (
    CreateCustomMonitorResponse,
)
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

name = "name_example"  # str
firewall_id = ID()  # ID  (optional)
artifact_identifier = ArtifactIdentifier()  # ArtifactIdentifier  (optional)
aggregation = Aggregation()  # Aggregation  (optional)
transform = Transform()  # Transform  (optional)
threshold = Threshold()  # Threshold  (optional)
notify = True  # bool  (optional)

try:
    # CreateCustomMonitor
    api_response: CreateCustomMonitorResponse = (
        client.monitor_service.create_custom_monitor(
            name,
            firewall_id=firewall_id,
            artifact_identifier=artifact_identifier,
            aggregation=aggregation,
            transform=transform,
            threshold=threshold,
            notify=notify,
        )
    )
    print("The response of MonitorServiceApi->create_custom_monitor:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling MonitorServiceApi->create_custom_monitor: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_monitor**
> object  = delete_custom_monitor()

DeleteCustomMonitor

Delete a custom monitor

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
monitor_id_uuid | **str** | Unique object ID. | 

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

monitor_id_uuid = "monitor_id_uuid_example"  # str

try:
    # DeleteCustomMonitor
    api_response: object = client.monitor_service.delete_custom_monitor(monitor_id_uuid)
    print("The response of MonitorServiceApi->delete_custom_monitor:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling MonitorServiceApi->delete_custom_monitor: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitor_result**
> GetMonitorResultResponse  = get_monitor_result()

GetMonitorResult

Graph a monitor within a time range

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
monitor_id_uuid | **str** | Unique object ID. | 
time_interval_start_time | **datetime** |  | [optional] 
time_interval_end_time | **datetime** |  | [optional] 

### Return type

[**GetMonitorResultResponse**](GetMonitorResultResponse.md)

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
from ri.apiclient.models.get_monitor_result_response import GetMonitorResultResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

monitor_id_uuid = "monitor_id_uuid_example"  # str
time_interval_start_time = "2013-10-20T19:20:30+01:00"  # datetime  (optional)
time_interval_end_time = "2013-10-20T19:20:30+01:00"  # datetime  (optional)

try:
    # GetMonitorResult
    api_response: GetMonitorResultResponse = client.monitor_service.get_monitor_result(
        monitor_id_uuid,
        time_interval_start_time=time_interval_start_time,
        time_interval_end_time=time_interval_end_time,
    )
    print("The response of MonitorServiceApi->get_monitor_result:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling MonitorServiceApi->get_monitor_result: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_metric_identifiers**
> ListMetricIdentifiersResponse  = list_metric_identifiers()

ListMetricIdentifiers

List all possible Custom Monitor Metric Identifiers

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
firewall_id_uuid | **str** | Unique object ID. | 

### Return type

[**ListMetricIdentifiersResponse**](ListMetricIdentifiersResponse.md)

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
from ri.apiclient.models.list_metric_identifiers_response import (
    ListMetricIdentifiersResponse,
)
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

firewall_id_uuid = "firewall_id_uuid_example"  # str

try:
    # ListMetricIdentifiers
    api_response: ListMetricIdentifiersResponse = (
        client.monitor_service.list_metric_identifiers(firewall_id_uuid)
    )
    print("The response of MonitorServiceApi->list_metric_identifiers:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling MonitorServiceApi->list_metric_identifiers: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_monitors**
> ListMonitorsResponse  = list_monitors()

ListMonitors

lists monitors by firewall ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
firewall_id_uuid | **str** | Unique object ID. | 
first_page_req_included_monitor_types | [**List[str]**](str.md) | Specifies a list of monitor types. Filters results to match the specified monitor types. | [optional] 
first_page_req_included_risk_category_types | [**List[str]**](str.md) | Specifies a list of risk category types. Filters results to match the specified risk category types. | [optional] 
first_page_req_pinned_monitors_only | **bool** | When the value of this Boolean is True, this endpoint returns a list of pinned Monitors. Otherwise, this endpoint does not filter Monitors by pinned status. | [optional] 
page_token | **str** | Specifies a page of the list returned by a ListMonitors query. The ListMonitors query returns a pageToken when there is more than one page of results. Specify either this field or the firstPageReq field. | [optional] 
page_size | **str** | The maximum number of Monitor objects to return in a single page. | [optional] 

### Return type

[**ListMonitorsResponse**](ListMonitorsResponse.md)

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
from ri.apiclient.models.list_monitors_response import ListMonitorsResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

firewall_id_uuid = "firewall_id_uuid_example"  # str
first_page_req_included_monitor_types = [
    "first_page_req_included_monitor_types_example"
]  # List[str]  (optional)
first_page_req_included_risk_category_types = [
    "first_page_req_included_risk_category_types_example"
]  # List[str]  (optional)
first_page_req_pinned_monitors_only = True  # bool  (optional)
page_token = "page_token_example"  # str  (optional)
page_size = "page_size_example"  # str  (optional)

try:
    # ListMonitors
    api_response: ListMonitorsResponse = client.monitor_service.list_monitors(
        firewall_id_uuid,
        first_page_req_included_monitor_types=first_page_req_included_monitor_types,
        first_page_req_included_risk_category_types=first_page_req_included_risk_category_types,
        first_page_req_pinned_monitors_only=first_page_req_pinned_monitors_only,
        page_token=page_token,
        page_size=page_size,
    )
    print("The response of MonitorServiceApi->list_monitors:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling MonitorServiceApi->list_monitors: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_monitor**
> UpdateMonitorResponse  = update_monitor()

UpdateMonitor

Updates a monitor.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
monitor_id_uuid | **str** | Unique object ID. | 
monitor | [**UpdateMonitorRequestMonitor**](UpdateMonitorRequestMonitor.md) |  | [optional] 
mask | **str** | The field mask. | [optional] 

### Return type

[**UpdateMonitorResponse**](UpdateMonitorResponse.md)

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
from ri.apiclient.models.update_monitor_request import UpdateMonitorRequest
from ri.apiclient.models.update_monitor_response import UpdateMonitorResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

monitor_id_uuid = "monitor_id_uuid_example"  # str
monitor = UpdateMonitorRequestMonitor()  # UpdateMonitorRequestMonitor  (optional)
mask = ""  # str  (optional)

try:
    # UpdateMonitor
    api_response: UpdateMonitorResponse = client.monitor_service.update_monitor(
        monitor_id_uuid, monitor=monitor, mask=mask
    )
    print("The response of MonitorServiceApi->update_monitor:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling MonitorServiceApi->update_monitor: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

