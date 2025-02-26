# TestCaseDisplay

Display contains information for displaying the test case in the web UI. The contents of each field are unstable; it is not recommended to parse them programmatically.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_info** | **bytearray** | Table info contains information for displaying the test case in a table in the FE. | [optional] 
**details** | **bytearray** | Details includes ML-specified details for the test case. This can include graphs, HTML, etc. | [optional] 
**details_layout** | **List[str]** |  | [optional] 

## Example

```python
from ri.apiclient.models.test_case_display import TestCaseDisplay

# TODO update the JSON string below
json = "{}"
# create an instance of TestCaseDisplay from a JSON string
test_case_display_instance = TestCaseDisplay.from_json(json)
# print the JSON string representation of the object
print(TestCaseDisplay.to_json())

# convert the object into a dict
test_case_display_dict = test_case_display_instance.to_dict()
# create an instance of TestCaseDisplay from a dict
test_case_display_from_dict = TestCaseDisplay.from_dict(test_case_display_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

