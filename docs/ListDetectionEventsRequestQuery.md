# ListDetectionEventsRequestQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firewall_id** | [**ID**](ID.md) |  | [optional] 
**event_object_id** | **str** | Optional: return a series of detection events for a single object. | [optional] 
**event_time_range** | [**TimeInterval**](TimeInterval.md) |  | [optional] 
**severity** | [**RimeSeverity**](RimeSeverity.md) |  | [optional] [default to RimeSeverity.UNSPECIFIED]
**event_types** | [**List[EventType]**](EventType.md) | Optional: When the list is empty, returns all. | [optional] 
**risk_category_types** | [**List[RiskCategoryType]**](RiskCategoryType.md) | Optional: When the list is empty, returns all. | [optional] 
**test_categories** | [**List[TestCategoryType]**](TestCategoryType.md) | Optional: When the list is empty, return all. | [optional] 
**sort** | [**SortSpec**](SortSpec.md) |  | [optional] 
**include_resolved** | **bool** |  | [optional] 

## Example

```python
from ri.apiclient.models.list_detection_events_request_query import ListDetectionEventsRequestQuery

# TODO update the JSON string below
json = "{}"
# create an instance of ListDetectionEventsRequestQuery from a JSON string
list_detection_events_request_query_instance = ListDetectionEventsRequestQuery.from_json(json)
# print the JSON string representation of the object
print(ListDetectionEventsRequestQuery.to_json())

# convert the object into a dict
list_detection_events_request_query_dict = list_detection_events_request_query_instance.to_dict()
# create an instance of ListDetectionEventsRequestQuery from a dict
list_detection_events_request_query_from_dict = ListDetectionEventsRequestQuery.from_dict(list_detection_events_request_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

