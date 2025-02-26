# ListNotificationsResponse

ListNotificationsResponse is a single page of notification settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notifications** | [**List[Notification]**](Notification.md) | List of individual notification objects requested from the backend. | [optional] 
**next_page_token** | **str** | The page token to use in the next ListNotifications call. | [optional] 
**has_more** | **bool** | Whether or not there are more notification settings in the DB. | [optional] 

## Example

```python
from ri.apiclient.models.list_notifications_response import ListNotificationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListNotificationsResponse from a JSON string
list_notifications_response_instance = ListNotificationsResponse.from_json(json)
# print the JSON string representation of the object
print(ListNotificationsResponse.to_json())

# convert the object into a dict
list_notifications_response_dict = list_notifications_response_instance.to_dict()
# create an instance of ListNotificationsResponse from a dict
list_notifications_response_from_dict = ListNotificationsResponse.from_dict(list_notifications_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

