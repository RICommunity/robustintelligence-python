# FailingRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_id** | **str** |  | [optional] 
**failing_features** | **List[str]** |  | [optional] 
**details** | **bytearray** |  | [optional] 

## Example

```python
from ri.apiclient.models.failing_row import FailingRow

# TODO update the JSON string below
json = "{}"
# create an instance of FailingRow from a JSON string
failing_row_instance = FailingRow.from_json(json)
# print the JSON string representation of the object
print(FailingRow.to_json())

# convert the object into a dict
failing_row_dict = failing_row_instance.to_dict()
# create an instance of FailingRow from a dict
failing_row_from_dict = FailingRow.from_dict(failing_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

