# StartFileScanResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | [**JobMetadata**](JobMetadata.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.start_file_scan_response import StartFileScanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StartFileScanResponse from a JSON string
start_file_scan_response_instance = StartFileScanResponse.from_json(json)
# print the JSON string representation of the object
print(StartFileScanResponse.to_json())

# convert the object into a dict
start_file_scan_response_dict = start_file_scan_response_instance.to_dict()
# create an instance of StartFileScanResponse from a dict
start_file_scan_response_from_dict = StartFileScanResponse.from_dict(
    start_file_scan_response_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

