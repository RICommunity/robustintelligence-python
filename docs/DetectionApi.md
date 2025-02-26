# ri.apiclient.DetectionApi

All URIs are relative to *http://&lt;platform-domain&gt;.rbst.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_detection_events**](#list_detection_events) | **GET** /v1-beta/detection-events/{projectId.uuid} | ListDetectionEvents

# **list_detection_events**
> ListDetectionEventsResponse  = list_detection_events()

ListDetectionEvents

List out events for a given project. Detection events represent problems Robust Intelligence detects in different risk categories, such as performance degradation or security risk. This is a paginated method.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id_uuid | **str** | Unique object ID. | 
first_page_req_event_object_id | **str** | Optional: return a series of detection events for a single object. | [optional] 
first_page_req_event_time_range_start_time | **datetime** |  | [optional] 
first_page_req_event_time_range_end_time | **datetime** |  | [optional] 
first_page_req_severity | **str** | Optional: When unspecified, returns all.   - SEVERITY_UNSPECIFIED: Indicates that no test runs for the specified metric.  - SEVERITY_PASS: Indicates that the specified metric is lower than the low threshold in the case where the Monitor is configured to trigger on an increase of a metric.  - SEVERITY_WARNING: Indicates that the specified metric is higher than the low threshold but still lower than the high threshold, in the case that a Monitor is configured to trigger on an increase of a metric. Warning and Alert severity levels will trigger a Degradation event.  - SEVERITY_ALERT: Indicates that the specified metric is higher than the high threshold in the case that the Monitor is configured to trigger on an increase of a metric. Warning and Alert severity level will trigger a Degradation event. | [optional] [default to SEVERITY_UNSPECIFIED]
first_page_req_event_types | [**List[str]**](str.md) | Optional: When the list is empty, returns all. | [optional] 
first_page_req_risk_category_types | [**List[str]**](str.md) | Optional: When the list is empty, returns all. | [optional] 
first_page_req_test_categories | [**List[str]**](str.md) | Optional: When the list is empty, return all. | [optional] 
first_page_req_sort_sort_order | **str** |  | [optional] [default to ORDER_UNSPECIFIED]
first_page_req_sort_sort_by | **str** |  | [optional] 
first_page_req_include_resolved | **bool** |  | [optional] 
page_token | **str** | Specifies a page of the list returned by a ListDetectionEvents query. The ListDetectionEvents query returns a pageToken when there is more than one page of results. Specify either this field or the firstPageReq field. | [optional] 
page_size | **str** | The maximum number of Detection Event objects to return in a single page. | [optional] 

### Return type

[**ListDetectionEventsResponse**](ListDetectionEventsResponse.md)

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
from ri.apiclient.models.list_detection_events_response import ListDetectionEventsResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

project_id_uuid = 'project_id_uuid_example'  # str 
first_page_req_event_object_id = 'first_page_req_event_object_id_example'  # str  (optional)
first_page_req_event_time_range_start_time = '2013-10-20T19:20:30+01:00'  # datetime  (optional)
first_page_req_event_time_range_end_time = '2013-10-20T19:20:30+01:00'  # datetime  (optional)
first_page_req_severity = SEVERITY_UNSPECIFIED  # str  (optional) (default to SEVERITY_UNSPECIFIED)
first_page_req_event_types = ['first_page_req_event_types_example']  # List[str]  (optional)
first_page_req_risk_category_types = ['first_page_req_risk_category_types_example']  # List[str]  (optional)
first_page_req_test_categories = ['first_page_req_test_categories_example']  # List[str]  (optional)
first_page_req_sort_sort_order = ORDER_UNSPECIFIED  # str  (optional) (default to ORDER_UNSPECIFIED)
first_page_req_sort_sort_by = 'first_page_req_sort_sort_by_example'  # str  (optional)
first_page_req_include_resolved = True  # bool  (optional)
page_token = 'page_token_example'  # str  (optional)
page_size = 'page_size_example'  # str  (optional)

try:
    # ListDetectionEvents
    api_response: ListDetectionEventsResponse = client.DetectionApi.list_detection_events(project_id_uuid, first_page_req_event_object_id=first_page_req_event_object_id, first_page_req_event_time_range_start_time=first_page_req_event_time_range_start_time, first_page_req_event_time_range_end_time=first_page_req_event_time_range_end_time, first_page_req_severity=first_page_req_severity, first_page_req_event_types=first_page_req_event_types, first_page_req_risk_category_types=first_page_req_risk_category_types, first_page_req_test_categories=first_page_req_test_categories, first_page_req_sort_sort_order=first_page_req_sort_sort_order, first_page_req_sort_sort_by=first_page_req_sort_sort_by, first_page_req_include_resolved=first_page_req_include_resolved, page_token=page_token, page_size=page_size)
    print("The response of DetectionApi->list_detection_events:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling DetectionApi->list_detection_events: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

