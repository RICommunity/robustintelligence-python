# Transform


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**difference_from_target** | [**DifferenceFromTarget**](DifferenceFromTarget.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.transform import Transform

# TODO update the JSON string below
json = "{}"
# create an instance of Transform from a JSON string
transform_instance = Transform.from_json(json)
# print the JSON string representation of the object
print(Transform.to_json())

# convert the object into a dict
transform_dict = transform_instance.to_dict()
# create an instance of Transform from a dict
transform_from_dict = Transform.from_dict(transform_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

