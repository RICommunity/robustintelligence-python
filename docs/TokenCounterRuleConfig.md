# TokenCounterRuleConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firewall_tokenizer** | [**FirewallTokenizer**](FirewallTokenizer.md) |  | [optional] [default to FirewallTokenizer.UNSPECIFIED]
**max_tokens** | **str** | The maximum number of tokens allowed in the model input/outputs. | [optional] 

## Example

```python
from ri.apiclient.models.token_counter_rule_config import TokenCounterRuleConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TokenCounterRuleConfig from a JSON string
token_counter_rule_config_instance = TokenCounterRuleConfig.from_json(json)
# print the JSON string representation of the object
print(TokenCounterRuleConfig.to_json())

# convert the object into a dict
token_counter_rule_config_dict = token_counter_rule_config_instance.to_dict()
# create an instance of TokenCounterRuleConfig from a dict
token_counter_rule_config_from_dict = TokenCounterRuleConfig.from_dict(token_counter_rule_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

