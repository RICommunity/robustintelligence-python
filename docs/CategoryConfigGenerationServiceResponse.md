# CategoryConfigGenerationServiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stress_test_categories** | [**List[TestCategoryType]**](TestCategoryType.md) |  | [optional] 
**continuous_test_categories** | [**List[TestCategoryType]**](TestCategoryType.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.category_config_generation_service_response import CategoryConfigGenerationServiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryConfigGenerationServiceResponse from a JSON string
category_config_generation_service_response_instance = CategoryConfigGenerationServiceResponse.from_json(json)
# print the JSON string representation of the object
print(CategoryConfigGenerationServiceResponse.to_json())

# convert the object into a dict
category_config_generation_service_response_dict = category_config_generation_service_response_instance.to_dict()
# create an instance of CategoryConfigGenerationServiceResponse from a dict
category_config_generation_service_response_from_dict = CategoryConfigGenerationServiceResponse.from_dict(category_config_generation_service_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

