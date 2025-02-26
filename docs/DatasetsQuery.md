# DatasetsQuery

DatasetsQuery is used to filter all datasets within a specified time range and firewall ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firewall_id** | [**ID**](ID.md) |  | [optional] 
**scheduled_ct_intervals** | [**TimeInterval**](TimeInterval.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.datasets_query import DatasetsQuery

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetsQuery from a JSON string
datasets_query_instance = DatasetsQuery.from_json(json)
# print the JSON string representation of the object
print(DatasetsQuery.to_json())

# convert the object into a dict
datasets_query_dict = datasets_query_instance.to_dict()
# create an instance of DatasetsQuery from a dict
datasets_query_from_dict = DatasetsQuery.from_dict(datasets_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

