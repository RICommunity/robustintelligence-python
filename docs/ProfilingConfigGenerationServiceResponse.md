# ProfilingConfigGenerationServiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profiling_config** | [**ProfilingConfig**](ProfilingConfig.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.profiling_config_generation_service_response import (
    ProfilingConfigGenerationServiceResponse,
)

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilingConfigGenerationServiceResponse from a JSON string
profiling_config_generation_service_response_instance = (
    ProfilingConfigGenerationServiceResponse.from_json(json)
)
# print the JSON string representation of the object
print(ProfilingConfigGenerationServiceResponse.to_json())

# convert the object into a dict
profiling_config_generation_service_response_dict = (
    profiling_config_generation_service_response_instance.to_dict()
)
# create an instance of ProfilingConfigGenerationServiceResponse from a dict
profiling_config_generation_service_response_from_dict = (
    ProfilingConfigGenerationServiceResponse.from_dict(
        profiling_config_generation_service_response_dict
    )
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

