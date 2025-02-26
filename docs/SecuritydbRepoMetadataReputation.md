# SecuritydbRepoMetadataReputation

Information about the \"reputation\" of the model repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**downloads** | **int** | The number of times the model repository has been downloaded. | [optional] 
**likes** | **int** | The number of times the model repository has been liked. | [optional] 
**stars** | **int** | The number of times the model repository has been starred. | [optional] 
**forks** | **int** | The number of times the model repository has been forked. | [optional] 

## Example

```python
from ri.apiclient.models.securitydb_repo_metadata_reputation import SecuritydbRepoMetadataReputation

# TODO update the JSON string below
json = "{}"
# create an instance of SecuritydbRepoMetadataReputation from a JSON string
securitydb_repo_metadata_reputation_instance = SecuritydbRepoMetadataReputation.from_json(json)
# print the JSON string representation of the object
print(SecuritydbRepoMetadataReputation.to_json())

# convert the object into a dict
securitydb_repo_metadata_reputation_dict = securitydb_repo_metadata_reputation_instance.to_dict()
# create an instance of SecuritydbRepoMetadataReputation from a dict
securitydb_repo_metadata_reputation_from_dict = SecuritydbRepoMetadataReputation.from_dict(securitydb_repo_metadata_reputation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

