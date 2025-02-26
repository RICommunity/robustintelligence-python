# TestFeatureResultDisplay

Display contains information for displaying the feature result in the RI web app. The contents of each field are unstable; it is not recommended to parse them programmatically.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary_details** | **bytearray** | Summary details are marshalled JSON. | [optional] 
**table_columns_to_show** | [**List[TableColumn]**](TableColumn.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.test_feature_result_display import TestFeatureResultDisplay

# TODO update the JSON string below
json = "{}"
# create an instance of TestFeatureResultDisplay from a JSON string
test_feature_result_display_instance = TestFeatureResultDisplay.from_json(json)
# print the JSON string representation of the object
print(TestFeatureResultDisplay.to_json())

# convert the object into a dict
test_feature_result_display_dict = test_feature_result_display_instance.to_dict()
# create an instance of TestFeatureResultDisplay from a dict
test_feature_result_display_from_dict = TestFeatureResultDisplay.from_dict(test_feature_result_display_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

