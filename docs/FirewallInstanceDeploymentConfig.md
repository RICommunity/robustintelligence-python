# FirewallInstanceDeploymentConfig

Configuration for the deployment spec of a Firewall Instance. The Pod Annotations are validated as valid k8s annotations. They cannot override pre-existing deployment annotations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pod_annotations** | **Dict[str, str]** |  | [optional] 

## Example

```python
from ri.apiclient.models.firewall_instance_deployment_config import FirewallInstanceDeploymentConfig

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallInstanceDeploymentConfig from a JSON string
firewall_instance_deployment_config_instance = FirewallInstanceDeploymentConfig.from_json(json)
# print the JSON string representation of the object
print(FirewallInstanceDeploymentConfig.to_json())

# convert the object into a dict
firewall_instance_deployment_config_dict = firewall_instance_deployment_config_instance.to_dict()
# create an instance of FirewallInstanceDeploymentConfig from a dict
firewall_instance_deployment_config_from_dict = FirewallInstanceDeploymentConfig.from_dict(firewall_instance_deployment_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

