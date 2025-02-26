# CustomerManagedKeyConfig

CustomerManagedKeyConfig specifies the configuration of a customer managed key. This config contains the key provider and the resource identifier of the key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_provider** | [**KeyProvider**](KeyProvider.md) |  | [default to KeyProvider.UNSPECIFIED]
**kms_key_arn** | **str** | The ARN of the AWS KMS key to use as the customer managed key. | 

## Example

```python
from ri.apiclient.models.customer_managed_key_config import CustomerManagedKeyConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerManagedKeyConfig from a JSON string
customer_managed_key_config_instance = CustomerManagedKeyConfig.from_json(json)
# print the JSON string representation of the object
print(CustomerManagedKeyConfig.to_json())

# convert the object into a dict
customer_managed_key_config_dict = customer_managed_key_config_instance.to_dict()
# create an instance of CustomerManagedKeyConfig from a dict
customer_managed_key_config_from_dict = CustomerManagedKeyConfig.from_dict(customer_managed_key_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

