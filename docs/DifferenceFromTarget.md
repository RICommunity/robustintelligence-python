# DifferenceFromTarget

DifferenceFromTarget defines a transform that calculates the difference between the aggregated metric defined in the monitor and the same metric defined with the target. if no aggregation is specified, an average value is used.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**difference** | [**Difference**](Difference.md) |  | [optional] [default to Difference.UNSPECIFIED]
**target** | [**Target**](Target.md) |  | [optional] [default to Target.UNSPECIFIED]

## Example

```python
from ri.apiclient.models.difference_from_target import DifferenceFromTarget

# TODO update the JSON string below
json = "{}"
# create an instance of DifferenceFromTarget from a JSON string
difference_from_target_instance = DifferenceFromTarget.from_json(json)
# print the JSON string representation of the object
print(DifferenceFromTarget.to_json())

# convert the object into a dict
difference_from_target_dict = difference_from_target_instance.to_dict()
# create an instance of DifferenceFromTarget from a dict
difference_from_target_from_dict = DifferenceFromTarget.from_dict(difference_from_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

