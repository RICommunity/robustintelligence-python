# HuggingFaceDataInfo

HuggingFaceDataInfo provides the information needed to load a HuggingFace dataset.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_uri** | **str** | The unique identifier of the dataset. | 
**split_name** | **str** | The string that represents the name of a predefined subset of data. | 
**loading_params_json** | **str** | This is a JSON-serialized string from a map. | [optional] 

## Example

```python
from ri.apiclient.models.hugging_face_data_info import HuggingFaceDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HuggingFaceDataInfo from a JSON string
hugging_face_data_info_instance = HuggingFaceDataInfo.from_json(json)
# print the JSON string representation of the object
print(HuggingFaceDataInfo.to_json())

# convert the object into a dict
hugging_face_data_info_dict = hugging_face_data_info_instance.to_dict()
# create an instance of HuggingFaceDataInfo from a dict
hugging_face_data_info_from_dict = HuggingFaceDataInfo.from_dict(hugging_face_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

