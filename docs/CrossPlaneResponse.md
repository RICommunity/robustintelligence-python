# CrossPlaneResponse

CrossPlaneResponse encompasses the set of responses from cross-plane services.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_config_generation_service_response** | [**CategoryConfigGenerationServiceResponse**](CategoryConfigGenerationServiceResponse.md) |  | [optional] 
**profiling_config_generation_service_response** | [**ProfilingConfigGenerationServiceResponse**](ProfilingConfigGenerationServiceResponse.md) |  | [optional] 
**test_suite_config_generation_service_response** | [**TestSuiteConfigGenerationServiceResponse**](TestSuiteConfigGenerationServiceResponse.md) |  | [optional] 
**check_object_exists_response** | [**CheckObjectExistsResponse**](CheckObjectExistsResponse.md) |  | [optional] 
**delete_object_response** | **object** |  | [optional] 
**get_read_object_presigned_link_response** | [**GetReadObjectPresignedLinkResponse**](GetReadObjectPresignedLinkResponse.md) |  | [optional] 
**get_upload_object_presigned_link_response** | [**GetUploadObjectPresignedLinkResponse**](GetUploadObjectPresignedLinkResponse.md) |  | [optional] 
**list_objects_response** | [**ListObjectsResponse**](ListObjectsResponse.md) |  | [optional] 
**validate_dataset_response** | [**ValidateDatasetResponse**](ValidateDatasetResponse.md) |  | [optional] 
**validate_model_response** | [**ValidateModelResponse**](ValidateModelResponse.md) |  | [optional] 
**validate_predictions_response** | [**ValidatePredictionsResponse**](ValidatePredictionsResponse.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.cross_plane_response import CrossPlaneResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrossPlaneResponse from a JSON string
cross_plane_response_instance = CrossPlaneResponse.from_json(json)
# print the JSON string representation of the object
print(CrossPlaneResponse.to_json())

# convert the object into a dict
cross_plane_response_dict = cross_plane_response_instance.to_dict()
# create an instance of CrossPlaneResponse from a dict
cross_plane_response_from_dict = CrossPlaneResponse.from_dict(cross_plane_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

