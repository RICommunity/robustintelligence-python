# StartFileScanRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | [**ID**](ID.md) |  | 
**model_id** | [**ID**](ID.md) |  | 
**run_time_info** | [**RunTimeInfo**](RunTimeInfo.md) |  | [optional] 
**agent_id** | [**ID**](ID.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.start_file_scan_request import StartFileScanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StartFileScanRequest from a JSON string
start_file_scan_request_instance = StartFileScanRequest.from_json(json)
# print the JSON string representation of the object
print(StartFileScanRequest.to_json())

# convert the object into a dict
start_file_scan_request_dict = start_file_scan_request_instance.to_dict()
# create an instance of StartFileScanRequest from a dict
start_file_scan_request_from_dict = StartFileScanRequest.from_dict(start_file_scan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

