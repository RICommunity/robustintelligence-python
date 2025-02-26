# ri.apiclient.ModelCardServiceApi

All URIs are relative to *http://&lt;platform-domain&gt;.rbst.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_model_card**](#create_model_card) | **POST** /v1-beta/modelcards | CreateModelCard
[**delete_model_card**](#delete_model_card) | **DELETE** /v1-beta/modelcards/{modelCardId.uuid} | DeleteModelCard
[**get_model_card**](#get_model_card) | **GET** /v1-beta/modelcards/{modelCardId.uuid} | GetModelCard
[**list_model_cards**](#list_model_cards) | **GET** /v1-beta/modelcards/projects/{projectId} | ListModelCards
[**update_model_card**](#update_model_card) | **PUT** /v1-beta/modelcards/{modelCard.modelCardId.uuid} | UpdateModelCard

# **create_model_card**
> CreateModelCardResponse  = create_model_card()

CreateModelCard

Create a new Model Card.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
model_card | [**ModelCard**](ModelCard.md) |  | [optional] 
project_id | [**ID**](ID.md) |  | [optional] 

### Return type

[**CreateModelCardResponse**](CreateModelCardResponse.md)

### Authorization


[rime-api-key](../README.md#rime-api-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### Example
```python

host_name = "http://<platform-domain>.rbst.io"

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rime-api-key
rime_api_key = os.environ["API_KEY"]

```

```python
import ri.apiclient
from ri import RIClient
from ri.apiclient.models.create_model_card_request import CreateModelCardRequest
from ri.apiclient.models.create_model_card_response import CreateModelCardResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

model_card = ModelCard()  # ModelCard  (optional)
project_id = ID()  # ID  (optional)

try:
    # CreateModelCard
    api_response: CreateModelCardResponse = client.ModelCardServiceApi.create_model_card(model_card=model_card, project_id=project_id)
    print("The response of ModelCardServiceApi->create_model_card:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ModelCardServiceApi->create_model_card: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_model_card**
> DeleteModelCardResponse  = delete_model_card()

DeleteModelCard

Delete Model Card.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
model_card_id_uuid | **str** | Unique object ID. | 

### Return type

[**DeleteModelCardResponse**](DeleteModelCardResponse.md)

### Authorization


[rime-api-key](../README.md#rime-api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### Example
```python

host_name = "http://<platform-domain>.rbst.io"

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rime-api-key
rime_api_key = os.environ["API_KEY"]

```

```python
import ri.apiclient
from ri import RIClient
from ri.apiclient.models.delete_model_card_response import DeleteModelCardResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

model_card_id_uuid = 'model_card_id_uuid_example'  # str 

try:
    # DeleteModelCard
    api_response: DeleteModelCardResponse = client.ModelCardServiceApi.delete_model_card(model_card_id_uuid)
    print("The response of ModelCardServiceApi->delete_model_card:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ModelCardServiceApi->delete_model_card: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_card**
> GetModelCardResponse  = get_model_card()

GetModelCard

Get Model Card By ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
model_card_id_uuid | **str** | Unique object ID. | 

### Return type

[**GetModelCardResponse**](GetModelCardResponse.md)

### Authorization


[rime-api-key](../README.md#rime-api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### Example
```python

host_name = "http://<platform-domain>.rbst.io"

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rime-api-key
rime_api_key = os.environ["API_KEY"]

```

```python
import ri.apiclient
from ri import RIClient
from ri.apiclient.models.get_model_card_response import GetModelCardResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

model_card_id_uuid = 'model_card_id_uuid_example'  # str 

try:
    # GetModelCard
    api_response: GetModelCardResponse = client.ModelCardServiceApi.get_model_card(model_card_id_uuid)
    print("The response of ModelCardServiceApi->get_model_card:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ModelCardServiceApi->get_model_card: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_model_cards**
> ListModelCardsResponse  = list_model_cards()

ListModelCards

List Model Cards by Project.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id | **str** | Uniquely specifies a Project.  List queries are kept as strings as they are used in query  parameters. | 

### Return type

[**ListModelCardsResponse**](ListModelCardsResponse.md)

### Authorization


[rime-api-key](../README.md#rime-api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### Example
```python

host_name = "http://<platform-domain>.rbst.io"

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rime-api-key
rime_api_key = os.environ["API_KEY"]

```

```python
import ri.apiclient
from ri import RIClient
from ri.apiclient.models.list_model_cards_response import ListModelCardsResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

project_id = 'project_id_example'  # str 

try:
    # ListModelCards
    api_response: ListModelCardsResponse = client.ModelCardServiceApi.list_model_cards(project_id)
    print("The response of ModelCardServiceApi->list_model_cards:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ModelCardServiceApi->list_model_cards: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_model_card**
> UpdateModelCardResponse  = update_model_card()

UpdateModelCard

Update Model Card by ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
model_card_model_card_id_uuid | **str** | Unique object ID. | 
model_card | [**UpdateModelCardRequestModelCard**](UpdateModelCardRequestModelCard.md) |  | [optional] 

### Return type

[**UpdateModelCardResponse**](UpdateModelCardResponse.md)

### Authorization


[rime-api-key](../README.md#rime-api-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### Example
```python

host_name = "http://<platform-domain>.rbst.io"

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rime-api-key
rime_api_key = os.environ["API_KEY"]

```

```python
import ri.apiclient
from ri import RIClient
from ri.apiclient.models.update_model_card_request import UpdateModelCardRequest
from ri.apiclient.models.update_model_card_response import UpdateModelCardResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

model_card_model_card_id_uuid = 'model_card_model_card_id_uuid_example'  # str 
model_card = UpdateModelCardRequestModelCard()  # UpdateModelCardRequestModelCard  (optional)

try:
    # UpdateModelCard
    api_response: UpdateModelCardResponse = client.ModelCardServiceApi.update_model_card(model_card_model_card_id_uuid, model_card=model_card)
    print("The response of ModelCardServiceApi->update_model_card:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling ModelCardServiceApi->update_model_card: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

