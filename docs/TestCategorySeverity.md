# TestCategorySeverity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_category** | [**TestCategoryType**](TestCategoryType.md) |  | [optional] [default to TestCategoryType.UNSPECIFIED]
**risk_category_type** | [**RiskCategoryType**](RiskCategoryType.md) |  | [optional] [default to RiskCategoryType.UNSPECIFIED]
**severity** | [**RimeSeverity**](RimeSeverity.md) |  | [optional] [default to RimeSeverity.UNSPECIFIED]

## Example

```python
from ri.apiclient.models.test_category_severity import TestCategorySeverity

# TODO update the JSON string below
json = "{}"
# create an instance of TestCategorySeverity from a JSON string
test_category_severity_instance = TestCategorySeverity.from_json(json)
# print the JSON string representation of the object
print(TestCategorySeverity.to_json())

# convert the object into a dict
test_category_severity_dict = test_category_severity_instance.to_dict()
# create an instance of TestCategorySeverity from a dict
test_category_severity_from_dict = TestCategorySeverity.from_dict(
    test_category_severity_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

