# CreateNotificationRequest

CreateNotificationRequest is a request for creating a new notification setting in the backend.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | [**ObjectType**](ObjectType.md) |  | [optional] [default to ObjectType.UNSPECIFIED]
**object_id** | **str** | Uniquely specifies an object for the notification. This varies depending on the object type; for Projects, this should be the unique identifier of the project. | 
**emails** | **List[str]** | List of emails that notifications should be sent to - this can be empty. | [optional] 
**config** | [**NotificationConfig**](NotificationConfig.md) |  | [optional] 
**webhooks** | [**List[WebhookConfig]**](WebhookConfig.md) | List of webhooks that notifications should be sent to - this can be empty. | [optional] 

## Example

```python
from ri.apiclient.models.create_notification_request import CreateNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNotificationRequest from a JSON string
create_notification_request_instance = CreateNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateNotificationRequest.to_json())

# convert the object into a dict
create_notification_request_dict = create_notification_request_instance.to_dict()
# create an instance of CreateNotificationRequest from a dict
create_notification_request_from_dict = CreateNotificationRequest.from_dict(create_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

