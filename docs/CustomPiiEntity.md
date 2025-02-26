# CustomPiiEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the entity type. | [optional] 
**patterns** | **List[str]** | The regex patterns to match against for this entity. | [optional] 
**context_words** | **List[str]** | Words to use as context that will boost the score if detected around the matching entity. These words are case-insensitive. | [optional] 

## Example

```python
from ri.apiclient.models.custom_pii_entity import CustomPiiEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CustomPiiEntity from a JSON string
custom_pii_entity_instance = CustomPiiEntity.from_json(json)
# print the JSON string representation of the object
print(CustomPiiEntity.to_json())

# convert the object into a dict
custom_pii_entity_dict = custom_pii_entity_instance.to_dict()
# create an instance of CustomPiiEntity from a dict
custom_pii_entity_from_dict = CustomPiiEntity.from_dict(custom_pii_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

