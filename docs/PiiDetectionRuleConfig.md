# PiiDetectionRuleConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_types** | [**List[PiiEntityType]**](PiiEntityType.md) | Entity types determines which types of PII will be flagged. | [optional] 
**custom_entities** | [**List[CustomPiiEntity]**](CustomPiiEntity.md) | Custom entities are custom-specified patterns to flag. | [optional] 

## Example

```python
from ri.apiclient.models.pii_detection_rule_config import PiiDetectionRuleConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PiiDetectionRuleConfig from a JSON string
pii_detection_rule_config_instance = PiiDetectionRuleConfig.from_json(json)
# print the JSON string representation of the object
print(PiiDetectionRuleConfig.to_json())

# convert the object into a dict
pii_detection_rule_config_dict = pii_detection_rule_config_instance.to_dict()
# create an instance of PiiDetectionRuleConfig from a dict
pii_detection_rule_config_from_dict = PiiDetectionRuleConfig.from_dict(pii_detection_rule_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

