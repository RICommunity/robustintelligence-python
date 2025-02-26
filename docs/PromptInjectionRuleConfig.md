# PromptInjectionRuleConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt_injection_rule_sensitivity** | [**RuleSensitivity**](RuleSensitivity.md) |  | [optional] [default to RuleSensitivity.UNSPECIFIED]

## Example

```python
from ri.apiclient.models.prompt_injection_rule_config import PromptInjectionRuleConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PromptInjectionRuleConfig from a JSON string
prompt_injection_rule_config_instance = PromptInjectionRuleConfig.from_json(json)
# print the JSON string representation of the object
print(PromptInjectionRuleConfig.to_json())

# convert the object into a dict
prompt_injection_rule_config_dict = prompt_injection_rule_config_instance.to_dict()
# create an instance of PromptInjectionRuleConfig from a dict
prompt_injection_rule_config_from_dict = PromptInjectionRuleConfig.from_dict(prompt_injection_rule_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

