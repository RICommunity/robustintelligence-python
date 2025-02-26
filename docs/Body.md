# Body


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body_object** | **object** | A JSON representation of the body to be sent to the model. Example for Anthropic:  {    \&quot;anthropic_version\&quot;: \&quot;bedrock-2023-05-31\&quot;,    \&quot;max_tokens\&quot;: 1000,    \&quot;messages\&quot;: [      {        \&quot;role\&quot;: \&quot;user\&quot;,        \&quot;content\&quot;: [          {            \&quot;type\&quot;: \&quot;image\&quot;,            \&quot;source\&quot;: {              \&quot;type\&quot;: \&quot;base64\&quot;,              \&quot;media_type\&quot;: \&quot;image/jpeg\&quot;,              \&quot;data\&quot;: \&quot;iVBORw...\&quot;            }          },          {            \&quot;type\&quot;: \&quot;text\&quot;,            \&quot;text\&quot;: \&quot;What&#39;s in this image?\&quot;          }        ]      }    ]  } Please view model documentation for the expected body format. | [optional] 
**prompt_key** | **str** | The key of the message that is being sent to the model. For example, \&quot;text\&quot; in the example for the object_body. Case sensitive. | [optional] 
**prompt_key_role** | **str** | The role that the prompt key should look for. If there is only one role, this can be omitted. Case sensitive. | [optional] 

## Example

```python
from ri.apiclient.models.body import Body

# TODO update the JSON string below
json = "{}"
# create an instance of Body from a JSON string
body_instance = Body.from_json(json)
# print the JSON string representation of the object
print(Body.to_json())

# convert the object into a dict
body_dict = body_instance.to_dict()
# create an instance of Body from a dict
body_from_dict = Body.from_dict(body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

