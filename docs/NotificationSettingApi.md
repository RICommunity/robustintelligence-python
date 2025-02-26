# ri.apiclient.NotificationSettingApi

All URIs are relative to *http://&lt;platform-domain&gt;.rbst.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification**](#create_notification) | **POST** /v1/notif-settings | CreateNotification
[**delete_notification**](#delete_notification) | **DELETE** /v1/notif-settings/{id.uuid} | DeleteNotification
[**list_notifications**](#list_notifications) | **GET** /v1/notif-settings | ListNotifications
[**update_notification**](#update_notification) | **PUT** /v1/notif-settings/{notification.id.uuid} | UpdateNotification

# **create_notification**
> CreateNotificationResponse  = create_notification()

CreateNotification

Creates a new notification setting.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
object_type | [**ObjectType**](ObjectType.md) |  | [optional] [default to OBJECT_TYPE_UNSPECIFIED]
object_id | **str** | Uniquely specifies an object for the notification. This varies depending on the object type; for Projects, this should be the unique identifier of the project. | 
emails | **List[str]** | List of emails that notifications should be sent to - this can be empty. | [optional] 
config | [**NotificationConfig**](NotificationConfig.md) |  | [optional] 
webhooks | [**List[WebhookConfig]**](List.md) | List of webhooks that notifications should be sent to - this can be empty. | [optional] 

### Return type

[**CreateNotificationResponse**](CreateNotificationResponse.md)

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
from ri.apiclient.models.create_notification_request import CreateNotificationRequest
from ri.apiclient.models.create_notification_response import CreateNotificationResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

object_type = ObjectType()  # ObjectType  (optional) (default to OBJECT_TYPE_UNSPECIFIED)
object_id = ''  # str 
emails = [
                    ''
                    ]  # List[str]  (optional)
config = NotificationConfig()  # NotificationConfig  (optional)
webhooks = List[WebhookConfig]  # List[WebhookConfig]  (optional)

try:
    # CreateNotification
    api_response: CreateNotificationResponse = client.notification_setting.create_notification(object_type=object_type, object_id, emails=emails, config=config, webhooks=webhooks)
    print("The response of NotificationSettingApi->create_notification:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling NotificationSettingApi->create_notification: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification**
> object  = delete_notification()

DeleteNotification

Hard-delete a notification setting.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id_uuid | **str** | Unique object ID. | 

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

id_uuid = "id_uuid_example"  # str

try:
    # DeleteNotification
    api_response: object = client.notification_setting.delete_notification(id_uuid)
    print("The response of NotificationSettingApi->delete_notification:\n")
    pprint(api_response)

except ApiException as e:
    print(
        "Exception when calling NotificationSettingApi->delete_notification: %s\n" % e
    )
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notifications**
> ListNotificationsResponse  = list_notifications()

ListNotifications

Lists notification settings with options to filter by project or the type of notification.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
list_notifications_query_object_types | [**List[str]**](str.md) | Specifies a set of object types. Filters results by the specified set of object types.   - OBJECT_TYPE_PROJECT: Used for notifications associated with an project. The Notification object ID is the Project ID. | [optional] 
list_notifications_query_object_ids | [**List[str]**](str.md) | Specifies a set of object IDs. Filters results by the specified set of object IDs. | [optional] 
page_token | **str** | Specifies a page of the list returned by a ListNotifications query. The ListNotifications query returns a pageToken when there is more than one page of results. Specify either this field or the listNotificationsQuery field. | [optional] 
page_size | **str** | The maximum number of Notification objects to return in a single page. | [optional] 

### Return type

[**ListNotificationsResponse**](ListNotificationsResponse.md)

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
from ri.apiclient.models.list_notifications_response import ListNotificationsResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

list_notifications_query_object_types = [
    "list_notifications_query_object_types_example"
]  # List[str]  (optional)
list_notifications_query_object_ids = [
    "list_notifications_query_object_ids_example"
]  # List[str]  (optional)
page_token = "page_token_example"  # str  (optional)
page_size = "page_size_example"  # str  (optional)

try:
    # ListNotifications
    api_response: ListNotificationsResponse = (
        client.notification_setting.list_notifications(
            list_notifications_query_object_types=list_notifications_query_object_types,
            list_notifications_query_object_ids=list_notifications_query_object_ids,
            page_token=page_token,
            page_size=page_size,
        )
    )
    print("The response of NotificationSettingApi->list_notifications:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling NotificationSettingApi->list_notifications: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification**
> UpdateNotificationResponse  = update_notification()

UpdateNotification

Updates an existing notification setting. The ID in the provided notification is used to identify it.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
notification_id_uuid | **str** | Unique object ID. | 
notification | [**UpdateNotificationRequestNotification**](UpdateNotificationRequestNotification.md) |  | [optional] 
mask | **str** | Mask for determining which fields of the notification setting should be written in the Update. Specify a mask as a &#x60;.&#x60; separated path of field names e.g. &#x60;foo.bar&#x60; for nested field &#x60;bar&#x60; in submessage &#x60;foo&#x60;. Note: some fields are marked immutable and cannot be changed. | [optional] 

### Return type

[**UpdateNotificationResponse**](UpdateNotificationResponse.md)

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
from ri.apiclient.models.update_notification_request import UpdateNotificationRequest
from ri.apiclient.models.update_notification_response import UpdateNotificationResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

notification_id_uuid = "notification_id_uuid_example"  # str
notification = (
    UpdateNotificationRequestNotification()
)  # UpdateNotificationRequestNotification  (optional)
mask = ""  # str  (optional)

try:
    # UpdateNotification
    api_response: UpdateNotificationResponse = (
        client.notification_setting.update_notification(
            notification_id_uuid, notification=notification, mask=mask
        )
    )
    print("The response of NotificationSettingApi->update_notification:\n")
    pprint(api_response)

except ApiException as e:
    print(
        "Exception when calling NotificationSettingApi->update_notification: %s\n" % e
    )
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

