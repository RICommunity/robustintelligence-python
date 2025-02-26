# GetProjectIDResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | [**ID**](ID.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.get_project_id_response import GetProjectIDResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectIDResponse from a JSON string
get_project_id_response_instance = GetProjectIDResponse.from_json(json)
# print the JSON string representation of the object
print(GetProjectIDResponse.to_json())

# convert the object into a dict
get_project_id_response_dict = get_project_id_response_instance.to_dict()
# create an instance of GetProjectIDResponse from a dict
get_project_id_response_from_dict = GetProjectIDResponse.from_dict(
    get_project_id_response_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

