# ArchivedJobLogs

ArchivedJobLogs contains the URL to the archived logs for a RIME job and the expiration time of the URL.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | [**SafeURL**](SafeURL.md) |  | [optional] 
**expiration_time** | **datetime** |  | [optional] 

## Example

```python
from ri.apiclient.models.archived_job_logs import ArchivedJobLogs

# TODO update the JSON string below
json = "{}"
# create an instance of ArchivedJobLogs from a JSON string
archived_job_logs_instance = ArchivedJobLogs.from_json(json)
# print the JSON string representation of the object
print(ArchivedJobLogs.to_json())

# convert the object into a dict
archived_job_logs_dict = archived_job_logs_instance.to_dict()
# create an instance of ArchivedJobLogs from a dict
archived_job_logs_from_dict = ArchivedJobLogs.from_dict(archived_job_logs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

