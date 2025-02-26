# WebhookConfig

Configuration for an individual webhook.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook** | **str** | The URL of the destination webhook. It is not a strict requirement, but it is recommended that webhooks be preauthenticated by including a secure token in the URL. | [optional] 

## Example

```python
from ri.apiclient.models.webhook_config import WebhookConfig

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookConfig from a JSON string
webhook_config_instance = WebhookConfig.from_json(json)
# print the JSON string representation of the object
print(WebhookConfig.to_json())

# convert the object into a dict
webhook_config_dict = webhook_config_instance.to_dict()
# create an instance of WebhookConfig from a dict
webhook_config_from_dict = WebhookConfig.from_dict(webhook_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

