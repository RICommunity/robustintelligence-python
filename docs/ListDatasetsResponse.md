# ListDatasetsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasets** | [**List[Dataset]**](Dataset.md) |  | [optional] 
**next_page_token** | **str** |  | [optional] 
**has_more** | **bool** |  | [optional] 

## Example

```python
from ri.apiclient.models.list_datasets_response import ListDatasetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListDatasetsResponse from a JSON string
list_datasets_response_instance = ListDatasetsResponse.from_json(json)
# print the JSON string representation of the object
print(ListDatasetsResponse.to_json())

# convert the object into a dict
list_datasets_response_dict = list_datasets_response_instance.to_dict()
# create an instance of ListDatasetsResponse from a dict
list_datasets_response_from_dict = ListDatasetsResponse.from_dict(list_datasets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

