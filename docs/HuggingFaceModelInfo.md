# HuggingFaceModelInfo

Represents info for a Hugging Face model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_uri** | **str** | The name of the model to use.  Can get be found by using the copy button next to the name of the model on the model page.  For example, the model_uri for the model at https://huggingface.co/distilgpt2 is \&quot;distilgpt2\&quot;. | 
**kwargs** | **str** | We are currently in the process of adding extra huggingface params and separating use cases into tabular and nlp. Use a serialized json dictionary for other variables right now to ensure maximum flexibility. | [optional] 

## Example

```python
from ri.apiclient.models.hugging_face_model_info import HuggingFaceModelInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HuggingFaceModelInfo from a JSON string
hugging_face_model_info_instance = HuggingFaceModelInfo.from_json(json)
# print the JSON string representation of the object
print(HuggingFaceModelInfo.to_json())

# convert the object into a dict
hugging_face_model_info_dict = hugging_face_model_info_instance.to_dict()
# create an instance of HuggingFaceModelInfo from a dict
hugging_face_model_info_from_dict = HuggingFaceModelInfo.from_dict(
    hugging_face_model_info_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

