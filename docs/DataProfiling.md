# DataProfiling

Specifies configuration values for profiling a dataset.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_quantiles** | **str** | The number of quantiles to split numeric subsets into. | [optional] 
**num_subsets** | **str** | The number of subsets to test. This field is sorted by count. | [optional] 
**column_type_info** | [**ColumnTypeInfo**](ColumnTypeInfo.md) |  | [optional] 
**feature_relationship_info** | [**FeatureRelationshipInfo**](FeatureRelationshipInfo.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.data_profiling import DataProfiling

# TODO update the JSON string below
json = "{}"
# create an instance of DataProfiling from a JSON string
data_profiling_instance = DataProfiling.from_json(json)
# print the JSON string representation of the object
print(DataProfiling.to_json())

# convert the object into a dict
data_profiling_dict = data_profiling_instance.to_dict()
# create an instance of DataProfiling from a dict
data_profiling_from_dict = DataProfiling.from_dict(data_profiling_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

