# ListMonitorCategoriesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**List[TestCategoryType]**](TestCategoryType.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.list_monitor_categories_response import (
    ListMonitorCategoriesResponse,
)

# TODO update the JSON string below
json = "{}"
# create an instance of ListMonitorCategoriesResponse from a JSON string
list_monitor_categories_response_instance = ListMonitorCategoriesResponse.from_json(
    json
)
# print the JSON string representation of the object
print(ListMonitorCategoriesResponse.to_json())

# convert the object into a dict
list_monitor_categories_response_dict = (
    list_monitor_categories_response_instance.to_dict()
)
# create an instance of ListMonitorCategoriesResponse from a dict
list_monitor_categories_response_from_dict = ListMonitorCategoriesResponse.from_dict(
    list_monitor_categories_response_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

