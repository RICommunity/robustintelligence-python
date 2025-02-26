# GenerativeValidationResult

GenerativeValidationResult represents a single result of testing a Generative model with attack prompts. The model output is sent to a detection layer, which indicates whether it contains objectionable content. There is a single test result for the \"attack_technique\", \"attack_objective\", and \"objective_sub_category\" combination.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | [optional] 
**attack_technique** | **str** | The attack technique used in the prompt. This is a string because the types of attacks changes frequently over time depending on our threat intelligence. | [optional] 
**attack_objective** | [**AttackObjective**](AttackObjective.md) |  | [optional] [default to AttackObjective.UNSPECIFIED]
**objective_sub_category** | [**ObjectiveSubCategory**](ObjectiveSubCategory.md) |  | [optional] [default to ObjectiveSubCategory.UNSPECIFIED]
**failing_examples** | [**List[Example]**](Example.md) | List of failing examples to demonstrate failures in this category. | [optional] 
**severity** | [**GenerativeSeverity**](GenerativeSeverity.md) |  | [optional] [default to GenerativeSeverity.NONE]
**owasp_standards** | [**List[StandardInfo]**](StandardInfo.md) | List of the OWASP AI risk standards associated with the attacks in these results. | [optional] 
**nist_standards** | [**List[StandardInfo]**](StandardInfo.md) | List of the NIST AI risk standards associated with the attacks in these results. | [optional] 
**mitre_standards** | [**List[StandardInfo]**](StandardInfo.md) | List of the MITRE AI risk standards associated with the attacks in these results. | [optional] 
**attacks_attempted** | **int** | The number of attacks attempted for these results. | [optional] 
**threat** | [**Threat**](Threat.md) |  | [optional] [default to Threat.UNSPECIFIED]
**successful_attacks** | **int** | The number of successful attacks completed for these results. | [optional] 
**skipped_reason** | **str** | Indicates that the test was skipped and provides a reason. If the test was not skipped this will be the empty string. | [optional] 
**test_run_id** | [**ID**](ID.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.generative_validation_result import GenerativeValidationResult

# TODO update the JSON string below
json = "{}"
# create an instance of GenerativeValidationResult from a JSON string
generative_validation_result_instance = GenerativeValidationResult.from_json(json)
# print the JSON string representation of the object
print(GenerativeValidationResult.to_json())

# convert the object into a dict
generative_validation_result_dict = generative_validation_result_instance.to_dict()
# create an instance of GenerativeValidationResult from a dict
generative_validation_result_from_dict = GenerativeValidationResult.from_dict(generative_validation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

