# CTInfo

CTInfo represents information about the dataset and its use in CT runs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firewall_id** | [**ID**](ID.md) |  | 
**start_time** | **datetime** | Start and end time are the start and end time of this dataset. | 
**end_time** | **datetime** |  | 
**ct_dataset_type** | [**CTDatasetType**](CTDatasetType.md) |  | [optional] [default to CTDatasetType.UNSPECIFIED]

## Example

```python
from ri.apiclient.models.ct_info import CTInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CTInfo from a JSON string
ct_info_instance = CTInfo.from_json(json)
# print the JSON string representation of the object
print(CTInfo.to_json())

# convert the object into a dict
ct_info_dict = ct_info_instance.to_dict()
# create an instance of CTInfo from a dict
ct_info_from_dict = CTInfo.from_dict(ct_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

