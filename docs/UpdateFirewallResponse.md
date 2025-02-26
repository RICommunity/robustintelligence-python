# UpdateFirewallResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firewall** | [**Firewall**](Firewall.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.update_firewall_response import UpdateFirewallResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFirewallResponse from a JSON string
update_firewall_response_instance = UpdateFirewallResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateFirewallResponse.to_json())

# convert the object into a dict
update_firewall_response_dict = update_firewall_response_instance.to_dict()
# create an instance of UpdateFirewallResponse from a dict
update_firewall_response_from_dict = UpdateFirewallResponse.from_dict(update_firewall_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

