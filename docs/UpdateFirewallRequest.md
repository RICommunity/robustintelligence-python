# UpdateFirewallRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firewall_id** | [**ID**](ID.md) |  | 
**firewall** | [**UpdateFirewallRequestFirewall**](UpdateFirewallRequestFirewall.md) |  | [optional] 
**mask** | **str** | Field mask specifies which fields of the firewall to update. | [optional] 

## Example

```python
from ri.apiclient.models.update_firewall_request import UpdateFirewallRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFirewallRequest from a JSON string
update_firewall_request_instance = UpdateFirewallRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateFirewallRequest.to_json())

# convert the object into a dict
update_firewall_request_dict = update_firewall_request_instance.to_dict()
# create an instance of UpdateFirewallRequest from a dict
update_firewall_request_from_dict = UpdateFirewallRequest.from_dict(update_firewall_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

