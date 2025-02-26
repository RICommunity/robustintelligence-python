# GetTestRunIDResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_run_id** | **str** |  | [optional] 

## Example

```python
from ri.apiclient.models.get_test_run_id_response import GetTestRunIDResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTestRunIDResponse from a JSON string
get_test_run_id_response_instance = GetTestRunIDResponse.from_json(json)
# print the JSON string representation of the object
print(GetTestRunIDResponse.to_json())

# convert the object into a dict
get_test_run_id_response_dict = get_test_run_id_response_instance.to_dict()
# create an instance of GetTestRunIDResponse from a dict
get_test_run_id_response_from_dict = GetTestRunIDResponse.from_dict(get_test_run_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

