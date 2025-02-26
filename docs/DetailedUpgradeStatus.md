# DetailedUpgradeStatus

DetailedUpgradeStatus is an UpgradeStatus with additional information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**UpgradeStatus**](UpgradeStatus.md) |  | [default to UpgradeStatus.UNSPECIFIED]
**last_update_time** | **datetime** |  | 
**error_message** | **str** | The error message if the status is failed. | [optional] 

## Example

```python
from ri.apiclient.models.detailed_upgrade_status import DetailedUpgradeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DetailedUpgradeStatus from a JSON string
detailed_upgrade_status_instance = DetailedUpgradeStatus.from_json(json)
# print the JSON string representation of the object
print(DetailedUpgradeStatus.to_json())

# convert the object into a dict
detailed_upgrade_status_dict = detailed_upgrade_status_instance.to_dict()
# create an instance of DetailedUpgradeStatus from a dict
detailed_upgrade_status_from_dict = DetailedUpgradeStatus.from_dict(detailed_upgrade_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

