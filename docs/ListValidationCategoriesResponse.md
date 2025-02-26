# ListValidationCategoriesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**List[TestCategoryType]**](TestCategoryType.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.list_validation_categories_response import ListValidationCategoriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListValidationCategoriesResponse from a JSON string
list_validation_categories_response_instance = ListValidationCategoriesResponse.from_json(json)
# print the JSON string representation of the object
print(ListValidationCategoriesResponse.to_json())

# convert the object into a dict
list_validation_categories_response_dict = list_validation_categories_response_instance.to_dict()
# create an instance of ListValidationCategoriesResponse from a dict
list_validation_categories_response_from_dict = ListValidationCategoriesResponse.from_dict(list_validation_categories_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

