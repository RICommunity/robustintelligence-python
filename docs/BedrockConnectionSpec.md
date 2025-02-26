# BedrockConnectionSpec

BedrockConnectionSpec defines the information needed to make and parse a request to AWS Bedrock.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | **str** | Specifies the model id to use. | [optional] 
**aws_integration_id** | [**ID**](ID.md) |  | [optional] 
**body** | [**Body**](Body.md) |  | [optional] 
**response_json_path** | **str** | A json path specifying where in the response json payload we can find the LLM&#39;s response response string. Note that the path must point to a string value in the json payload. Whitespace and other special characters can be encoded as unicode (\\u0020). Periods in json fields can be escaped with a backslash. | [optional] 

## Example

```python
from ri.apiclient.models.bedrock_connection_spec import BedrockConnectionSpec

# TODO update the JSON string below
json = "{}"
# create an instance of BedrockConnectionSpec from a JSON string
bedrock_connection_spec_instance = BedrockConnectionSpec.from_json(json)
# print the JSON string representation of the object
print(BedrockConnectionSpec.to_json())

# convert the object into a dict
bedrock_connection_spec_dict = bedrock_connection_spec_instance.to_dict()
# create an instance of BedrockConnectionSpec from a dict
bedrock_connection_spec_from_dict = BedrockConnectionSpec.from_dict(bedrock_connection_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

