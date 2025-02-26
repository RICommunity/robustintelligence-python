# CategoryTestIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_category** | [**TestCategoryType**](TestCategoryType.md) |  | [optional] [default to TestCategoryType.UNSPECIFIED]
**metric** | **str** | The metric name. | [optional] 

## Example

```python
from ri.apiclient.models.category_test_identifier import CategoryTestIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryTestIdentifier from a JSON string
category_test_identifier_instance = CategoryTestIdentifier.from_json(json)
# print the JSON string representation of the object
print(CategoryTestIdentifier.to_json())

# convert the object into a dict
category_test_identifier_dict = category_test_identifier_instance.to_dict()
# create an instance of CategoryTestIdentifier from a dict
category_test_identifier_from_dict = CategoryTestIdentifier.from_dict(category_test_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

