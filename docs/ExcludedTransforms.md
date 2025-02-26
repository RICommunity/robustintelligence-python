# ExcludedTransforms

ExcludedTransforms allows a metric to define which transforms cannot be applied to the metric.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excluded_transforms** | [**List[Transform]**](Transform.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.excluded_transforms import ExcludedTransforms

# TODO update the JSON string below
json = "{}"
# create an instance of ExcludedTransforms from a JSON string
excluded_transforms_instance = ExcludedTransforms.from_json(json)
# print the JSON string representation of the object
print(ExcludedTransforms.to_json())

# convert the object into a dict
excluded_transforms_dict = excluded_transforms_instance.to_dict()
# create an instance of ExcludedTransforms from a dict
excluded_transforms_from_dict = ExcludedTransforms.from_dict(excluded_transforms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

