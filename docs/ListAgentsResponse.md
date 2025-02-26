# ListAgentsResponse

ListAgentsResponse returns the list of agent metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents** | [**List[Agent]**](Agent.md) |  | [optional] 
**next_page_token** | **str** | Use this page token in your next ListAgents call to access to the next page of results. | [optional] 
**has_more** | **bool** |  | [optional] 

## Example

```python
from ri.apiclient.models.list_agents_response import ListAgentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAgentsResponse from a JSON string
list_agents_response_instance = ListAgentsResponse.from_json(json)
# print the JSON string representation of the object
print(ListAgentsResponse.to_json())

# convert the object into a dict
list_agents_response_dict = list_agents_response_instance.to_dict()
# create an instance of ListAgentsResponse from a dict
list_agents_response_from_dict = ListAgentsResponse.from_dict(list_agents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

