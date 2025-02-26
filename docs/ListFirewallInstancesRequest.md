# ListFirewallInstancesRequest

ListFirewallInstancesRequest is the request to list firewall instance metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_size** | **str** |  | [optional] 
**page_token** | **str** | Specifies a page of the list returned by a ListFirewallInstances query. The ListFirewallInstances query returns a pageToken when there is more than one page of results. Specify either this field or the firstPageQuery field. | [optional] 
**first_page_query** | [**ListFirewallInstancesQuery**](ListFirewallInstancesQuery.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.list_firewall_instances_request import ListFirewallInstancesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListFirewallInstancesRequest from a JSON string
list_firewall_instances_request_instance = ListFirewallInstancesRequest.from_json(json)
# print the JSON string representation of the object
print(ListFirewallInstancesRequest.to_json())

# convert the object into a dict
list_firewall_instances_request_dict = list_firewall_instances_request_instance.to_dict()
# create an instance of ListFirewallInstancesRequest from a dict
list_firewall_instances_request_from_dict = ListFirewallInstancesRequest.from_dict(list_firewall_instances_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

