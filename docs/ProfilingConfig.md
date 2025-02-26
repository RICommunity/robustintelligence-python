# ProfilingConfig

Specifies data and model profiling configurations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_profiling** | [**DataProfiling**](DataProfiling.md) |  | [optional] 
**model_profiling** | [**ModelProfiling**](ModelProfiling.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.profiling_config import ProfilingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilingConfig from a JSON string
profiling_config_instance = ProfilingConfig.from_json(json)
# print the JSON string representation of the object
print(ProfilingConfig.to_json())

# convert the object into a dict
profiling_config_dict = profiling_config_instance.to_dict()
# create an instance of ProfilingConfig from a dict
profiling_config_from_dict = ProfilingConfig.from_dict(profiling_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

