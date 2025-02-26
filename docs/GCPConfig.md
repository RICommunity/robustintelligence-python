# GCPConfig

Configuration for GCP.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gcp_sa_email** | **str** | GCP service account email for the role to be attached to the service account of the model test jobs. | [optional] 

## Example

```python
from ri.apiclient.models.gcp_config import GCPConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GCPConfig from a JSON string
gcp_config_instance = GCPConfig.from_json(json)
# print the JSON string representation of the object
print(GCPConfig.to_json())

# convert the object into a dict
gcp_config_dict = gcp_config_instance.to_dict()
# create an instance of GCPConfig from a dict
gcp_config_from_dict = GCPConfig.from_dict(gcp_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

