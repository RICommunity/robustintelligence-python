# Scan

A file scan job runs over a registered model. It is used to assess a model's supply chain security risk.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | [**ID**](ID.md) |  | [optional] 
**file_scan_id** | **str** |  | [optional] 

## Example

```python
from ri.apiclient.models.scan import Scan

# TODO update the JSON string below
json = "{}"
# create an instance of Scan from a JSON string
scan_instance = Scan.from_json(json)
# print the JSON string representation of the object
print(Scan.to_json())

# convert the object into a dict
scan_dict = scan_instance.to_dict()
# create an instance of Scan from a dict
scan_from_dict = Scan.from_dict(scan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

