# FilescanningRepoMetadataReputation

Information about the \"reputation\" of the model repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**downloads** | **str** | The number of times the model repository has been downloaded. | [optional] 
**likes** | **str** | The number of times the model repository has been liked. | [optional] 
**stars** | **str** | The number of times the model repository has been starred. | [optional] 
**forks** | **str** | The number of times the model repository has been forked. | [optional] 

## Example

```python
from ri.apiclient.models.filescanning_repo_metadata_reputation import FilescanningRepoMetadataReputation

# TODO update the JSON string below
json = "{}"
# create an instance of FilescanningRepoMetadataReputation from a JSON string
filescanning_repo_metadata_reputation_instance = FilescanningRepoMetadataReputation.from_json(json)
# print the JSON string representation of the object
print(FilescanningRepoMetadataReputation.to_json())

# convert the object into a dict
filescanning_repo_metadata_reputation_dict = filescanning_repo_metadata_reputation_instance.to_dict()
# create an instance of FilescanningRepoMetadataReputation from a dict
filescanning_repo_metadata_reputation_from_dict = FilescanningRepoMetadataReputation.from_dict(filescanning_repo_metadata_reputation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

