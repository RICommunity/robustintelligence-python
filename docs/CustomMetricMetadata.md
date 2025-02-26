# CustomMetricMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_description** | **str** | Short description. | [optional] 
**starter_description** | **str** | Starter description. | [optional] 
**why_it_matters_description** | **str** | Why it matters description. | [optional] 
**configuration_description** | **str** | Configuration description. | [optional] 
**example_description** | **str** | Example description. | [optional] 

## Example

```python
from ri.apiclient.models.custom_metric_metadata import CustomMetricMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CustomMetricMetadata from a JSON string
custom_metric_metadata_instance = CustomMetricMetadata.from_json(json)
# print the JSON string representation of the object
print(CustomMetricMetadata.to_json())

# convert the object into a dict
custom_metric_metadata_dict = custom_metric_metadata_instance.to_dict()
# create an instance of CustomMetricMetadata from a dict
custom_metric_metadata_from_dict = CustomMetricMetadata.from_dict(custom_metric_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

