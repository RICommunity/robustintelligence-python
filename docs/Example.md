# Example


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attack_prompt** | **str** | RI attack prompt to elicit issues. | [optional] 
**model_output** | **str** | Output from the generative model on the given prompt. | [optional] 
**detection_context** | **str** | Additional information about the example, such as copyright text.  This will evaluate to a valid JSON string. | [optional] 

## Example

```python
from ri.apiclient.models.example import Example

# TODO update the JSON string below
json = "{}"
# create an instance of Example from a JSON string
example_instance = Example.from_json(json)
# print the JSON string representation of the object
print(Example.to_json())

# convert the object into a dict
example_dict = example_instance.to_dict()
# create an instance of Example from a dict
example_from_dict = Example.from_dict(example_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

