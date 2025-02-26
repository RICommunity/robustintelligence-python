# ri.apiclient.ScheduleServiceApi

All URIs are relative to *http://&lt;platform-domain&gt;.rbst.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_schedule**](#create_schedule) | **POST** /v1-beta/schedules | CreateSchedule creates a schedule.
[**delete_schedule**](#delete_schedule) | **DELETE** /v1-beta/schedules/{scheduleId.uuid} | DeleteSchedule deletes a schedule.
[**get_schedule**](#get_schedule) | **GET** /v1-beta/schedules/{scheduleId.uuid} | GetSchedule gets a schedule.
[**update_schedule**](#update_schedule) | **PATCH** /v1-beta/schedules/{schedule.scheduleId.uuid} | UpdateSchedule updates a schedule.

# **create_schedule**
> CreateScheduleResponse  = create_schedule()

CreateSchedule creates a schedule.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id | [**ID**](ID.md) |  | 
test_run_config | [**TestRunConfig**](TestRunConfig.md) |  | 
frequency_cron_expr | **str** | Cron expression used to determine how often to run the schedule. | 

### Return type

[**CreateScheduleResponse**](CreateScheduleResponse.md)

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
from ri.apiclient.models.create_schedule_request import CreateScheduleRequest
from ri.apiclient.models.create_schedule_response import CreateScheduleResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

project_id = ID()  # ID 
test_run_config = TestRunConfig()  # TestRunConfig 
frequency_cron_expr = ''  # str 

try:
    # CreateSchedule creates a schedule.
    api_response: CreateScheduleResponse = client.ScheduleServiceApi.create_schedule(project_id, test_run_config, frequency_cron_expr)
    print("The response of ScheduleServiceApi->create_schedule:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ScheduleServiceApi->create_schedule: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_schedule**
> object  = delete_schedule()

DeleteSchedule deletes a schedule.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
schedule_id_uuid | **str** | Unique object ID. | 

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

schedule_id_uuid = 'schedule_id_uuid_example'  # str 

try:
    # DeleteSchedule deletes a schedule.
    api_response: object = client.ScheduleServiceApi.delete_schedule(schedule_id_uuid)
    print("The response of ScheduleServiceApi->delete_schedule:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ScheduleServiceApi->delete_schedule: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schedule**
> GetScheduleResponse  = get_schedule()

GetSchedule gets a schedule.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
schedule_id_uuid | **str** | Unique object ID. | 

### Return type

[**GetScheduleResponse**](GetScheduleResponse.md)

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
from ri.apiclient.models.get_schedule_response import GetScheduleResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

schedule_id_uuid = 'schedule_id_uuid_example'  # str 

try:
    # GetSchedule gets a schedule.
    api_response: GetScheduleResponse = client.ScheduleServiceApi.get_schedule(schedule_id_uuid)
    print("The response of ScheduleServiceApi->get_schedule:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ScheduleServiceApi->get_schedule: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_schedule**
> UpdateScheduleResponse  = update_schedule()

UpdateSchedule updates a schedule.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
schedule_schedule_id_uuid | **str** | Unique object ID. | 
mask | **str** | Update mask specifies the fields in the config that will be updated. Any values not in the mask will be ignored. Currently only updated the frequency of the schedule is supported. | 
schedule_id | **object** | Unique ID of an object in RIME. | [optional] 
project_id | [**ID**](ID.md) |  | [optional] 
test_run_config | [**TestRunConfig**](TestRunConfig.md) |  | [optional] 
frequency_cron_expr | **str** | Cron expression used to determine how often to run the schedule. Accepts \&quot;@hourly\&quot;, \&quot;@daily\&quot;, \&quot;@weekly\&quot;, and \&quot;@monthly\&quot;. | [optional] 

### Return type

[**UpdateScheduleResponse**](UpdateScheduleResponse.md)

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
from ri.apiclient.models.update_schedule_request import UpdateScheduleRequest
from ri.apiclient.models.update_schedule_response import UpdateScheduleResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

schedule_schedule_id_uuid = 'schedule_schedule_id_uuid_example'  # str 
mask = 'mask_example'  # str 
schedule_id = ri.apiclient.models.schedule_id.scheduleId()  # object  (optional)
project_id = ID()  # ID  (optional)
test_run_config = TestRunConfig()  # TestRunConfig  (optional)
frequency_cron_expr = ''  # str  (optional)

try:
    # UpdateSchedule updates a schedule.
    api_response: UpdateScheduleResponse = client.ScheduleServiceApi.update_schedule(schedule_schedule_id_uuid, mask, schedule_id=schedule_id, project_id=project_id, test_run_config=test_run_config, frequency_cron_expr=frequency_cron_expr)
    print("The response of ScheduleServiceApi->update_schedule:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ScheduleServiceApi->update_schedule: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

