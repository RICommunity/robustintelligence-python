# GetCustomerManagedKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmk_config** | [**CustomerManagedKeyConfig**](CustomerManagedKeyConfig.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.get_customer_managed_key_response import GetCustomerManagedKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCustomerManagedKeyResponse from a JSON string
get_customer_managed_key_response_instance = GetCustomerManagedKeyResponse.from_json(json)
# print the JSON string representation of the object
print(GetCustomerManagedKeyResponse.to_json())

# convert the object into a dict
get_customer_managed_key_response_dict = get_customer_managed_key_response_instance.to_dict()
# create an instance of GetCustomerManagedKeyResponse from a dict
get_customer_managed_key_response_from_dict = GetCustomerManagedKeyResponse.from_dict(get_customer_managed_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

