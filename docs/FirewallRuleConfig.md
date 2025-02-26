# FirewallRuleConfig

FirewallRuleConfig describes the firewall rule configuration of the firewall.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | [**Language**](Language.md) |  | [optional] [default to Language.EN]
**selected_rules** | [**List[FirewallRuleType]**](FirewallRuleType.md) | If this list is empty, all available firewall rules will be run. Otherwise, only the rules specified here will be run. | [optional] 
**individual_rules_config** | [**IndividualRulesConfig**](IndividualRulesConfig.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.firewall_rule_config import FirewallRuleConfig

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallRuleConfig from a JSON string
firewall_rule_config_instance = FirewallRuleConfig.from_json(json)
# print the JSON string representation of the object
print(FirewallRuleConfig.to_json())

# convert the object into a dict
firewall_rule_config_dict = firewall_rule_config_instance.to_dict()
# create an instance of FirewallRuleConfig from a dict
firewall_rule_config_from_dict = FirewallRuleConfig.from_dict(firewall_rule_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

