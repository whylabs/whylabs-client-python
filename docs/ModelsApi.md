# whylabs_client.ModelsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_model**](ModelsApi.md#create_model) | **POST** /v0/organizations/{org_id}/models | Create a model with a given name and a time period
[**deactivate_model**](ModelsApi.md#deactivate_model) | **DELETE** /v0/organizations/{org_id}/models/{model_id} | Mark a model as inactive
[**delete_analyzer**](ModelsApi.md#delete_analyzer) | **DELETE** /v0/organizations/{org_id}/models/{dataset_id}/monitor-config/analyzer/{analyzer_id} | Delete the analyzer config for a given dataset.
[**delete_entity_schema_column**](ModelsApi.md#delete_entity_schema_column) | **DELETE** /v0/organizations/{org_id}/models/{dataset_id}/schema/column/{column_id} | Delete the entity schema of a single column for a given dataset.
[**delete_monitor**](ModelsApi.md#delete_monitor) | **DELETE** /v0/organizations/{org_id}/models/{dataset_id}/monitor-config/monitor/{monitor_id} | Delete the monitor for a given dataset.
[**get_analyzer**](ModelsApi.md#get_analyzer) | **GET** /v0/organizations/{org_id}/models/{dataset_id}/monitor-config/analyzer/{analyzer_id} | Get the analyzer config for a given dataset.
[**get_entity_schema**](ModelsApi.md#get_entity_schema) | **GET** /v0/organizations/{org_id}/models/{dataset_id}/schema | Get the entity schema config for a given dataset.
[**get_entity_schema_column**](ModelsApi.md#get_entity_schema_column) | **GET** /v0/organizations/{org_id}/models/{dataset_id}/schema/column/{column_id} | Get the entity schema of a single column for a given dataset.
[**get_model**](ModelsApi.md#get_model) | **GET** /v0/organizations/{org_id}/models/{model_id} | Get a model metadata
[**get_monitor**](ModelsApi.md#get_monitor) | **GET** /v0/organizations/{org_id}/models/{dataset_id}/monitor-config/monitor/{monitor_id} | Get the monitor config for a given dataset.
[**get_monitor_config_v2**](ModelsApi.md#get_monitor_config_v2) | **GET** /v0/organizations/{org_id}/models/{model_id}/monitor-config/v2 | Get the monitor config for a given model or segment. The return of this api will include default values that we apply over any config that omits portions of the monitor config schema.
[**get_monitor_config_v3**](ModelsApi.md#get_monitor_config_v3) | **GET** /v0/organizations/{org_id}/models/{dataset_id}/monitor-config/v3 | Get the monitor config document for a given dataset.
[**get_monitor_config_v3_version**](ModelsApi.md#get_monitor_config_v3_version) | **GET** /v0/organizations/{org_id}/models/{dataset_id}/monitor-config/v3/versions/{version_id} | Get the monitor config document version for a given dataset.
[**list_models**](ModelsApi.md#list_models) | **GET** /v0/organizations/{org_id}/models | Get a list of all of the model ids for an organization.
[**list_monitor_config_v3_versions**](ModelsApi.md#list_monitor_config_v3_versions) | **GET** /v0/organizations/{org_id}/models/{dataset_id}/monitor-config/v3/versions | List the monitor config document versions for a given dataset.
[**list_segments**](ModelsApi.md#list_segments) | **GET** /v0/organizations/{org_id}/models/{model_id}/segments | Get a model metadata
[**put_analyzer**](ModelsApi.md#put_analyzer) | **PUT** /v0/organizations/{org_id}/models/{dataset_id}/monitor-config/analyzer/{analyzer_id} | Save the analyzer config for a given dataset.
[**put_entity_schema**](ModelsApi.md#put_entity_schema) | **PUT** /v0/organizations/{org_id}/models/{dataset_id}/schema | Save the entity schema config for a given dataset.
[**put_entity_schema_column**](ModelsApi.md#put_entity_schema_column) | **PUT** /v0/organizations/{org_id}/models/{dataset_id}/schema/column/{column_id} | Save the entity schema of a single column for a given dataset.
[**put_monitor**](ModelsApi.md#put_monitor) | **PUT** /v0/organizations/{org_id}/models/{dataset_id}/monitor-config/monitor/{monitor_id} | Save the monitor for a given dataset.
[**put_monitor_config_v2**](ModelsApi.md#put_monitor_config_v2) | **PUT** /v0/organizations/{org_id}/models/{model_id}/monitor-config/v2 | Save the monitor config for a given model or segment
[**put_monitor_config_v3**](ModelsApi.md#put_monitor_config_v3) | **PUT** /v0/organizations/{org_id}/models/{dataset_id}/monitor-config/v3 | Save the monitor config document for a given dataset.
[**put_request_monitor_run_config**](ModelsApi.md#put_request_monitor_run_config) | **PUT** /v0/organizations/{org_id}/models/{dataset_id}/request-monitor-run | Put the RequestMonitorRun config into S3.
[**put_segments**](ModelsApi.md#put_segments) | **PUT** /v0/organizations/{org_id}/models/{model_id}/segments | Add a segment to the dataset
[**update_model**](ModelsApi.md#update_model) | **PUT** /v0/organizations/{org_id}/models/{model_id} | Update a model&#39;s metadata
[**validate_monitor_config_v3**](ModelsApi.md#validate_monitor_config_v3) | **PUT** /v0/organizations/{org_id}/models/{dataset_id}/monitor-config/v3/validate | Validate the monitor config document for a given dataset.


# **create_model**
> ModelMetadata create_model(org_id, model_name, time_period)

Create a model with a given name and a time period

Create a model

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from whylabs_client.model.model_metadata import ModelMetadata
from whylabs_client.model.model_type import ModelType
from whylabs_client.model.time_period import TimePeriod
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
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
    api_instance = models_api.ModelsApi(api_client)
    org_id = "org-123" # str | The organization ID
    model_name = "Credit-Score-1" # str | The name of a model
    time_period = TimePeriod("P1M") # TimePeriod | The [TimePeriod] for data aggregation/alerting for a model
    model_type = ModelType("CLASSIFICATION") # ModelType | The [ModelType] of the dataset (optional)
    model_id = "model-123" # str, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a model with a given name and a time period
        api_response = api_instance.create_model(org_id, model_name, time_period)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->create_model: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a model with a given name and a time period
        api_response = api_instance.create_model(org_id, model_name, time_period, model_type=model_type, model_id=model_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->create_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The organization ID |
 **model_name** | **str**| The name of a model |
 **time_period** | **TimePeriod**| The [TimePeriod] for data aggregation/alerting for a model |
 **model_type** | **ModelType**| The [ModelType] of the dataset | [optional]
 **model_id** | **str, none_type**|  | [optional]

### Return type

[**ModelMetadata**](ModelMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The [ModelMetadata] if operation succeeds |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_model**
> ModelMetadata deactivate_model(org_id, model_id)

Mark a model as inactive

Mark a model as inactive

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from whylabs_client.model.model_metadata import ModelMetadata
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
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
    api_instance = models_api.ModelsApi(api_client)
    org_id = "org-123" # str | The organization ID
    model_id = "model-123" # str | The model ID

    # example passing only required values which don't have defaults set
    try:
        # Mark a model as inactive
        api_response = api_instance.deactivate_model(org_id, model_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->deactivate_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The organization ID |
 **model_id** | **str**| The model ID |

### Return type

[**ModelMetadata**](ModelMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The [ModelMetadata] if operation succeeds |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_analyzer**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_analyzer(org_id, dataset_id, analyzer_id)

Delete the analyzer config for a given dataset.

Delete the analyzer config for a given dataset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
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
    api_instance = models_api.ModelsApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    analyzer_id = "drift-analyzer" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete the analyzer config for a given dataset.
        api_response = api_instance.delete_analyzer(org_id, dataset_id, analyzer_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->delete_analyzer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **analyzer_id** | **str**|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

# **delete_entity_schema_column**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_entity_schema_column(org_id, dataset_id, column_id)

Delete the entity schema of a single column for a given dataset.

Delete the entity schema of a single column for a given dataset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
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
    api_instance = models_api.ModelsApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    column_id = "feature-123" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete the entity schema of a single column for a given dataset.
        api_response = api_instance.delete_entity_schema_column(org_id, dataset_id, column_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->delete_entity_schema_column: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **column_id** | **str**|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DeleteEntitySchemaColumn default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_monitor**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_monitor(org_id, dataset_id, monitor_id)

Delete the monitor for a given dataset.

Delete the monitor for a given dataset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
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
    api_instance = models_api.ModelsApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    monitor_id = "drift-monitor-123" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete the monitor for a given dataset.
        api_response = api_instance.delete_monitor(org_id, dataset_id, monitor_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->delete_monitor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **monitor_id** | **str**|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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
from whylabs_client.api import models_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
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
    api_instance = models_api.ModelsApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    analyzer_id = "drift-analyzer" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get the analyzer config for a given dataset.
        api_response = api_instance.get_analyzer(org_id, dataset_id, analyzer_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->get_analyzer: %s\n" % e)
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

# **get_entity_schema**
> EntitySchema get_entity_schema(org_id, dataset_id)

Get the entity schema config for a given dataset.

Get the entity schema config for a given dataset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from whylabs_client.model.entity_schema import EntitySchema
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
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
    api_instance = models_api.ModelsApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get the entity schema config for a given dataset.
        api_response = api_instance.get_entity_schema(org_id, dataset_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->get_entity_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |

### Return type

[**EntitySchema**](EntitySchema.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GetEntitySchema default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_schema_column**
> ColumnSchema get_entity_schema_column(org_id, dataset_id, column_id)

Get the entity schema of a single column for a given dataset.

Get the entity schema of a single column for a given dataset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from whylabs_client.model.column_schema import ColumnSchema
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
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
    api_instance = models_api.ModelsApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    column_id = "feature-123" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get the entity schema of a single column for a given dataset.
        api_response = api_instance.get_entity_schema_column(org_id, dataset_id, column_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->get_entity_schema_column: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **column_id** | **str**|  |

### Return type

[**ColumnSchema**](ColumnSchema.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GetEntitySchemaColumn default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model**
> ModelMetadata get_model(org_id, model_id)

Get a model metadata

Returns various metadata about a model

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from whylabs_client.model.model_metadata import ModelMetadata
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
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
    api_instance = models_api.ModelsApi(api_client)
    org_id = "org-123" # str | The name of an organization
    model_id = "model-123" # str | The ID of a model

    # example passing only required values which don't have defaults set
    try:
        # Get a model metadata
        api_response = api_instance.get_model(org_id, model_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->get_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The name of an organization |
 **model_id** | **str**| The ID of a model |

### Return type

[**ModelMetadata**](ModelMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A [ModelMetadata] object if operation succeeds |  -  |

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
from whylabs_client.api import models_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
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
    api_instance = models_api.ModelsApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    monitor_id = "drift-monitor-123" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get the monitor config for a given dataset.
        api_response = api_instance.get_monitor(org_id, dataset_id, monitor_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->get_monitor: %s\n" % e)
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

# **get_monitor_config_v2**
> GetMonitorConfigV2Response get_monitor_config_v2(org_id, model_id)

Get the monitor config for a given model or segment. The return of this api will include default values that we apply over any config that omits portions of the monitor config schema.

Get the monitor config for a given model or segment. The return of this api will include default values that we apply over any config that omits portions of the monitor config schema.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from whylabs_client.model.segment_tag import SegmentTag
from whylabs_client.model.get_monitor_config_v2_response import GetMonitorConfigV2Response
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
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
    api_instance = models_api.ModelsApi(api_client)
    org_id = "org-123" # str | 
    model_id = "model-123" # str | 
    segment_tags = [
        SegmentTag(
            key="key_example",
            value="value_example",
        ),
    ] # [SegmentTag], none_type |  (optional)
    segment_tags_json = "segment_tags_json_example" # str, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the monitor config for a given model or segment. The return of this api will include default values that we apply over any config that omits portions of the monitor config schema.
        api_response = api_instance.get_monitor_config_v2(org_id, model_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->get_monitor_config_v2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the monitor config for a given model or segment. The return of this api will include default values that we apply over any config that omits portions of the monitor config schema.
        api_response = api_instance.get_monitor_config_v2(org_id, model_id, segment_tags=segment_tags, segment_tags_json=segment_tags_json)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->get_monitor_config_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **model_id** | **str**|  |
 **segment_tags** | [**[SegmentTag], none_type**](SegmentTag.md)|  | [optional]
 **segment_tags_json** | **str, none_type**|  | [optional]

### Return type

[**GetMonitorConfigV2Response**](GetMonitorConfigV2Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GetMonitorConfigV2 default response |  -  |

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
from whylabs_client.api import models_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
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
    api_instance = models_api.ModelsApi(api_client)
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
        print("Exception when calling ModelsApi->get_monitor_config_v3: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the monitor config document for a given dataset.
        api_response = api_instance.get_monitor_config_v3(org_id, dataset_id, include_entity_schema=include_entity_schema, include_entity_weights=include_entity_weights)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->get_monitor_config_v3: %s\n" % e)
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

# **get_monitor_config_v3_version**
> str get_monitor_config_v3_version(org_id, dataset_id, version_id)

Get the monitor config document version for a given dataset.

Get the monitor config document version for a given dataset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
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
    api_instance = models_api.ModelsApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    version_id = "4920545486e2a4cdf0f770c09748e663" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get the monitor config document version for a given dataset.
        api_response = api_instance.get_monitor_config_v3_version(org_id, dataset_id, version_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->get_monitor_config_v3_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **version_id** | **str**|  |

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
**0** | GetMonitorConfigV3Version default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_models**
> ListModelsResponse list_models(org_id)

Get a list of all of the model ids for an organization.

Get a list of all of the model ids for an organization.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from whylabs_client.model.list_models_response import ListModelsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
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
    api_instance = models_api.ModelsApi(api_client)
    org_id = "org-123" # str | Your company's unique organization ID

    # example passing only required values which don't have defaults set
    try:
        # Get a list of all of the model ids for an organization.
        api_response = api_instance.list_models(org_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->list_models: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Your company&#39;s unique organization ID |

### Return type

[**ListModelsResponse**](ListModelsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A list of model summary items |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_monitor_config_v3_versions**
> [MonitorConfigVersion] list_monitor_config_v3_versions(org_id, dataset_id)

List the monitor config document versions for a given dataset.

List the monitor config document versions for a given dataset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from whylabs_client.model.monitor_config_version import MonitorConfigVersion
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
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
    api_instance = models_api.ModelsApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 

    # example passing only required values which don't have defaults set
    try:
        # List the monitor config document versions for a given dataset.
        api_response = api_instance.list_monitor_config_v3_versions(org_id, dataset_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->list_monitor_config_v3_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |

### Return type

[**[MonitorConfigVersion]**](MonitorConfigVersion.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ListMonitorConfigV3Versions default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_segments**
> ListSegmentsResponse list_segments(org_id, model_id)

Get a model metadata

Returns the list of Segments for a given model

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from whylabs_client.model.list_segments_response import ListSegmentsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
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
    api_instance = models_api.ModelsApi(api_client)
    org_id = "org-123" # str | The name of an organization
    model_id = "model-123" # str | The ID of a model

    # example passing only required values which don't have defaults set
    try:
        # Get a model metadata
        api_response = api_instance.list_segments(org_id, model_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->list_segments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The name of an organization |
 **model_id** | **str**| The ID of a model |

### Return type

[**ListSegmentsResponse**](ListSegmentsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A [ListSegmentsResponse] object if operation succeeds |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_analyzer**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} put_analyzer(org_id, dataset_id, analyzer_id, body)

Save the analyzer config for a given dataset.

Save the analyzer config for a given dataset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
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
    api_instance = models_api.ModelsApi(api_client)
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
        print("Exception when calling ModelsApi->put_analyzer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **analyzer_id** | **str**|  |
 **body** | **str**|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

# **put_entity_schema**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} put_entity_schema(org_id, dataset_id, entity_schema)

Save the entity schema config for a given dataset.

Save the entity schema config for a given dataset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from whylabs_client.model.entity_schema import EntitySchema
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
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
    api_instance = models_api.ModelsApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    entity_schema = EntitySchema(
        columns={
            "key": ColumnSchema(
                classifier="input",
                data_type="fractional",
                discreteness="discrete",
            ),
        },
        metadata=SchemaMetadata(
            version=1,
            updated_timestamp=1,
            author="author_example",
        ),
    ) # EntitySchema | 

    # example passing only required values which don't have defaults set
    try:
        # Save the entity schema config for a given dataset.
        api_response = api_instance.put_entity_schema(org_id, dataset_id, entity_schema)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->put_entity_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **entity_schema** | [**EntitySchema**](EntitySchema.md)|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PutEntitySchema default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_entity_schema_column**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} put_entity_schema_column(org_id, dataset_id, column_id, column_schema)

Save the entity schema of a single column for a given dataset.

Save the entity schema of a single column for a given dataset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from whylabs_client.model.column_schema import ColumnSchema
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
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
    api_instance = models_api.ModelsApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    column_id = "feature-123" # str | 
    column_schema = ColumnSchema(
        classifier="input",
        data_type="fractional",
        discreteness="discrete",
    ) # ColumnSchema | 

    # example passing only required values which don't have defaults set
    try:
        # Save the entity schema of a single column for a given dataset.
        api_response = api_instance.put_entity_schema_column(org_id, dataset_id, column_id, column_schema)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->put_entity_schema_column: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **column_id** | **str**|  |
 **column_schema** | [**ColumnSchema**](ColumnSchema.md)|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PutEntitySchemaColumn default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_monitor**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} put_monitor(org_id, dataset_id, monitor_id, body)

Save the monitor for a given dataset.

Save the monitor for a given dataset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
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
    api_instance = models_api.ModelsApi(api_client)
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
        print("Exception when calling ModelsApi->put_monitor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **monitor_id** | **str**|  |
 **body** | **str**|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

# **put_monitor_config_v2**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} put_monitor_config_v2(org_id, model_id, dataset_request_monitor_config)

Save the monitor config for a given model or segment

Save the monitor config for a given model or segment

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from whylabs_client.model.segment_tag import SegmentTag
from whylabs_client.model.dataset_request_monitor_config import DatasetRequestMonitorConfig
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
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
    api_instance = models_api.ModelsApi(api_client)
    org_id = "org-123" # str | 
    model_id = "model-123" # str | 
    dataset_request_monitor_config = DatasetRequestMonitorConfig(
        config=RequestMonitorConfig(
            schema_version="schema_version_example",
            num_std_dev=3.14,
            reference=MonitorRequestReference(
                type=MonitorRequestReferenceType("reference_profile"),
                profile_timestamp=1,
                profile_id="profile_id_example",
                num_batches=1,
            ),
            missing_recent_data=MissingRecentDataRequestConfig(
                enable=True,
            ),
            missing_recent_profiles=MissingRecentProfilesRequestConfig(
                enable=True,
            ),
            distribution=DistributionMonitorRequestConfig(
                enable=True,
                threshold=3.14,
            ),
            missing_values=MissingValuesMonitorRequestConfig(
                enable=True,
                threshold=3.14,
                threshold_lower_bound=3.14,
                threshold_upper_bound=3.14,
            ),
            unique_values=UniqueValuesMonitorRequestConfig(
                enable=True,
                min_record_count=1,
                min_threshold=3.14,
                max_threshold=3.14,
            ),
            datatype=DatatypeMonitorRequestConfig(
                enable=True,
            ),
            seasonal_arima=SeasonalARIMARequestConfig(
                enable=True,
                seasonality_batches=1,
                metrics=[
                    WhyLogsMetric("TotalCount"),
                ],
            ),
        ),
        per_feature_config={
            "key": RequestFeatureMonitorConfig(
                distribution=DistributionMonitorRequestConfig(
                    enable=True,
                    threshold=3.14,
                ),
                missing_values=MissingValuesMonitorRequestConfig(
                    enable=True,
                    threshold=3.14,
                    threshold_lower_bound=3.14,
                    threshold_upper_bound=3.14,
                ),
                unique_values=UniqueValuesMonitorRequestConfig(
                    enable=True,
                    min_record_count=1,
                    min_threshold=3.14,
                    max_threshold=3.14,
                ),
                datatype=DatatypeMonitorRequestConfig(
                    enable=True,
                ),
                seasonal_arima=SeasonalARIMARequestConfig(
                    enable=True,
                    seasonality_batches=1,
                    metrics=[
                        WhyLogsMetric("TotalCount"),
                    ],
                ),
            ),
        },
    ) # DatasetRequestMonitorConfig | 
    segment_tags = [
        SegmentTag(
            key="key_example",
            value="value_example",
        ),
    ] # [SegmentTag], none_type |  (optional)
    segment_tags_json = "segment_tags_json_example" # str, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Save the monitor config for a given model or segment
        api_response = api_instance.put_monitor_config_v2(org_id, model_id, dataset_request_monitor_config)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->put_monitor_config_v2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Save the monitor config for a given model or segment
        api_response = api_instance.put_monitor_config_v2(org_id, model_id, dataset_request_monitor_config, segment_tags=segment_tags, segment_tags_json=segment_tags_json)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->put_monitor_config_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **model_id** | **str**|  |
 **dataset_request_monitor_config** | [**DatasetRequestMonitorConfig**](DatasetRequestMonitorConfig.md)|  |
 **segment_tags** | [**[SegmentTag], none_type**](SegmentTag.md)|  | [optional]
 **segment_tags_json** | **str, none_type**|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PutMonitorConfigV2 default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_monitor_config_v3**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} put_monitor_config_v3(org_id, dataset_id, body)

Save the monitor config document for a given dataset.

Save the monitor config document for a given dataset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
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
    api_instance = models_api.ModelsApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    body = "body_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Save the monitor config document for a given dataset.
        api_response = api_instance.put_monitor_config_v3(org_id, dataset_id, body)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->put_monitor_config_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **body** | **str**|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

# **put_request_monitor_run_config**
> str put_request_monitor_run_config(org_id, dataset_id, inline_object)

Put the RequestMonitorRun config into S3.

Put the RequestMonitorRun config into S3.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from whylabs_client.model.inline_object import InlineObject
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
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
    api_instance = models_api.ModelsApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    inline_object = InlineObject(
        analyzer_ids=[
            "drift-analyzer",
        ],
        overwrite=True,
        start_timestamp=1577836800000,
        end_timestamp=1893456000000,
    ) # InlineObject | 

    # example passing only required values which don't have defaults set
    try:
        # Put the RequestMonitorRun config into S3.
        api_response = api_instance.put_request_monitor_run_config(org_id, dataset_id, inline_object)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->put_request_monitor_run_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **inline_object** | [**InlineObject**](InlineObject.md)|  |

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PutRequestMonitorRunConfig default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_segments**
> SegmentMetadata put_segments(org_id, model_id, segment_tag)

Add a segment to the dataset

Return 200 if succeeds

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from whylabs_client.model.segment_tag import SegmentTag
from whylabs_client.model.segment_metadata import SegmentMetadata
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
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
    api_instance = models_api.ModelsApi(api_client)
    org_id = "org-123" # str | The name of an organization
    model_id = "model-123" # str | The ID of a model
    segment_tag = [
        SegmentTag(
            key="key_example",
            value="value_example",
        ),
    ] # [SegmentTag] | List of segment tags to create the segment for

    # example passing only required values which don't have defaults set
    try:
        # Add a segment to the dataset
        api_response = api_instance.put_segments(org_id, model_id, segment_tag)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->put_segments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The name of an organization |
 **model_id** | **str**| The ID of a model |
 **segment_tag** | [**[SegmentTag]**](SegmentTag.md)| List of segment tags to create the segment for |

### Return type

[**SegmentMetadata**](SegmentMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A [SegmentMetadata] object if operation succeeds |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_model**
> ModelMetadata update_model(org_id, model_id, model_name, time_period)

Update a model's metadata

Update a model's metadata

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from whylabs_client.model.model_metadata import ModelMetadata
from whylabs_client.model.model_type import ModelType
from whylabs_client.model.time_period import TimePeriod
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
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
    api_instance = models_api.ModelsApi(api_client)
    org_id = "org-123" # str | The organization ID
    model_id = "model-123" # str | The model ID
    model_name = "Credit-Score-1" # str | The name of a model
    time_period = TimePeriod("P1M") # TimePeriod | The [TimePeriod] for data aggregation/alerting for a model
    model_type = ModelType("CLASSIFICATION") # ModelType | The [ModelType] of the dataset (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a model's metadata
        api_response = api_instance.update_model(org_id, model_id, model_name, time_period)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->update_model: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a model's metadata
        api_response = api_instance.update_model(org_id, model_id, model_name, time_period, model_type=model_type)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->update_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The organization ID |
 **model_id** | **str**| The model ID |
 **model_name** | **str**| The name of a model |
 **time_period** | **TimePeriod**| The [TimePeriod] for data aggregation/alerting for a model |
 **model_type** | **ModelType**| The [ModelType] of the dataset | [optional]

### Return type

[**ModelMetadata**](ModelMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The [ModelMetadata] if operation succeeds |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_monitor_config_v3**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} validate_monitor_config_v3(org_id, dataset_id, body)

Validate the monitor config document for a given dataset.

Validate the monitor config document for a given dataset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
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
    api_instance = models_api.ModelsApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    body = "body_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Validate the monitor config document for a given dataset.
        api_response = api_instance.validate_monitor_config_v3(org_id, dataset_id, body)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->validate_monitor_config_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **body** | **str**|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

