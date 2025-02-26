# LatestRunInfo

LatestRunInfo tracks the latest run bin in the firewall.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bin** | [**TimeInterval**](TimeInterval.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.latest_run_info import LatestRunInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LatestRunInfo from a JSON string
latest_run_info_instance = LatestRunInfo.from_json(json)
# print the JSON string representation of the object
print(LatestRunInfo.to_json())

# convert the object into a dict
latest_run_info_dict = latest_run_info_instance.to_dict()
# create an instance of LatestRunInfo from a dict
latest_run_info_from_dict = LatestRunInfo.from_dict(latest_run_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

