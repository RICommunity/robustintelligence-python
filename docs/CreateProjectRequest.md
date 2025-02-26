# CreateProjectRequest

CreateProjectRequest defines a request to create a new Project.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**use_case** | **str** |  | [optional] 
**ethical_consideration** | **str** |  | [optional] 
**workspace_id** | [**ID**](ID.md) |  | [optional] 
**model_task** | [**ModelTask**](ModelTask.md) |  | [default to ModelTask.UNSPECIFIED]
**tags** | **List[str]** | List of tags associated with the Project to help organizing Projects. | [optional] 
**profiling_config** | [**ProfilingConfig**](ProfilingConfig.md) |  | [optional] 
**is_published** | **bool** | Published projects are shown on the Workspace overview page. | [optional] 
**run_time_info** | [**RunTimeInfo**](RunTimeInfo.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.create_project_request import CreateProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectRequest from a JSON string
create_project_request_instance = CreateProjectRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProjectRequest.to_json())

# convert the object into a dict
create_project_request_dict = create_project_request_instance.to_dict()
# create an instance of CreateProjectRequest from a dict
create_project_request_from_dict = CreateProjectRequest.from_dict(create_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

