# ListGAITestJobsRequestQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_statuses** | [**List[JobStatus]**](JobStatus.md) | Specifies a set of statuses. The query only returns results with a status in the specified set. Specify no statuses to return all results. | [optional] 

## Example

```python
from ri.apiclient.models.list_gai_test_jobs_request_query import ListGAITestJobsRequestQuery

# TODO update the JSON string below
json = "{}"
# create an instance of ListGAITestJobsRequestQuery from a JSON string
list_gai_test_jobs_request_query_instance = ListGAITestJobsRequestQuery.from_json(json)
# print the JSON string representation of the object
print(ListGAITestJobsRequestQuery.to_json())

# convert the object into a dict
list_gai_test_jobs_request_query_dict = list_gai_test_jobs_request_query_instance.to_dict()
# create an instance of ListGAITestJobsRequestQuery from a dict
list_gai_test_jobs_request_query_from_dict = ListGAITestJobsRequestQuery.from_dict(list_gai_test_jobs_request_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

