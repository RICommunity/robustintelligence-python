# Filters

Filters provides a mechanism for specifying which attacks to run. An empty set of filters will result in all tests being run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attack_objectives** | [**List[AttackObjective]**](AttackObjective.md) | Only attacks that have one of these attack objectives will be run. If empty, this filter is not applied. | [optional] 

## Example

```python
from ri.apiclient.models.filters import Filters

# TODO update the JSON string below
json = "{}"
# create an instance of Filters from a JSON string
filters_instance = Filters.from_json(json)
# print the JSON string representation of the object
print(Filters.to_json())

# convert the object into a dict
filters_dict = filters_instance.to_dict()
# create an instance of Filters from a dict
filters_from_dict = Filters.from_dict(filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

