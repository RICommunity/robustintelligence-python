# ListObjectsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paths** | **List[str]** |  | [optional] 

## Example

```python
from ri.apiclient.models.list_objects_response import ListObjectsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListObjectsResponse from a JSON string
list_objects_response_instance = ListObjectsResponse.from_json(json)
# print the JSON string representation of the object
print(ListObjectsResponse.to_json())

# convert the object into a dict
list_objects_response_dict = list_objects_response_instance.to_dict()
# create an instance of ListObjectsResponse from a dict
list_objects_response_from_dict = ListObjectsResponse.from_dict(list_objects_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

