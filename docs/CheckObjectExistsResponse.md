# CheckObjectExistsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exists** | **bool** |  | [optional] 

## Example

```python
from ri.apiclient.models.check_object_exists_response import CheckObjectExistsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckObjectExistsResponse from a JSON string
check_object_exists_response_instance = CheckObjectExistsResponse.from_json(json)
# print the JSON string representation of the object
print(CheckObjectExistsResponse.to_json())

# convert the object into a dict
check_object_exists_response_dict = check_object_exists_response_instance.to_dict()
# create an instance of CheckObjectExistsResponse from a dict
check_object_exists_response_from_dict = CheckObjectExistsResponse.from_dict(
    check_object_exists_response_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

