# UpdateNotificationResponse

UpdateNotificationResponse is returned after a successful update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification** | [**Notification**](Notification.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.update_notification_response import UpdateNotificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNotificationResponse from a JSON string
update_notification_response_instance = UpdateNotificationResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateNotificationResponse.to_json())

# convert the object into a dict
update_notification_response_dict = update_notification_response_instance.to_dict()
# create an instance of UpdateNotificationResponse from a dict
update_notification_response_from_dict = UpdateNotificationResponse.from_dict(
    update_notification_response_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

