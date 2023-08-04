# whylabs_client.MonitorApi

All URIs are relative to *https://api.whylabsapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_analyzer**](MonitorApi.md#delete_analyzer) | **DELETE** /v0/organizations/{org_id}/models/{dataset_id}/monitor-config/analyzer/{analyzer_id} | Delete the analyzer config for a given dataset.
[**delete_monitor**](MonitorApi.md#delete_monitor) | **DELETE** /v0/organizations/{org_id}/models/{dataset_id}/monitor-config/monitor/{monitor_id} | Delete the monitor for a given dataset.
[**get_analyzer**](MonitorApi.md#get_analyzer) | **GET** /v0/organizations/{org_id}/models/{dataset_id}/monitor-config/analyzer/{analyzer_id} | Get the analyzer config for a given dataset.
[**get_monitor**](MonitorApi.md#get_monitor) | **GET** /v0/organizations/{org_id}/models/{dataset_id}/monitor-config/monitor/{monitor_id} | Get the monitor config for a given dataset.
[**get_monitor_config_v3**](MonitorApi.md#get_monitor_config_v3) | **GET** /v0/organizations/{org_id}/models/{dataset_id}/monitor-config/v3 | Get the monitor config document for a given dataset.
[**patch_monitor_config_v3**](MonitorApi.md#patch_monitor_config_v3) | **PATCH** /v0/organizations/{org_id}/models/{dataset_id}/monitor-config/v3 | Patch an updated monitor config document for a given dataset.
[**put_analyzer**](MonitorApi.md#put_analyzer) | **PUT** /v0/organizations/{org_id}/models/{dataset_id}/monitor-config/analyzer/{analyzer_id} | Save the analyzer config for a given dataset.
[**put_monitor**](MonitorApi.md#put_monitor) | **PUT** /v0/organizations/{org_id}/models/{dataset_id}/monitor-config/monitor/{monitor_id} | Save the monitor for a given dataset.
[**put_monitor_config_v3**](MonitorApi.md#put_monitor_config_v3) | **PUT** /v0/organizations/{org_id}/models/{dataset_id}/monitor-config/v3 | Save the monitor config document for a given dataset.
[**validate_monitor_config_v3**](MonitorApi.md#validate_monitor_config_v3) | **PUT** /v0/organizations/{org_id}/models/{dataset_id}/monitor-config/v3/validate | Validate the monitor config document for a given dataset.


# **delete_analyzer**
> Response delete_analyzer(org_id, dataset_id, analyzer_id)

Delete the analyzer config for a given dataset.

Delete the analyzer config for a given dataset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import monitor_api
from whylabs_client.model.response import Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.whylabsapp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "https://api.whylabsapp.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with whylabs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    analyzer_id = "drift-analyzer" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete the analyzer config for a given dataset.
        api_response = api_instance.delete_analyzer(org_id, dataset_id, analyzer_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MonitorApi->delete_analyzer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **analyzer_id** | **str**|  |

### Return type

[**Response**](Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DeleteAnalyzer default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_monitor**
> Response delete_monitor(org_id, dataset_id, monitor_id)

Delete the monitor for a given dataset.

Delete the monitor for a given dataset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import monitor_api
from whylabs_client.model.response import Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.whylabsapp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "https://api.whylabsapp.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with whylabs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    monitor_id = "drift-monitor-123" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete the monitor for a given dataset.
        api_response = api_instance.delete_monitor(org_id, dataset_id, monitor_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MonitorApi->delete_monitor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **monitor_id** | **str**|  |

### Return type

[**Response**](Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DeleteMonitor default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analyzer**
> str get_analyzer(org_id, dataset_id, analyzer_id)

Get the analyzer config for a given dataset.

Get the analyzer config for a given dataset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import monitor_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.whylabsapp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "https://api.whylabsapp.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with whylabs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    analyzer_id = "drift-analyzer" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get the analyzer config for a given dataset.
        api_response = api_instance.get_analyzer(org_id, dataset_id, analyzer_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MonitorApi->get_analyzer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **analyzer_id** | **str**|  |

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GetAnalyzer default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitor**
> str get_monitor(org_id, dataset_id, monitor_id)

Get the monitor config for a given dataset.

Get the monitor config for a given dataset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import monitor_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.whylabsapp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "https://api.whylabsapp.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with whylabs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    monitor_id = "drift-monitor-123" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get the monitor config for a given dataset.
        api_response = api_instance.get_monitor(org_id, dataset_id, monitor_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MonitorApi->get_monitor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **monitor_id** | **str**|  |

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GetMonitor default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitor_config_v3**
> str get_monitor_config_v3(org_id, dataset_id)

Get the monitor config document for a given dataset.

Get the monitor config document for a given dataset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import monitor_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.whylabsapp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "https://api.whylabsapp.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with whylabs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    include_entity_schema = True # bool, none_type |  (optional)
    include_entity_weights = True # bool, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the monitor config document for a given dataset.
        api_response = api_instance.get_monitor_config_v3(org_id, dataset_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MonitorApi->get_monitor_config_v3: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the monitor config document for a given dataset.
        api_response = api_instance.get_monitor_config_v3(org_id, dataset_id, include_entity_schema=include_entity_schema, include_entity_weights=include_entity_weights)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MonitorApi->get_monitor_config_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **include_entity_schema** | **bool, none_type**|  | [optional]
 **include_entity_weights** | **bool, none_type**|  | [optional]

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GetMonitorConfigV3 default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_monitor_config_v3**
> Response patch_monitor_config_v3(org_id, dataset_id, body)

Patch an updated monitor config document for a given dataset.

Save an updated monitor config document for a given dataset.  Monitors and analyzers matching an existing ID are replaced.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import monitor_api
from whylabs_client.model.response import Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.whylabsapp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "https://api.whylabsapp.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with whylabs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    body = "body_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Patch an updated monitor config document for a given dataset.
        api_response = api_instance.patch_monitor_config_v3(org_id, dataset_id, body)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MonitorApi->patch_monitor_config_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **body** | **str**|  |

### Return type

[**Response**](Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PatchMonitorConfigV3 default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_analyzer**
> Response put_analyzer(org_id, dataset_id, analyzer_id, body)

Save the analyzer config for a given dataset.

Save the analyzer config for a given dataset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import monitor_api
from whylabs_client.model.response import Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.whylabsapp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "https://api.whylabsapp.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with whylabs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    analyzer_id = "drift-analyzer" # str | 
    body = "body_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Save the analyzer config for a given dataset.
        api_response = api_instance.put_analyzer(org_id, dataset_id, analyzer_id, body)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MonitorApi->put_analyzer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **analyzer_id** | **str**|  |
 **body** | **str**|  |

### Return type

[**Response**](Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PutAnalyzer default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_monitor**
> Response put_monitor(org_id, dataset_id, monitor_id, body)

Save the monitor for a given dataset.

Save the monitor for a given dataset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import monitor_api
from whylabs_client.model.response import Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.whylabsapp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "https://api.whylabsapp.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with whylabs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    monitor_id = "drift-monitor-123" # str | 
    body = "body_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Save the monitor for a given dataset.
        api_response = api_instance.put_monitor(org_id, dataset_id, monitor_id, body)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MonitorApi->put_monitor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **monitor_id** | **str**|  |
 **body** | **str**|  |

### Return type

[**Response**](Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PutMonitor default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_monitor_config_v3**
> Response put_monitor_config_v3(org_id, dataset_id, body)

Save the monitor config document for a given dataset.

Save the monitor config document for a given dataset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import monitor_api
from whylabs_client.model.response import Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.whylabsapp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "https://api.whylabsapp.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with whylabs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    body = "body_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Save the monitor config document for a given dataset.
        api_response = api_instance.put_monitor_config_v3(org_id, dataset_id, body)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MonitorApi->put_monitor_config_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **body** | **str**|  |

### Return type

[**Response**](Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PutMonitorConfigV3 default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_monitor_config_v3**
> Response validate_monitor_config_v3(org_id, dataset_id, body)

Validate the monitor config document for a given dataset.

Validate the monitor config document for a given dataset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import monitor_api
from whylabs_client.model.response import Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.whylabsapp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "https://api.whylabsapp.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with whylabs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    body = "body_example" # str | 
    verbose = True # bool, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Validate the monitor config document for a given dataset.
        api_response = api_instance.validate_monitor_config_v3(org_id, dataset_id, body)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MonitorApi->validate_monitor_config_v3: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Validate the monitor config document for a given dataset.
        api_response = api_instance.validate_monitor_config_v3(org_id, dataset_id, body, verbose=verbose)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MonitorApi->validate_monitor_config_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **body** | **str**|  |
 **verbose** | **bool, none_type**|  | [optional]

### Return type

[**Response**](Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ValidateMonitorConfigV3 default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

