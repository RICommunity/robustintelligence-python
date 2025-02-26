# SeverityCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_none_severity** | **str** |  | [optional] 
**num_low_severity** | **str** |  | [optional] 
**num_high_severity** | **str** |  | [optional] 

## Example

```python
from ri.apiclient.models.severity_counts import SeverityCounts

# TODO update the JSON string below
json = "{}"
# create an instance of SeverityCounts from a JSON string
severity_counts_instance = SeverityCounts.from_json(json)
# print the JSON string representation of the object
print(SeverityCounts.to_json())

# convert the object into a dict
severity_counts_dict = severity_counts_instance.to_dict()
# create an instance of SeverityCounts from a dict
severity_counts_from_dict = SeverityCounts.from_dict(severity_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

