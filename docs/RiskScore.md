# RiskScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RiskCategoryType**](RiskCategoryType.md) |  | [optional] [default to RiskCategoryType.UNSPECIFIED]
**severity** | [**RimeSeverity**](RimeSeverity.md) |  | [optional] [default to RimeSeverity.UNSPECIFIED]
**score** | **float** | A risk score is a value between 0 and 1, where 0 is the lowest risk and 1 is the highest risk. | [optional] 

## Example

```python
from ri.apiclient.models.risk_score import RiskScore

# TODO update the JSON string below
json = "{}"
# create an instance of RiskScore from a JSON string
risk_score_instance = RiskScore.from_json(json)
# print the JSON string representation of the object
print(RiskScore.to_json())

# convert the object into a dict
risk_score_dict = risk_score_instance.to_dict()
# create an instance of RiskScore from a dict
risk_score_from_dict = RiskScore.from_dict(risk_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

