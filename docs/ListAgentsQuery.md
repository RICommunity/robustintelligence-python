# ListAgentsQuery

This query can filter the results by agent status types, such as AGENT_STATUS_ACTIVE, and by agent IDs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_status_types** | [**List[AgentStatus]**](AgentStatus.md) | Specifies a set of agent status types. The query filters for results that match the specified types. | [optional] 
**agent_ids** | **List[str]** | Specifies a set of agent IDs. The query filters for results that match the specified IDs. | [optional] 
**type** | [**AgentType**](AgentType.md) |  | [optional] [default to AgentType.VALIDATION]

## Example

```python
from ri.apiclient.models.list_agents_query import ListAgentsQuery

# TODO update the JSON string below
json = "{}"
# create an instance of ListAgentsQuery from a JSON string
list_agents_query_instance = ListAgentsQuery.from_json(json)
# print the JSON string representation of the object
print(ListAgentsQuery.to_json())

# convert the object into a dict
list_agents_query_dict = list_agents_query_instance.to_dict()
# create an instance of ListAgentsQuery from a dict
list_agents_query_from_dict = ListAgentsQuery.from_dict(list_agents_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

