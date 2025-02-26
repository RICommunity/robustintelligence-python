# ListJobsForProjectRequestQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_statuses** | [**List[JobStatus]**](JobStatus.md) | Specifies a set of statuses. The query only returns results with a status in the specified set. Specify no statuses to return all results. | [optional] 
**selected_types** | [**List[JobType]**](JobType.md) | Specifies a set of types. The query only returns jobs with types in the specified set. Specify no types to return all results. Job types not tied to projects will not be returned. | [optional] 
**schedule_id** | [**ID**](ID.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.list_jobs_for_project_request_query import ListJobsForProjectRequestQuery

# TODO update the JSON string below
json = "{}"
# create an instance of ListJobsForProjectRequestQuery from a JSON string
list_jobs_for_project_request_query_instance = ListJobsForProjectRequestQuery.from_json(json)
# print the JSON string representation of the object
print(ListJobsForProjectRequestQuery.to_json())

# convert the object into a dict
list_jobs_for_project_request_query_dict = list_jobs_for_project_request_query_instance.to_dict()
# create an instance of ListJobsForProjectRequestQuery from a dict
list_jobs_for_project_request_query_from_dict = ListJobsForProjectRequestQuery.from_dict(list_jobs_for_project_request_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

