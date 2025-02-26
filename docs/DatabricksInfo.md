# DatabricksInfo

DatabricksInfo provides the information needed to load a Delta Lake table from Databricks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_name** | **str** | The database table name to use. | 

## Example

```python
from ri.apiclient.models.databricks_info import DatabricksInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DatabricksInfo from a JSON string
databricks_info_instance = DatabricksInfo.from_json(json)
# print the JSON string representation of the object
print(DatabricksInfo.to_json())

# convert the object into a dict
databricks_info_dict = databricks_info_instance.to_dict()
# create an instance of DatabricksInfo from a dict
databricks_info_from_dict = DatabricksInfo.from_dict(databricks_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

