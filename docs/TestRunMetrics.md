# TestRunMetrics

TestRunMetrics returns metrics for a test run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_perf** | [**Dict[str, ModelPerfMetric]**](ModelPerfMetric.md) | The model performance over the test run as computed using various metrics. | [optional] 
**average_prediction** | **float** | The average prediction for the test run (only defined for a subset of tasks such as binary classification). | [optional] 
**num_inputs** | **str** | The number of inputs. For tabular data, an input is one row. | [optional] 
**num_failing_inputs** | **str** | The number of failing inputs. | [optional] 
**duration_millis** | **str** | The duration of the test run in milliseconds. | [optional] 
**severity_counts** | [**SeverityCounts**](SeverityCounts.md) |  | [optional] 
**summary_counts** | [**ResultSummaryCounts**](ResultSummaryCounts.md) |  | [optional] 
**category_summary_metrics** | [**List[CategorySummaryMetric]**](CategorySummaryMetric.md) | The list of category summary metrics. | [optional] 
**risk_scores** | [**List[RiskScore]**](RiskScore.md) | The list of risk scores. | [optional] 

## Example

```python
from ri.apiclient.models.test_run_metrics import TestRunMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunMetrics from a JSON string
test_run_metrics_instance = TestRunMetrics.from_json(json)
# print the JSON string representation of the object
print(TestRunMetrics.to_json())

# convert the object into a dict
test_run_metrics_dict = test_run_metrics_instance.to_dict()
# create an instance of TestRunMetrics from a dict
test_run_metrics_from_dict = TestRunMetrics.from_dict(test_run_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

