# CreateFirewallResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firewall_id** | [**ID**](ID.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.create_firewall_response import CreateFirewallResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFirewallResponse from a JSON string
create_firewall_response_instance = CreateFirewallResponse.from_json(json)
# print the JSON string representation of the object
print(CreateFirewallResponse.to_json())

# convert the object into a dict
create_firewall_response_dict = create_firewall_response_instance.to_dict()
# create an instance of CreateFirewallResponse from a dict
create_firewall_response_from_dict = CreateFirewallResponse.from_dict(create_firewall_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

