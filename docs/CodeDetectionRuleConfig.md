# CodeDetectionRuleConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**malicious** | **bool** | Whether the rule only checks for malicious code. | [optional] 
**ignore_contexts** | **bool** | Ignore contexts specifies whether the firewall should skip the contexts field of the model input in the firewall validate request. | [optional] 

## Example

```python
from ri.apiclient.models.code_detection_rule_config import CodeDetectionRuleConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CodeDetectionRuleConfig from a JSON string
code_detection_rule_config_instance = CodeDetectionRuleConfig.from_json(json)
# print the JSON string representation of the object
print(CodeDetectionRuleConfig.to_json())

# convert the object into a dict
code_detection_rule_config_dict = code_detection_rule_config_instance.to_dict()
# create an instance of CodeDetectionRuleConfig from a dict
code_detection_rule_config_from_dict = CodeDetectionRuleConfig.from_dict(code_detection_rule_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

