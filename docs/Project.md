# Project

Project collects test runs for a Stress Test or Continuous Test that relate to a shared machine learning task. Each model for the task is tested by an individual test run. A Continuous Test monitors a currently promoted model over time by continuously testing that model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**use_case** | **str** |  | [optional] 
**ethical_consideration** | **str** |  | [optional] 
**creation_time** | **datetime** |  | [optional] 
**owner_id** | [**ID**](ID.md) |  | [optional] 
**workspace_id** | [**ID**](ID.md) |  | [optional] 
**model_task** | [**ModelTask**](ModelTask.md) |  | [optional] [default to ModelTask.UNSPECIFIED]
**tags** | **List[str]** | List of tags associated with the Project to help organizing Projects. | [optional] 
**firewall_ids** | [**List[ID]**](ID.md) | List of Firewall IDs that belong to the Project. | [optional] 
**project_test_suite_config** | [**TestSuiteConfig**](TestSuiteConfig.md) |  | [optional] 
**profiling_config** | [**ProfilingConfig**](ProfilingConfig.md) |  | [optional] 
**run_time_info** | [**RunTimeInfo**](RunTimeInfo.md) |  | [optional] 
**is_published** | **bool** | Published projects are shown on the Workspace overview page. | [optional] 
**last_test_run_time** | **datetime** | Last time a Test Run was successfully uploaded to the Project. | [optional] 
**stress_test_categories** | [**List[TestCategoryType]**](TestCategoryType.md) | List of test categories to be run in Stress Testing. | [optional] 
**continuous_test_categories** | [**List[TestCategoryType]**](TestCategoryType.md) | List of test categories to be run in Continuous Testing. | [optional] 
**risk_scores** | [**List[RiskScore]**](RiskScore.md) |  | [optional] 
**active_schedule** | [**ScheduleInfo**](ScheduleInfo.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print(Project.to_json())

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_from_dict = Project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

