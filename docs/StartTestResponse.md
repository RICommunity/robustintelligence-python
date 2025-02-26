# StartTestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | [**ID**](ID.md) |  | [optional] 
**test_run_id** | [**ID**](ID.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.start_test_response import StartTestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StartTestResponse from a JSON string
start_test_response_instance = StartTestResponse.from_json(json)
# print the JSON string representation of the object
print(StartTestResponse.to_json())

# convert the object into a dict
start_test_response_dict = start_test_response_instance.to_dict()
# create an instance of StartTestResponse from a dict
start_test_response_from_dict = StartTestResponse.from_dict(start_test_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

