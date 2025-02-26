# Notification

Notification represents a single notification setting in the backend. It includes the configuration for when notifications should be sent as well as the list of receivers (emails, webhooks, etc.).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | [optional] 
**object_type** | [**ObjectType**](ObjectType.md) |  | [optional] [default to ObjectType.UNSPECIFIED]
**object_id** | **str** | Uniquely specifies the object for the notification. | [optional] 
**notification_type** | [**NotificationType**](NotificationType.md) |  | [optional] [default to NotificationType.UNSPECIFIED]
**config** | [**NotificationConfig**](NotificationConfig.md) |  | [optional] 
**webhooks** | [**List[WebhookConfig]**](WebhookConfig.md) | Webhooks are a list of destination webhooks to which notifications will be sent. | [optional] 
**emails** | **List[str]** | Emails specify the list of emails to which notifications will be sent. | [optional] 
**last_send_time** | **datetime** | Last send time is the last time the notification was successfully sent. | [optional] 

## Example

```python
from ri.apiclient.models.notification import Notification

# TODO update the JSON string below
json = "{}"
# create an instance of Notification from a JSON string
notification_instance = Notification.from_json(json)
# print the JSON string representation of the object
print(Notification.to_json())

# convert the object into a dict
notification_dict = notification_instance.to_dict()
# create an instance of Notification from a dict
notification_from_dict = Notification.from_dict(notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

