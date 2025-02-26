# PullSecret

Description of the secret required to pull a custom image.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Kubernetes pull secret that stores the required pull secret for the custom image. | [optional] 

## Example

```python
from ri.apiclient.models.pull_secret import PullSecret

# TODO update the JSON string below
json = "{}"
# create an instance of PullSecret from a JSON string
pull_secret_instance = PullSecret.from_json(json)
# print the JSON string representation of the object
print(PullSecret.to_json())

# convert the object into a dict
pull_secret_dict = pull_secret_instance.to_dict()
# create an instance of PullSecret from a dict
pull_secret_from_dict = PullSecret.from_dict(pull_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

