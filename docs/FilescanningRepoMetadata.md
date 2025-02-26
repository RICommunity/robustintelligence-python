# FilescanningRepoMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purl** | [**PackageURL**](PackageURL.md) |  | [optional] 
**repo_last_modified_time** | **datetime** | The time when the model repository was last modified, inferred from the git history. | [optional] 
**tags** | **List[str]** | The tags associated with the model repository. | [optional] 
**reputation** | [**FilescanningRepoMetadataReputation**](FilescanningRepoMetadataReputation.md) |  | [optional] 
**license** | [**FilescanningRepoMetadataLicense**](FilescanningRepoMetadataLicense.md) |  | [optional] 
**author** | **str** | The author of the model repository. | [optional] 

## Example

```python
from ri.apiclient.models.filescanning_repo_metadata import FilescanningRepoMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FilescanningRepoMetadata from a JSON string
filescanning_repo_metadata_instance = FilescanningRepoMetadata.from_json(json)
# print the JSON string representation of the object
print(FilescanningRepoMetadata.to_json())

# convert the object into a dict
filescanning_repo_metadata_dict = filescanning_repo_metadata_instance.to_dict()
# create an instance of FilescanningRepoMetadata from a dict
filescanning_repo_metadata_from_dict = FilescanningRepoMetadata.from_dict(
    filescanning_repo_metadata_dict
)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

