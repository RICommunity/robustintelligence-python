# ListFirewallInstancesQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_ids** | **List[str]** | Specifies a set of agent IDs. The query filters for firewall instances that belong to the specified agents. | [optional] 
**deployment_status** | [**FirewallInstanceStatus**](FirewallInstanceStatus.md) |  | [optional] [default to FirewallInstanceStatus.UNSPECIFIED]

## Example

```python
from ri.apiclient.models.list_firewall_instances_query import ListFirewallInstancesQuery

# TODO update the JSON string below
json = "{}"
# create an instance of ListFirewallInstancesQuery from a JSON string
list_firewall_instances_query_instance = ListFirewallInstancesQuery.from_json(json)
# print the JSON string representation of the object
print(ListFirewallInstancesQuery.to_json())

# convert the object into a dict
list_firewall_instances_query_dict = list_firewall_instances_query_instance.to_dict()
# create an instance of ListFirewallInstancesQuery from a dict
list_firewall_instances_query_from_dict = ListFirewallInstancesQuery.from_dict(list_firewall_instances_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

