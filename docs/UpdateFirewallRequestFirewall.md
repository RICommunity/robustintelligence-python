# UpdateFirewallRequestFirewall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firewall_id** | **object** | Unique ID of an object in RIME. | [optional] 
**project_id** | [**ID**](ID.md) |  | [optional] 
**model_id** | [**ID**](ID.md) |  | [optional] 
**bin_size** | **str** |  | [optional] 
**ref_data_id** | **str** | The semantic ID of the reference dataset. This should correspond with the primary key in the Dataset Registry. | [optional] 
**scheduled_ct_info** | [**ScheduledCTInfo**](ScheduledCTInfo.md) |  | [optional] 
**risk_scores** | [**List[RiskScore]**](RiskScore.md) |  | [optional] 
**test_category_severities** | [**List[TestCategorySeverity]**](TestCategorySeverity.md) |  | [optional] 
**latest_run_info** | [**LatestRunInfo**](LatestRunInfo.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.update_firewall_request_firewall import UpdateFirewallRequestFirewall

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFirewallRequestFirewall from a JSON string
update_firewall_request_firewall_instance = UpdateFirewallRequestFirewall.from_json(json)
# print the JSON string representation of the object
print(UpdateFirewallRequestFirewall.to_json())

# convert the object into a dict
update_firewall_request_firewall_dict = update_firewall_request_firewall_instance.to_dict()
# create an instance of UpdateFirewallRequestFirewall from a dict
update_firewall_request_firewall_from_dict = UpdateFirewallRequestFirewall.from_dict(update_firewall_request_firewall_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

