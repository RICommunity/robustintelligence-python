# TableColumn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | [**TableColumnType**](TableColumnType.md) |  | [optional] [default to TableColumnType.UNSPECIFIED]

## Example

```python
from ri.apiclient.models.table_column import TableColumn

# TODO update the JSON string below
json = "{}"
# create an instance of TableColumn from a JSON string
table_column_instance = TableColumn.from_json(json)
# print the JSON string representation of the object
print(TableColumn.to_json())

# convert the object into a dict
table_column_dict = table_column_instance.to_dict()
# create an instance of TableColumn from a dict
table_column_from_dict = TableColumn.from_dict(table_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

