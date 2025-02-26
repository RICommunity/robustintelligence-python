# LanguageDetectionRuleConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**whitelisted_languages** | [**List[Language]**](Language.md) | Whitelisted languages are the languages that are allowed to be present in model input text. | [optional] 

## Example

```python
from ri.apiclient.models.language_detection_rule_config import (
    LanguageDetectionRuleConfig,
)

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageDetectionRuleConfig from a JSON string
language_detection_rule_config_instance = LanguageDetectionRuleConfig.from_json(json)
# print the JSON string representation of the object
print(LanguageDetectionRuleConfig.to_json())

# convert the object into a dict
language_detection_rule_config_dict = language_detection_rule_config_instance.to_dict()
# create an instance of LanguageDetectionRuleConfig from a dict
language_detection_rule_config_from_dict = LanguageDetectionRuleConfig.from_dict(
    language_detection_rule_config_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

