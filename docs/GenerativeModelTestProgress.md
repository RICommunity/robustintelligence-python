# GenerativeModelTestProgress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_attacks** | **int** |  | [optional] 
**attacks_attempted** | **int** |  | [optional] 

## Example

```python
from ri.apiclient.models.generative_model_test_progress import (
    GenerativeModelTestProgress,
)

# TODO update the JSON string below
json = "{}"
# create an instance of GenerativeModelTestProgress from a JSON string
generative_model_test_progress_instance = GenerativeModelTestProgress.from_json(json)
# print the JSON string representation of the object
print(GenerativeModelTestProgress.to_json())

# convert the object into a dict
generative_model_test_progress_dict = generative_model_test_progress_instance.to_dict()
# create an instance of GenerativeModelTestProgress from a dict
generative_model_test_progress_from_dict = GenerativeModelTestProgress.from_dict(
    generative_model_test_progress_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

