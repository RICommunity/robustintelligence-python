# CreateNotificationResponse

CreateNotificationResponse is the response from creating a notification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.create_notification_response import CreateNotificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNotificationResponse from a JSON string
create_notification_response_instance = CreateNotificationResponse.from_json(json)
# print the JSON string representation of the object
print(CreateNotificationResponse.to_json())

# convert the object into a dict
create_notification_response_dict = create_notification_response_instance.to_dict()
# create an instance of CreateNotificationResponse from a dict
create_notification_response_from_dict = CreateNotificationResponse.from_dict(create_notification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

