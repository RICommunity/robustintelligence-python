# CreateFirewallRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | [**ID**](ID.md) |  | 
**model_id** | [**ID**](ID.md) |  | 
**bin_size** | **str** | Duration of each bin size of continuous tests. | 
**ref_data_id** | **str** | Uniquely specifies a reference data set. | 
**scheduled_ct_parameters** | [**ScheduledCTParameters**](ScheduledCTParameters.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.create_firewall_request import CreateFirewallRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFirewallRequest from a JSON string
create_firewall_request_instance = CreateFirewallRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFirewallRequest.to_json())

# convert the object into a dict
create_firewall_request_dict = create_firewall_request_instance.to_dict()
# create an instance of CreateFirewallRequest from a dict
create_firewall_request_from_dict = CreateFirewallRequest.from_dict(create_firewall_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

