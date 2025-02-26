# ListNotificationsQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_types** | [**List[ObjectType]**](ObjectType.md) | Specifies a set of object types. Filters results by the specified set of object types. | [optional] 
**object_ids** | **List[str]** | Specifies a set of object IDs. Filters results by the specified set of object IDs. | [optional] 

## Example

```python
from ri.apiclient.models.list_notifications_query import ListNotificationsQuery

# TODO update the JSON string below
json = "{}"
# create an instance of ListNotificationsQuery from a JSON string
list_notifications_query_instance = ListNotificationsQuery.from_json(json)
# print the JSON string representation of the object
print(ListNotificationsQuery.to_json())

# convert the object into a dict
list_notifications_query_dict = list_notifications_query_instance.to_dict()
# create an instance of ListNotificationsQuery from a dict
list_notifications_query_from_dict = ListNotificationsQuery.from_dict(list_notifications_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

