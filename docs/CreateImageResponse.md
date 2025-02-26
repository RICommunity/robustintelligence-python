# CreateImageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | [**ManagedImage**](ManagedImage.md) |  | [optional] 
**job** | [**JobMetadata**](JobMetadata.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.create_image_response import CreateImageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateImageResponse from a JSON string
create_image_response_instance = CreateImageResponse.from_json(json)
# print the JSON string representation of the object
print(CreateImageResponse.to_json())

# convert the object into a dict
create_image_response_dict = create_image_response_instance.to_dict()
# create an instance of CreateImageResponse from a dict
create_image_response_from_dict = CreateImageResponse.from_dict(create_image_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

