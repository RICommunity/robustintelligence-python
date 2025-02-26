# GetResultsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[GenerativeValidationResult]**](GenerativeValidationResult.md) | The list of generative testing results. | [optional] 
**next_page_token** | **str** | A token representing the next page from the list returned by a query. | [optional] 
**has_more** | **bool** | A Boolean flag that specifies whether there are more results to return. | [optional] 
**job_id** | [**ID**](ID.md) |  | [optional] 
**job_status** | [**JobStatus**](JobStatus.md) |  | [optional] [default to JobStatus.UNSPECIFIED]

## Example

```python
from ri.apiclient.models.get_results_response import GetResultsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetResultsResponse from a JSON string
get_results_response_instance = GetResultsResponse.from_json(json)
# print the JSON string representation of the object
print(GetResultsResponse.to_json())

# convert the object into a dict
get_results_response_dict = get_results_response_instance.to_dict()
# create an instance of GetResultsResponse from a dict
get_results_response_from_dict = GetResultsResponse.from_dict(get_results_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

