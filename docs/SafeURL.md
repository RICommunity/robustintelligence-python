# SafeURL

SafeURL represents a URL that has been safely constructed. e.g. a user clicking on this link is guaranteed to land on the RIME web app. We use this instead of a raw str so that application code can generate SafeURL messages in certain ways -> this provides stronger typing than just using a string.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | A safely constructed URL. | [optional] 

## Example

```python
from ri.apiclient.models.safe_url import SafeURL

# TODO update the JSON string below
json = "{}"
# create an instance of SafeURL from a JSON string
safe_url_instance = SafeURL.from_json(json)
# print the JSON string representation of the object
print(SafeURL.to_json())

# convert the object into a dict
safe_url_dict = safe_url_instance.to_dict()
# create an instance of SafeURL from a dict
safe_url_from_dict = SafeURL.from_dict(safe_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

