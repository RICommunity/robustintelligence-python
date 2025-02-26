# GenerativeValidationConfig

GenerativeValidationConfig is the configuration to run a generative model test.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt_bank** | [**PromptBank**](PromptBank.md) |  | [optional] [default to PromptBank.UNSPECIFIED]
**system_prompt** | **str** | The system prompt that is currently active on the provided endpoint. If this is not set, system prompt extraction tests will be skipped. | [optional] 
**connection** | [**ModelConnectionSpec**](ModelConnectionSpec.md) |  | [optional] 
**model_output_is_sensitive** | **bool** | Will not be saved to the database, logged in plaintext, etc. | [optional] 
**filters** | [**Filters**](Filters.md) |  | [optional] 
**language** | [**Language**](Language.md) |  | [optional] [default to Language.EN]

## Example

```python
from ri.apiclient.models.generative_validation_config import GenerativeValidationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GenerativeValidationConfig from a JSON string
generative_validation_config_instance = GenerativeValidationConfig.from_json(json)
# print the JSON string representation of the object
print(GenerativeValidationConfig.to_json())

# convert the object into a dict
generative_validation_config_dict = generative_validation_config_instance.to_dict()
# create an instance of GenerativeValidationConfig from a dict
generative_validation_config_from_dict = GenerativeValidationConfig.from_dict(
    generative_validation_config_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

