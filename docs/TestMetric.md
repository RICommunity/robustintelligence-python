# TestMetric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** |  | [optional] 
**category** | [**TestMetricCategory**](TestMetricCategory.md) |  | [optional] [default to TestMetricCategory.UNSPECIFIED]
**int_value** | **str** |  | [optional] 
**float_value** | **float** |  | [optional] 
**empty** | **object** |  | [optional] 
**str_value** | **str** |  | [optional] 
**int_list** | [**IntList**](IntList.md) |  | [optional] 
**float_list** | [**FloatList**](FloatList.md) |  | [optional] 
**str_list** | [**StrList**](StrList.md) |  | [optional] 
**test_case_monitor_info** | [**TestCaseMonitorInfo**](TestCaseMonitorInfo.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.test_metric import TestMetric

# TODO update the JSON string below
json = "{}"
# create an instance of TestMetric from a JSON string
test_metric_instance = TestMetric.from_json(json)
# print the JSON string representation of the object
print(TestMetric.to_json())

# convert the object into a dict
test_metric_dict = test_metric_instance.to_dict()
# create an instance of TestMetric from a dict
test_metric_from_dict = TestMetric.from_dict(test_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

