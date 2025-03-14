# Dataset

Dataset represents a full entry in the Data Registry, with info, metadata, and tags used to identify the data both internally and to an external user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name and dataset_id are both enforced to be unique. Name is user specified. dataset_id is internally generated. It is semantically determined as firewall_id#start_time#end_time in the case the CTInfo is provided. | [optional] 
**dataset_id** | **str** |  | [optional] 
**project_ids** | [**List[ID]**](ID.md) | For now, a dataset will only have one project_id associated with it. We make this an array to allow dataset&#39;s to be shared in the future. | [optional] 
**creator_id** | [**ID**](ID.md) |  | [optional] 
**creation_time** | **datetime** |  | [optional] 
**user_metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**integration_id** | [**ID**](ID.md) |  | [optional] 
**data_info** | [**DataInfo**](DataInfo.md) |  | [optional] 
**ct_info** | [**CTInfo**](CTInfo.md) |  | [optional] 
**validity_status** | [**ValidityStatus**](ValidityStatus.md) |  | [optional] [default to ValidityStatus.UNSPECIFIED]
**marked_for_delete_at** | **datetime** | If marked_for_delete_at is set, the document will be deleted after a TTL. | [optional] 
**validity_status_message** | **str** | Information about the validity status of the dataset, such as why it is invalid.  A Case where this would be populated is when the ValidityStatus is not explicitly set to valid by the XP validation task and additional details are required to convey to the user why the dataset is not valid. | [optional] 
**size_bytes** | **str** |  | [optional] 

## Example

```python
from ri.apiclient.models.dataset import Dataset

# TODO update the JSON string below
json = "{}"
# create an instance of Dataset from a JSON string
dataset_instance = Dataset.from_json(json)
# print the JSON string representation of the object
print(Dataset.to_json())

# convert the object into a dict
dataset_dict = dataset_instance.to_dict()
# create an instance of Dataset from a dict
dataset_from_dict = Dataset.from_dict(dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

