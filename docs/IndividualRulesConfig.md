# IndividualRulesConfig

IndividualRulesConfig contains configuration parameters for each individual rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**off_topic** | [**OffTopicRuleConfig**](OffTopicRuleConfig.md) |  | [optional] 
**pii_detection_input** | [**PiiDetectionRuleConfig**](PiiDetectionRuleConfig.md) |  | [optional] 
**pii_detection_output** | [**PiiDetectionRuleConfig**](PiiDetectionRuleConfig.md) |  | [optional] 
**token_counter_input** | [**TokenCounterRuleConfig**](TokenCounterRuleConfig.md) |  | [optional] 
**token_counter_output** | [**TokenCounterRuleConfig**](TokenCounterRuleConfig.md) |  | [optional] 
**unknown_external_source** | [**UnknownExternalSourceRuleConfig**](UnknownExternalSourceRuleConfig.md) |  | [optional] 
**language_detection** | [**LanguageDetectionRuleConfig**](LanguageDetectionRuleConfig.md) |  | [optional] 
**prompt_injection** | [**PromptInjectionRuleConfig**](PromptInjectionRuleConfig.md) |  | [optional] 
**toxicity_rule_config_input** | [**ToxicityRuleConfig**](ToxicityRuleConfig.md) |  | [optional] 
**toxicity_rule_config_output** | [**ToxicityRuleConfig**](ToxicityRuleConfig.md) |  | [optional] 
**code_detection** | [**CodeDetectionRuleConfig**](CodeDetectionRuleConfig.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.individual_rules_config import IndividualRulesConfig

# TODO update the JSON string below
json = "{}"
# create an instance of IndividualRulesConfig from a JSON string
individual_rules_config_instance = IndividualRulesConfig.from_json(json)
# print the JSON string representation of the object
print(IndividualRulesConfig.to_json())

# convert the object into a dict
individual_rules_config_dict = individual_rules_config_instance.to_dict()
# create an instance of IndividualRulesConfig from a dict
individual_rules_config_from_dict = IndividualRulesConfig.from_dict(individual_rules_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

