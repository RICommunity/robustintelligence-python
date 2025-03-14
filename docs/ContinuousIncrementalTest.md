# ContinuousIncrementalTest

A continuous incremental test job runs `n` test runs, where `n` is the number of bins specified in the dataset. This is a production specific workflow and is used to monitor a model's performance over time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firewall_id** | **str** |  | [optional] 
**ct_test_run_ids** | **List[str]** |  | [optional] 
**progress** | [**ContinuousTestJobProgress**](ContinuousTestJobProgress.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.continuous_incremental_test import ContinuousIncrementalTest

# TODO update the JSON string below
json = "{}"
# create an instance of ContinuousIncrementalTest from a JSON string
continuous_incremental_test_instance = ContinuousIncrementalTest.from_json(json)
# print the JSON string representation of the object
print(ContinuousIncrementalTest.to_json())

# convert the object into a dict
continuous_incremental_test_dict = continuous_incremental_test_instance.to_dict()
# create an instance of ContinuousIncrementalTest from a dict
continuous_incremental_test_from_dict = ContinuousIncrementalTest.from_dict(continuous_incremental_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

