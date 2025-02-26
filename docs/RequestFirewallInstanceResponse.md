# RequestFirewallInstanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firewall_instance_id** | [**ID**](ID.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.request_firewall_instance_response import RequestFirewallInstanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RequestFirewallInstanceResponse from a JSON string
request_firewall_instance_response_instance = RequestFirewallInstanceResponse.from_json(json)
# print the JSON string representation of the object
print(RequestFirewallInstanceResponse.to_json())

# convert the object into a dict
request_firewall_instance_response_dict = request_firewall_instance_response_instance.to_dict()
# create an instance of RequestFirewallInstanceResponse from a dict
request_firewall_instance_response_from_dict = RequestFirewallInstanceResponse.from_dict(request_firewall_instance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

