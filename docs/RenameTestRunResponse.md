# RenameTestRunResponse

RenameTestRunResponse returns the renamed test run as requested.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_run** | [**TestRunDetail**](TestRunDetail.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.rename_test_run_response import RenameTestRunResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RenameTestRunResponse from a JSON string
rename_test_run_response_instance = RenameTestRunResponse.from_json(json)
# print the JSON string representation of the object
print(RenameTestRunResponse.to_json())

# convert the object into a dict
rename_test_run_response_dict = rename_test_run_response_instance.to_dict()
# create an instance of RenameTestRunResponse from a dict
rename_test_run_response_from_dict = RenameTestRunResponse.from_dict(rename_test_run_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

