# CreateProjectResponse

CreateProjectResponse returns a newly created Project.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | [**Project**](Project.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.create_project_response import CreateProjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectResponse from a JSON string
create_project_response_instance = CreateProjectResponse.from_json(json)
# print the JSON string representation of the object
print(CreateProjectResponse.to_json())

# convert the object into a dict
create_project_response_dict = create_project_response_instance.to_dict()
# create an instance of CreateProjectResponse from a dict
create_project_response_from_dict = CreateProjectResponse.from_dict(create_project_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

