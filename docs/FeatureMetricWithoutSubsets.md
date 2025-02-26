# FeatureMetricWithoutSubsets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_case_metric_identifier** | [**TestCaseMetricIdentifier**](TestCaseMetricIdentifier.md) |  | [optional] 
**excluded_transforms** | [**ExcludedTransforms**](ExcludedTransforms.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.feature_metric_without_subsets import FeatureMetricWithoutSubsets

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureMetricWithoutSubsets from a JSON string
feature_metric_without_subsets_instance = FeatureMetricWithoutSubsets.from_json(json)
# print the JSON string representation of the object
print(FeatureMetricWithoutSubsets.to_json())

# convert the object into a dict
feature_metric_without_subsets_dict = feature_metric_without_subsets_instance.to_dict()
# create an instance of FeatureMetricWithoutSubsets from a dict
feature_metric_without_subsets_from_dict = FeatureMetricWithoutSubsets.from_dict(feature_metric_without_subsets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

