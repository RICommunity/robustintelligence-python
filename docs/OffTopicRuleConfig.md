# OffTopicRuleConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**in_domain_intents** | **List[str]** | In_domain_intents is a list of strings that are considered on-topic. Total number of data points in in_domain_intents and restricted_intents should not exceed 500 and total bytes should not exceed 300KB. | [optional] 
**restricted_intents** | **List[str]** |  | [optional] 
**in_domain_intents_sensitivity** | [**RuleSensitivity**](RuleSensitivity.md) |  | [optional] [default to RuleSensitivity.UNSPECIFIED]
**restricted_intents_sensitivity** | [**RuleSensitivity**](RuleSensitivity.md) |  | [optional] [default to RuleSensitivity.UNSPECIFIED]

## Example

```python
from ri.apiclient.models.off_topic_rule_config import OffTopicRuleConfig

# TODO update the JSON string below
json = "{}"
# create an instance of OffTopicRuleConfig from a JSON string
off_topic_rule_config_instance = OffTopicRuleConfig.from_json(json)
# print the JSON string representation of the object
print(OffTopicRuleConfig.to_json())

# convert the object into a dict
off_topic_rule_config_dict = off_topic_rule_config_instance.to_dict()
# create an instance of OffTopicRuleConfig from a dict
off_topic_rule_config_from_dict = OffTopicRuleConfig.from_dict(
    off_topic_rule_config_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

