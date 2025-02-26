# LimitStatus

LimitStatus contains the status of a limit in this deployment's license.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | [**LicenseLimit**](LicenseLimit.md) |  | [optional] [default to LicenseLimit.UNSPECIFIED]
**limit_status** | [**LimitStatusStatus**](LimitStatusStatus.md) |  | [optional] [default to LimitStatusStatus.UNSPECIFIED]
**limit_value** | **str** |  | [optional] 
**current_value** | **str** |  | [optional] 

## Example

```python
from ri.apiclient.models.limit_status import LimitStatus

# TODO update the JSON string below
json = "{}"
# create an instance of LimitStatus from a JSON string
limit_status_instance = LimitStatus.from_json(json)
# print the JSON string representation of the object
print(LimitStatus.to_json())

# convert the object into a dict
limit_status_dict = limit_status_instance.to_dict()
# create an instance of LimitStatus from a dict
limit_status_from_dict = LimitStatus.from_dict(limit_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

