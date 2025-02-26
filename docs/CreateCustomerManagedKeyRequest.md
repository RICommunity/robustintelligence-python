# CreateCustomerManagedKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmk_config** | [**CustomerManagedKeyConfig**](CustomerManagedKeyConfig.md) |  | 

## Example

```python
from ri.apiclient.models.create_customer_managed_key_request import CreateCustomerManagedKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomerManagedKeyRequest from a JSON string
create_customer_managed_key_request_instance = CreateCustomerManagedKeyRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCustomerManagedKeyRequest.to_json())

# convert the object into a dict
create_customer_managed_key_request_dict = create_customer_managed_key_request_instance.to_dict()
# create an instance of CreateCustomerManagedKeyRequest from a dict
create_customer_managed_key_request_from_dict = CreateCustomerManagedKeyRequest.from_dict(create_customer_managed_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

