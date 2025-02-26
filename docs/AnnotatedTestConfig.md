# AnnotatedTestConfig

AnnotatedTestConfig stores the configuration values for a single test, alongside descriptions of the configuration values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contents** | **bytearray** |  | [optional] 
**description** | **str** | A description of the configuration parameters for the test. | [optional] 

## Example

```python
from ri.apiclient.models.annotated_test_config import AnnotatedTestConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotatedTestConfig from a JSON string
annotated_test_config_instance = AnnotatedTestConfig.from_json(json)
# print the JSON string representation of the object
print(AnnotatedTestConfig.to_json())

# convert the object into a dict
annotated_test_config_dict = annotated_test_config_instance.to_dict()
# create an instance of AnnotatedTestConfig from a dict
annotated_test_config_from_dict = AnnotatedTestConfig.from_dict(
    annotated_test_config_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

