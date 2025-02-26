# HttpConnectionSpec

HttpConnectionSpec is how a user defines information for how to configure an http request to an LLM.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**http_headers** | **Dict[str, str]** | HTTP headers that will be sent along with the request payload to the LLM endpoint. These headers can include authentication. | [optional] 
**endpoint_payload_template** | **str** | A string template that will be used to create the json payload sent to the LLM endpoint. This template must contain one and only one variable -- prompt_string. This will be replaced at runtime with the prompt used to send to the model. | 
**response_json_path** | **str** | A json path specifying where in the response json payload we can find the LLM&#39;s response response string. Note that the path must point to a string value in the json payload. Whitespace and other special characters can be encoded as unicode (\\u0020). Periods in json fields can be escaped with a backslash. | 
**http_auth_integration_id** | [**ID**](ID.md) |  | [optional] 
**mtls_integration_id** | [**ID**](ID.md) |  | [optional] 

## Example

```python
from ri.apiclient.models.http_connection_spec import HttpConnectionSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HttpConnectionSpec from a JSON string
http_connection_spec_instance = HttpConnectionSpec.from_json(json)
# print the JSON string representation of the object
print(HttpConnectionSpec.to_json())

# convert the object into a dict
http_connection_spec_dict = http_connection_spec_instance.to_dict()
# create an instance of HttpConnectionSpec from a dict
http_connection_spec_from_dict = HttpConnectionSpec.from_dict(http_connection_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

