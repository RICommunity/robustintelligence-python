# RefEvalDatasets

RefEvalDatasets uniquely specifies information about reference and evaluation Datasets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref_dataset_id** | **str** | Uniquely specifies a reference Dataset. | [optional] 
**eval_dataset_id** | **str** | Uniquely specifies an evaluation Dataset. | 
**eval_dataset_time_interval** | [**TimeInterval**](TimeInterval.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.ref_eval_datasets import RefEvalDatasets

# TODO update the JSON string below
json = "{}"
# create an instance of RefEvalDatasets from a JSON string
ref_eval_datasets_instance = RefEvalDatasets.from_json(json)
# print the JSON string representation of the object
print(RefEvalDatasets.to_json())

# convert the object into a dict
ref_eval_datasets_dict = ref_eval_datasets_instance.to_dict()
# create an instance of RefEvalDatasets from a dict
ref_eval_datasets_from_dict = RefEvalDatasets.from_dict(ref_eval_datasets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

