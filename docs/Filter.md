# Filter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**included_monitor_types** | [**List[MonitorType]**](MonitorType.md) | Specifies a list of monitor types. Filters results to match the specified monitor types. | [optional] 
**included_risk_category_types** | [**List[RiskCategoryType]**](RiskCategoryType.md) | Specifies a list of risk category types. Filters results to match the specified risk category types. | [optional] 
**pinned_monitors_only** | **bool** | When the value of this Boolean is True, this endpoint returns a list of pinned Monitors. Otherwise, this endpoint does not filter Monitors by pinned status. | [optional] 

## Example

```python
from ri.apiclient.models.filter import Filter

# TODO update the JSON string below
json = "{}"
# create an instance of Filter from a JSON string
filter_instance = Filter.from_json(json)
# print the JSON string representation of the object
print(Filter.to_json())

# convert the object into a dict
filter_dict = filter_instance.to_dict()
# create an instance of Filter from a dict
filter_from_dict = Filter.from_dict(filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

