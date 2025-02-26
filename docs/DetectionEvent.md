# DetectionEvent

DetectionEvent describes a specific problem with a model. Examples of issues reported by this event include performance metrics dropping below a specified threshold or detecting an evasion attack. Each event is attached to a parent monitor that has a corresponding test in the RIME engine.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | [optional] 
**project_id** | [**ID**](ID.md) |  | [optional] 
**firewall_id** | [**ID**](ID.md) |  | [optional] 
**event_type** | [**EventType**](EventType.md) |  | [optional] [default to EventType.UNSPECIFIED]
**severity** | [**RimeSeverity**](RimeSeverity.md) |  | [optional] [default to RimeSeverity.UNSPECIFIED]
**event_object_id** | **str** | The event object varies with the event type. CT and security events use a monitor. Offline Test events use the test run. | [optional] 
**event_object_name** | **str** | event_object_name to avoid extra query from UI to display, and allow easier search support with DB. If the event object is renamed, the event will not be updated. | [optional] 
**event_time_range** | [**TimeInterval**](TimeInterval.md) |  | [optional] 
**last_update_time** | **datetime** |  | [optional] 
**risk_category_type** | [**RiskCategoryType**](RiskCategoryType.md) |  | [optional] [default to RiskCategoryType.UNSPECIFIED]
**test_category** | [**TestCategoryType**](TestCategoryType.md) |  | [optional] [default to TestCategoryType.UNSPECIFIED]
**description** | **str** | Human-readable description of the event. | [optional] 
**description_html** | **str** | Description of the event with HTML for nicer rendering. | [optional] 
**resolution** | [**Resolution**](Resolution.md) |  | [optional] 
**detail** | [**EventDetail**](EventDetail.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.detection_event import DetectionEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DetectionEvent from a JSON string
detection_event_instance = DetectionEvent.from_json(json)
# print the JSON string representation of the object
print(DetectionEvent.to_json())

# convert the object into a dict
detection_event_dict = detection_event_instance.to_dict()
# create an instance of DetectionEvent from a dict
detection_event_from_dict = DetectionEvent.from_dict(detection_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

