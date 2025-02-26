# ListJobsForProjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | [**List[JobMetadata]**](JobMetadata.md) |  | [optional] 
**next_page_token** | **str** | Use this page token in your next ListJobs call to access the next page of results. | [optional] 
**has_more** | **bool** |  | [optional] 

## Example

```python
from ri.apiclient.models.list_jobs_for_project_response import (
    ListJobsForProjectResponse,
)

# TODO update the JSON string below
json = "{}"
# create an instance of ListJobsForProjectResponse from a JSON string
list_jobs_for_project_response_instance = ListJobsForProjectResponse.from_json(json)
# print the JSON string representation of the object
print(ListJobsForProjectResponse.to_json())

# convert the object into a dict
list_jobs_for_project_response_dict = list_jobs_for_project_response_instance.to_dict()
# create an instance of ListJobsForProjectResponse from a dict
list_jobs_for_project_response_from_dict = ListJobsForProjectResponse.from_dict(
    list_jobs_for_project_response_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

