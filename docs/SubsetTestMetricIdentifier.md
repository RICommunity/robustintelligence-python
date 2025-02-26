# SubsetTestMetricIdentifier

In order to specify a TestCaseMetricIdentifier, TestBatchType, FeatureName and Metric are required. Note that each of them refer to fields in the TestCase doc. Metric refers to a single Metric in array TestMetric (in the TestCase doc). For example for some TestCase Doc: {    ...    test_batch_type: 'subset_performance:subset_positive_prediction_rate',    feature_id: 'xxxx',    metrics: [      {        category: 14,        metric: 'worst_perf_diff',        data: {float_value: 0.032836160521054425},        data_type: 1      },      {      category: 14,          metric: 'names',          data: { str_list: [ 'credit', 'debit', 'null' ] },          data_type: 1      },    ] } We can specify TestCaseMetricIdentifier as: {    test_batch_id = 'subset_performance:subset_positive_prediction_rate',    feature_id = 'xxxx',    metric = 'names', } Use well.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_batch_id** | **str** | Uniquely specifies a Test Batch. | [optional] 
**metric** | **str** | The metric name. | [optional] 
**feature_names** | **List[str]** | Human-readable names of the features. Must be sorted lexicographically. | [optional] 
**subset_name** | **str** | Human-readable name of the feature subset used for the &#x60;subset_name&#x60; field. This is used to display the subset name on the frontend. | [optional] 

## Example

```python
from ri.apiclient.models.subset_test_metric_identifier import SubsetTestMetricIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of SubsetTestMetricIdentifier from a JSON string
subset_test_metric_identifier_instance = SubsetTestMetricIdentifier.from_json(json)
# print the JSON string representation of the object
print(SubsetTestMetricIdentifier.to_json())

# convert the object into a dict
subset_test_metric_identifier_dict = subset_test_metric_identifier_instance.to_dict()
# create an instance of SubsetTestMetricIdentifier from a dict
subset_test_metric_identifier_from_dict = SubsetTestMetricIdentifier.from_dict(subset_test_metric_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

