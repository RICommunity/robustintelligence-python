# ListDetectionEventsResponse

ListDetectionEventsResponse repesents a single page of detection events returned from the backend.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[DetectionEvent]**](DetectionEvent.md) | Page of events returned from the backend. | [optional] 
**next_page_token** | **str** | Page token to use in the next ListDetectionEvents call. | [optional] 
**has_more** | **bool** | Indicates whether there are more events to return. | [optional] 

## Example

```python
from ri.apiclient.models.list_detection_events_response import (
    ListDetectionEventsResponse,
)

# TODO update the JSON string below
json = "{}"
# create an instance of ListDetectionEventsResponse from a JSON string
list_detection_events_response_instance = ListDetectionEventsResponse.from_json(json)
# print the JSON string representation of the object
print(ListDetectionEventsResponse.to_json())

# convert the object into a dict
list_detection_events_response_dict = list_detection_events_response_instance.to_dict()
# create an instance of ListDetectionEventsResponse from a dict
list_detection_events_response_from_dict = ListDetectionEventsResponse.from_dict(
    list_detection_events_response_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

