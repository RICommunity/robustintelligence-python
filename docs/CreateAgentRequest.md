# CreateAgentRequest

CreateAgentRequest is the request for creating an agent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Agent name given by the user. | [optional] 
**local_config** | **object** | Configuration for local machine. | [optional] 
**aws_config** | [**AWSConfig**](AWSConfig.md) |  | [optional] 
**gcp_config** | [**GCPConfig**](GCPConfig.md) |  | [optional] 
**azure_config** | [**AzureConfig**](AzureConfig.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.create_agent_request import CreateAgentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAgentRequest from a JSON string
create_agent_request_instance = CreateAgentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAgentRequest.to_json())

# convert the object into a dict
create_agent_request_dict = create_agent_request_instance.to_dict()
# create an instance of CreateAgentRequest from a dict
create_agent_request_from_dict = CreateAgentRequest.from_dict(create_agent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

