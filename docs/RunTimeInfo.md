# RunTimeInfo

Configures run-time details about how a job should be run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_image** | [**CustomImageType**](CustomImageType.md) |  | [optional] 
**resource_request** | [**ResourceRequest**](ResourceRequest.md) |  | [optional] 
**explicit_errors** | **bool** | Specifies whether the job will return silent errors. By default, this is set to false, and silent errors are not returned. | [optional] 
**random_seed** | **str** | Random seed to use for the Job, so that Test Job result will be deterministic. | [optional] 

## Example

```python
from ri.apiclient.models.run_time_info import RunTimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RunTimeInfo from a JSON string
run_time_info_instance = RunTimeInfo.from_json(json)
# print the JSON string representation of the object
print(RunTimeInfo.to_json())

# convert the object into a dict
run_time_info_dict = run_time_info_instance.to_dict()
# create an instance of RunTimeInfo from a dict
run_time_info_from_dict = RunTimeInfo.from_dict(run_time_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

