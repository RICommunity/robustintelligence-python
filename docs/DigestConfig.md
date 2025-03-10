# DigestConfig

DigestConfig is a configuration for digest notifications. These notifications are helpful for receiving a succinct summary of activity under a given project.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | [**DigestFrequency**](DigestFrequency.md) |  | [optional] [default to DigestFrequency.UNSPECIFIED]
**hour_offset** | **int** | The offset in the day when the digest starts. The offset is taken in the configured timezone for the workspace. Uses a default value of 08:00 when not provided. | [optional] 
**last_digest_time** | **datetime** | The last time that the RI platform sent the digest. This timestamp is zero when no digests have ever been sent. | [optional] 

## Example

```python
from ri.apiclient.models.digest_config import DigestConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DigestConfig from a JSON string
digest_config_instance = DigestConfig.from_json(json)
# print the JSON string representation of the object
print(DigestConfig.to_json())

# convert the object into a dict
digest_config_dict = digest_config_instance.to_dict()
# create an instance of DigestConfig from a dict
digest_config_from_dict = DigestConfig.from_dict(digest_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

