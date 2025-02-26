# AWSConfig

Configuration for AWS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_role_arn** | **str** | AWS ARN of the the role to be attached to the service account of the model test jobs. | [optional] 

## Example

```python
from ri.apiclient.models.aws_config import AWSConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AWSConfig from a JSON string
aws_config_instance = AWSConfig.from_json(json)
# print the JSON string representation of the object
print(AWSConfig.to_json())

# convert the object into a dict
aws_config_dict = aws_config_instance.to_dict()
# create an instance of AWSConfig from a dict
aws_config_from_dict = AWSConfig.from_dict(aws_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

