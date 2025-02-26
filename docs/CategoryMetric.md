# CategoryMetric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value** | **float** |  | [optional] 
**threshold** | [**Threshold**](Threshold.md) |  | [optional] 
**description** | **str** |  | [optional] 
**risk_category_type** | [**RiskCategoryType**](RiskCategoryType.md) |  | [optional] [default to RiskCategoryType.UNSPECIFIED]

## Example

```python
from ri.apiclient.models.category_metric import CategoryMetric

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryMetric from a JSON string
category_metric_instance = CategoryMetric.from_json(json)
# print the JSON string representation of the object
print(CategoryMetric.to_json())

# convert the object into a dict
category_metric_dict = category_metric_instance.to_dict()
# create an instance of CategoryMetric from a dict
category_metric_from_dict = CategoryMetric.from_dict(category_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

