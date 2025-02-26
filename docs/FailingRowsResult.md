# FailingRowsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failing_rows** | [**List[FailingRow]**](FailingRow.md) |  | [optional] 
**top_count** | **str** |  | [optional] 
**total_count** | **str** |  | [optional] 
**all_included** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from ri.apiclient.models.failing_rows_result import FailingRowsResult

# TODO update the JSON string below
json = "{}"
# create an instance of FailingRowsResult from a JSON string
failing_rows_result_instance = FailingRowsResult.from_json(json)
# print the JSON string representation of the object
print(FailingRowsResult.to_json())

# convert the object into a dict
failing_rows_result_dict = failing_rows_result_instance.to_dict()
# create an instance of FailingRowsResult from a dict
failing_rows_result_from_dict = FailingRowsResult.from_dict(failing_rows_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

