# GetFirewallResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firewall** | [**Firewall**](Firewall.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.get_firewall_response import GetFirewallResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFirewallResponse from a JSON string
get_firewall_response_instance = GetFirewallResponse.from_json(json)
# print the JSON string representation of the object
print(GetFirewallResponse.to_json())

# convert the object into a dict
get_firewall_response_dict = get_firewall_response_instance.to_dict()
# create an instance of GetFirewallResponse from a dict
get_firewall_response_from_dict = GetFirewallResponse.from_dict(get_firewall_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

