# ResultSummaryCounts

ResultSummaryCounts returns the number of tests that have each status for a given test run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **str** | The total number of tests. | [optional] 
**var_pass** | **str** | The number of tests that pass. | [optional] 
**warning** | **str** | The number of tests that raise a warning. | [optional] 
**fail** | **str** | The number of tests that fail. | [optional] 
**skip** | **str** | The number of tests that are skipped. | [optional] 

## Example

```python
from ri.apiclient.models.result_summary_counts import ResultSummaryCounts

# TODO update the JSON string below
json = "{}"
# create an instance of ResultSummaryCounts from a JSON string
result_summary_counts_instance = ResultSummaryCounts.from_json(json)
# print the JSON string representation of the object
print(ResultSummaryCounts.to_json())

# convert the object into a dict
result_summary_counts_dict = result_summary_counts_instance.to_dict()
# create an instance of ResultSummaryCounts from a dict
result_summary_counts_from_dict = ResultSummaryCounts.from_dict(result_summary_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

