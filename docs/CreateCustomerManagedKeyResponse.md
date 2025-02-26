# CreateCustomerManagedKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmk_config** | [**CustomerManagedKeyConfig**](CustomerManagedKeyConfig.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.create_customer_managed_key_response import (
    CreateCustomerManagedKeyResponse,
)

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomerManagedKeyResponse from a JSON string
create_customer_managed_key_response_instance = (
    CreateCustomerManagedKeyResponse.from_json(json)
)
# print the JSON string representation of the object
print(CreateCustomerManagedKeyResponse.to_json())

# convert the object into a dict
create_customer_managed_key_response_dict = (
    create_customer_managed_key_response_instance.to_dict()
)
# create an instance of CreateCustomerManagedKeyResponse from a dict
create_customer_managed_key_response_from_dict = (
    CreateCustomerManagedKeyResponse.from_dict(
        create_customer_managed_key_response_dict
    )
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

