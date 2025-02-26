# ri.apiclient.AgentManagerApi

All URIs are relative to *http://&lt;platform-domain&gt;.rbst.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_agent**](#create_agent) | **POST** /v1/agents | CreateAgent
[**create_firewall_agent**](#create_firewall_agent) | **POST** /v1-beta/agents/firewall | CreateFirewallAgent
[**delete_agent**](#delete_agent) | **DELETE** /v1/agents/{agentId.uuid} | DeleteAgent
[**delete_firewall_instance**](#delete_firewall_instance) | **DELETE** /v1-beta/agents/firewall/{agentId.uuid}/firewall-instance/{firewallInstanceId.uuid} | DeleteFirewallInstance
[**get_agent**](#get_agent) | **GET** /v1/agents/{agentId.uuid} | GetAgent
[**get_upgrade_for_agent**](#get_upgrade_for_agent) | **GET** /v1-beta/agents/{agentId.uuid}/upgrade | GetUpgradeForAgent returns the desired state of the agent and the current status of the upgrade.
[**list_agents**](#list_agents) | **GET** /v1/agents | ListAgents
[**list_firewall_instances**](#list_firewall_instances) | **POST** /v1-beta/agents/firewall/instances | ListFirewallInstances
[**request_firewall_instance**](#request_firewall_instance) | **POST** /v1-beta/agents/firewall/{agentId.uuid}/firewall-instance/request | RequestFirewallInstance
[**upgrade_agent**](#upgrade_agent) | **POST** /v1-beta/agents/{agentId.uuid}/upgrade | UpgradeAgent starts the process of upgrading the agent to the version of the control plane

# **create_agent**
> CreateAgentResponse  = create_agent()

CreateAgent

Creates agent and returns the configuration for installing the agent.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | **str** | Agent name given by the user. | [optional] 
local_config | **object** | Configuration for local machine. | [optional] 
aws_config | [**AWSConfig**](AWSConfig.md) |  | [optional] 
gcp_config | [**GCPConfig**](GCPConfig.md) |  | [optional] 
azure_config | [**AzureConfig**](AzureConfig.md) |  | [optional] 

### Return type

[**CreateAgentResponse**](CreateAgentResponse.md)

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
from ri.apiclient.models.create_agent_request import CreateAgentRequest
from ri.apiclient.models.create_agent_response import CreateAgentResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

name = ''  # str  (optional)
local_config = ri.apiclient.models.local_config.localConfig()  # object  (optional)
aws_config = AWSConfig()  # AWSConfig  (optional)
gcp_config = GCPConfig()  # GCPConfig  (optional)
azure_config = AzureConfig()  # AzureConfig  (optional)

try:
    # CreateAgent
    api_response: CreateAgentResponse = client.AgentManagerApi.create_agent(name=name, local_config=local_config, aws_config=aws_config, gcp_config=gcp_config, azure_config=azure_config)
    print("The response of AgentManagerApi->create_agent:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling AgentManagerApi->create_agent: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_firewall_agent**
> CreateFirewallAgentResponse  = create_firewall_agent()

CreateFirewallAgent

Creates a firewall agent and returns the api key.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | **str** | The agent name given by the user. | [optional] 

### Return type

[**CreateFirewallAgentResponse**](CreateFirewallAgentResponse.md)

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
from ri.apiclient.models.create_firewall_agent_request import CreateFirewallAgentRequest
from ri.apiclient.models.create_firewall_agent_response import CreateFirewallAgentResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

name = ''  # str  (optional)

try:
    # CreateFirewallAgent
    api_response: CreateFirewallAgentResponse = client.AgentManagerApi.create_firewall_agent(name=name)
    print("The response of AgentManagerApi->create_firewall_agent:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling AgentManagerApi->create_firewall_agent: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent**
> object  = delete_agent()

DeleteAgent

Deletes a specified agent. Must be called on an already deactivated agent. An error is returned if the deletion fails or if the agent is not in a deletable state.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
agent_id_uuid | **str** | Unique object ID. | 

### Return type

**object**

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
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

agent_id_uuid = 'agent_id_uuid_example'  # str 

try:
    # DeleteAgent
    api_response: object = client.AgentManagerApi.delete_agent(agent_id_uuid)
    print("The response of AgentManagerApi->delete_agent:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling AgentManagerApi->delete_agent: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_firewall_instance**
> object  = delete_firewall_instance()

DeleteFirewallInstance

Marks the specified firewall instance with REQUESTED_DELETE status. Expects firewall agent in the DP to check for and eventually delete the firewall instance. This is intended to be used by external clients of the CP.  Example flow: user uses API to call DeleteFirewallInstance -> CP tries to delete the firewall instance with the DP and then delete it from the DB.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
agent_id_uuid | **str** | Unique object ID. | 
firewall_instance_id_uuid | **str** | Unique object ID. | 

### Return type

**object**

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
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

agent_id_uuid = 'agent_id_uuid_example'  # str 
firewall_instance_id_uuid = 'firewall_instance_id_uuid_example'  # str 

try:
    # DeleteFirewallInstance
    api_response: object = client.AgentManagerApi.delete_firewall_instance(agent_id_uuid, firewall_instance_id_uuid)
    print("The response of AgentManagerApi->delete_firewall_instance:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling AgentManagerApi->delete_firewall_instance: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent**
> GetAgentResponse  = get_agent()

GetAgent

Returns the agent that matches the specified ID.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
agent_id_uuid | **str** | Unique object ID. | 

### Return type

[**GetAgentResponse**](GetAgentResponse.md)

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
from ri.apiclient.models.get_agent_response import GetAgentResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

agent_id_uuid = 'agent_id_uuid_example'  # str 

try:
    # GetAgent
    api_response: GetAgentResponse = client.AgentManagerApi.get_agent(agent_id_uuid)
    print("The response of AgentManagerApi->get_agent:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling AgentManagerApi->get_agent: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_for_agent**
> GetUpgradeForAgentResponse  = get_upgrade_for_agent()

GetUpgradeForAgent returns the desired state of the agent and the current status of the upgrade.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
agent_id_uuid | **str** | Unique object ID. | 
agent_namespace | **str** | The namespace in which the agent is deployed. Since namespace is not known in the CP, it must be provided by the launcher when calling GetUpgradeForAgent. | 

### Return type

[**GetUpgradeForAgentResponse**](GetUpgradeForAgentResponse.md)

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
from ri.apiclient.models.get_upgrade_for_agent_response import GetUpgradeForAgentResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

agent_id_uuid = 'agent_id_uuid_example'  # str 
agent_namespace = 'agent_namespace_example'  # str 

try:
    # GetUpgradeForAgent returns the desired state of the agent and the current status of the upgrade.
    api_response: GetUpgradeForAgentResponse = client.AgentManagerApi.get_upgrade_for_agent(agent_id_uuid, agent_namespace)
    print("The response of AgentManagerApi->get_upgrade_for_agent:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling AgentManagerApi->get_upgrade_for_agent: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_agents**
> ListAgentsResponse  = list_agents()

ListAgents

Returns a paginated list of agents.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page_size | **str** | The maximum number of Agent objects to return in a single page. | [optional] 
page_token | **str** | Specifies a page of the list returned by a ListAgents query. The ListAgents query returns a pageToken when there is more than one page of results. Specify either this field or the firstPageQuery field. | [optional] 
first_page_query_agent_status_types | [**List[str]**](str.md) | Specifies a set of agent status types. The query filters for results that match the specified types.   - AGENT_STATUS_PENDING: Resources have been created for the agent but the agent has not started yet.  - AGENT_STATUS_ACTIVE: Agent can run jobs.  - AGENT_STATUS_UNRESPONSIVE: No agent heartbeat for three minutes.  - AGENT_STATUS_DEACTIVATED: Agent can no longer run jobs and can be deleted. (Deprecated after Deactivation and Deletion endpoints are combined) | [optional] 
first_page_query_agent_ids | [**List[str]**](str.md) | Specifies a set of agent IDs. The query filters for results that match the specified IDs. | [optional] 
first_page_query_type | **str** | Specifies the type of agent (validation or firewall). The query filters for results that match the specified type.   - AGENT_TYPE_VALIDATION: We use the zero value for VALIDATION for backwards compatibility with existing agents. protolint:disable:next ENUM_FIELD_NAMES_ZERO_VALUE_END_WITH | [optional] [default to AGENT_TYPE_VALIDATION]

### Return type

[**ListAgentsResponse**](ListAgentsResponse.md)

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
from ri.apiclient.models.list_agents_response import ListAgentsResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

page_size = 'page_size_example'  # str  (optional)
page_token = 'page_token_example'  # str  (optional)
first_page_query_agent_status_types = ['first_page_query_agent_status_types_example']  # List[str]  (optional)
first_page_query_agent_ids = ['first_page_query_agent_ids_example']  # List[str]  (optional)
first_page_query_type = AGENT_TYPE_VALIDATION  # str  (optional) (default to AGENT_TYPE_VALIDATION)

try:
    # ListAgents
    api_response: ListAgentsResponse = client.AgentManagerApi.list_agents(page_size=page_size, page_token=page_token, first_page_query_agent_status_types=first_page_query_agent_status_types, first_page_query_agent_ids=first_page_query_agent_ids, first_page_query_type=first_page_query_type)
    print("The response of AgentManagerApi->list_agents:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling AgentManagerApi->list_agents: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_firewall_instances**
> ListFirewallInstancesResponse  = list_firewall_instances()

ListFirewallInstances

Returns a paginated list of firewall instances.

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page_size | **str** |  | [optional] 
page_token | **str** | Specifies a page of the list returned by a ListFirewallInstances query. The ListFirewallInstances query returns a pageToken when there is more than one page of results. Specify either this field or the firstPageQuery field. | [optional] 
first_page_query | [**ListFirewallInstancesQuery**](ListFirewallInstancesQuery.md) |  | [optional] 

### Return type

[**ListFirewallInstancesResponse**](ListFirewallInstancesResponse.md)

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
from ri.apiclient.models.list_firewall_instances_request import ListFirewallInstancesRequest
from ri.apiclient.models.list_firewall_instances_response import ListFirewallInstancesResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

page_size = ''  # str  (optional)
page_token = ''  # str  (optional)
first_page_query = ListFirewallInstancesQuery()  # ListFirewallInstancesQuery  (optional)

try:
    # ListFirewallInstances
    api_response: ListFirewallInstancesResponse = client.AgentManagerApi.list_firewall_instances(page_size=page_size, page_token=page_token, first_page_query=first_page_query)
    print("The response of AgentManagerApi->list_firewall_instances:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling AgentManagerApi->list_firewall_instances: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_firewall_instance**
> RequestFirewallInstanceResponse  = request_firewall_instance()

RequestFirewallInstance

Creates a new firewall instance record in the DB with REQUESTED status. Expects firewall agent in the DP to check for and eventually deploy the firewall instance. This is intended to be used by external clients of the CP.  Example flow: user logs into the UI connected to the CP -> user tries to create agent in the UI -> UI calls RequestFirewallInstance -> CP tries to create the agent with the DP and then update the status

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
agent_id_uuid | **str** | Unique object ID. | 
agent_id | **object** | ID of the agent that will create the firewall instance. | [optional] 
config | [**FirewallRuleConfig**](FirewallRuleConfig.md) |  | 
description | **str** | Human-readable description of the firewall instance. | 
spec | [**FirewallInstanceDeploymentConfig**](FirewallInstanceDeploymentConfig.md) |  | [optional] 

### Return type

[**RequestFirewallInstanceResponse**](RequestFirewallInstanceResponse.md)

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
from ri.apiclient.models.request_firewall_instance_request import RequestFirewallInstanceRequest
from ri.apiclient.models.request_firewall_instance_response import RequestFirewallInstanceResponse
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

agent_id_uuid = 'agent_id_uuid_example'  # str 
agent_id = ri.apiclient.models.id_of_the_agent_that_will_create_the_firewall_instance/.ID of the agent that will create the firewall instance.()  # object  (optional)
config = FirewallRuleConfig()  # FirewallRuleConfig 
description = ''  # str 
spec = FirewallInstanceDeploymentConfig()  # FirewallInstanceDeploymentConfig  (optional)

try:
    # RequestFirewallInstance
    api_response: RequestFirewallInstanceResponse = client.AgentManagerApi.request_firewall_instance(agent_id_uuid, agent_id=agent_id, config, description, spec=spec)
    print("The response of AgentManagerApi->request_firewall_instance:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling AgentManagerApi->request_firewall_instance: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upgrade_agent**
> object  = upgrade_agent()

UpgradeAgent starts the process of upgrading the agent to the version of the control plane

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
agent_id_uuid | **str** | Unique object ID. | 
agent_id | **object** | Uniquely specifies an Agent. | [optional] 
custom_values | **Dict[str, str]** | Example:   {     \&quot;rimeAgent.images.agentImage.registry\&quot;: \&quot;docker.io\&quot;,   } | [optional] 

### Return type

**object**

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
from ri.apiclient.models.upgrade_agent_request import UpgradeAgentRequest
from ri.apiclient.models import *
from ri.apiclient.rest import ApiException
from pprint import pprint

# Configure the client
domain = "https://api.example.com"
api_key = "your_api_key"
client = RIClient(domain=domain, api_key=api_key)

agent_id_uuid = 'agent_id_uuid_example'  # str 
agent_id = ri.apiclient.models.uniquely_specifies_an_agent/.Uniquely specifies an Agent.()  # object  (optional)
custom_values = {
                    'key' : ''
                    }  # Dict[str, str]  (optional)

try:
    # UpgradeAgent starts the process of upgrading the agent to the version of the control plane
    api_response: object = client.AgentManagerApi.upgrade_agent(agent_id_uuid, agent_id=agent_id, custom_values=custom_values)
    print("The response of AgentManagerApi->upgrade_agent:\n")
    pprint(api_response)

except ApiException as e:
    print("Exception when calling AgentManagerApi->upgrade_agent: %s\n" % e)
```



[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

