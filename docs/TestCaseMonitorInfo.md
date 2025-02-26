# TestCaseMonitorInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold** | [**Threshold**](Threshold.md) |  | [optional] 
**is_subset_metric** | **bool** |  | [optional] 
**excluded_transforms** | [**ExcludedTransforms**](ExcludedTransforms.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.test_case_monitor_info import TestCaseMonitorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TestCaseMonitorInfo from a JSON string
test_case_monitor_info_instance = TestCaseMonitorInfo.from_json(json)
# print the JSON string representation of the object
print(TestCaseMonitorInfo.to_json())

# convert the object into a dict
test_case_monitor_info_dict = test_case_monitor_info_instance.to_dict()
# create an instance of TestCaseMonitorInfo from a dict
test_case_monitor_info_from_dict = TestCaseMonitorInfo.from_dict(test_case_monitor_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

