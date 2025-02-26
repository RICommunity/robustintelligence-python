# ListProjectsResponse

ListProjectsResponse returns a list of Projects as requested.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projects** | [**List[ProjectWithDetails]**](ProjectWithDetails.md) |  | [optional] 
**next_page_token** | **str** | A token representing the next page from the list returned by a ListProjects query. | [optional] 
**has_more** | **bool** | A Boolean that specifies whether there are more Projects to return. | [optional] 

## Example

```python
from ri.apiclient.models.list_projects_response import ListProjectsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListProjectsResponse from a JSON string
list_projects_response_instance = ListProjectsResponse.from_json(json)
# print the JSON string representation of the object
print(ListProjectsResponse.to_json())

# convert the object into a dict
list_projects_response_dict = list_projects_response_instance.to_dict()
# create an instance of ListProjectsResponse from a dict
list_projects_response_from_dict = ListProjectsResponse.from_dict(list_projects_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

