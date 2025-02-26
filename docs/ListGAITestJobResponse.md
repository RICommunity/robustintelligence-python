# ListGAITestJobResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | [**List[JobMetadata]**](JobMetadata.md) |  | [optional] 
**next_page_token** | **str** | Use this page token in your next ListJobs call to access the next page of results. | [optional] 
**has_more** | **bool** |  | [optional] 

## Example

```python
from ri.apiclient.models.list_gai_test_job_response import ListGAITestJobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListGAITestJobResponse from a JSON string
list_gai_test_job_response_instance = ListGAITestJobResponse.from_json(json)
# print the JSON string representation of the object
print(ListGAITestJobResponse.to_json())

# convert the object into a dict
list_gai_test_job_response_dict = list_gai_test_job_response_instance.to_dict()
# create an instance of ListGAITestJobResponse from a dict
list_gai_test_job_response_from_dict = ListGAITestJobResponse.from_dict(list_gai_test_job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

