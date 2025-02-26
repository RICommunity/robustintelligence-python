# ToxicityRuleConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**toxicity_rule_sensitivity** | [**RuleSensitivity**](RuleSensitivity.md) |  | [optional] [default to RuleSensitivity.UNSPECIFIED]
**toxicity_rule_mode** | [**ToxicityRuleMode**](ToxicityRuleMode.md) |  | [optional] [default to ToxicityRuleMode.ADVANCED]

## Example

```python
from ri.apiclient.models.toxicity_rule_config import ToxicityRuleConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ToxicityRuleConfig from a JSON string
toxicity_rule_config_instance = ToxicityRuleConfig.from_json(json)
# print the JSON string representation of the object
print(ToxicityRuleConfig.to_json())

# convert the object into a dict
toxicity_rule_config_dict = toxicity_rule_config_instance.to_dict()
# create an instance of ToxicityRuleConfig from a dict
toxicity_rule_config_from_dict = ToxicityRuleConfig.from_dict(toxicity_rule_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

