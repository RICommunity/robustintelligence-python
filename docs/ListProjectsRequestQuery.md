# ListProjectsRequestQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_published** | **bool** | Optional: If true, return published projects. If false, return unpublished projects. If not specified, return all projects. | [optional] 
**creation_time_range** | [**TimeInterval**](TimeInterval.md) |  | [optional] 
**last_test_run_time_range** | [**TimeInterval**](TimeInterval.md) |  | [optional] 
**stress_test_categories** | [**List[TestCategoryType]**](TestCategoryType.md) | Optional: When specified, return all projects whose ST categories are a superset of the ST categories provided here. | [optional] 
**continuous_test_categories** | [**List[TestCategoryType]**](TestCategoryType.md) | Optional: When specified, return all projects whose CT categories are a superset of the CT categories provided here. | [optional] 
**owner_email** | **str** | Optional: When specified, return all projects whose owner email matches. | [optional] 
**model_tasks** | [**List[ModelTask]**](ModelTask.md) | Optional: When specified, return all projects whose model task is the provided model task. | [optional] 
**status** | [**ProjectStatus**](ProjectStatus.md) |  | [optional] [default to ProjectStatus.UNSPECIFIED]
**sort** | [**SortSpec**](SortSpec.md) |  | [optional] 
**search** | [**SearchSpec**](SearchSpec.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.list_projects_request_query import ListProjectsRequestQuery

# TODO update the JSON string below
json = "{}"
# create an instance of ListProjectsRequestQuery from a JSON string
list_projects_request_query_instance = ListProjectsRequestQuery.from_json(json)
# print the JSON string representation of the object
print(ListProjectsRequestQuery.to_json())

# convert the object into a dict
list_projects_request_query_dict = list_projects_request_query_instance.to_dict()
# create an instance of ListProjectsRequestQuery from a dict
list_projects_request_query_from_dict = ListProjectsRequestQuery.from_dict(
    list_projects_request_query_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

