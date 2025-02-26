# JobInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | [**ID**](ID.md) |  | [optional] 
**job_status** | [**JobStatus**](JobStatus.md) |  | [optional] [default to JobStatus.UNSPECIFIED]
**start_time** | **datetime** | When the job started and not the same as when the job was created.  If the job never starts, it will be 0. | [optional] 
**completion_time** | **datetime** | When the job finished. | [optional] 

## Example

```python
from ri.apiclient.models.job_info import JobInfo

# TODO update the JSON string below
json = "{}"
# create an instance of JobInfo from a JSON string
job_info_instance = JobInfo.from_json(json)
# print the JSON string representation of the object
print(JobInfo.to_json())

# convert the object into a dict
job_info_dict = job_info_instance.to_dict()
# create an instance of JobInfo from a dict
job_info_from_dict = JobInfo.from_dict(job_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

