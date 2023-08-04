# whylabs_client.ModelsApi

All URIs are relative to *https://api.whylabsapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_model**](ModelsApi.md#create_model) | **POST** /v0/organizations/{org_id}/models | Create a model with a given name and a time period
[**deactivate_model**](ModelsApi.md#deactivate_model) | **DELETE** /v0/organizations/{org_id}/models/{model_id} | Mark a model as inactive
[**delete_entity_schema**](ModelsApi.md#delete_entity_schema) | **DELETE** /v0/organizations/{org_id}/models/{dataset_id}/schema | Delete the entity schema config for a given dataset.
[**delete_entity_schema_column**](ModelsApi.md#delete_entity_schema_column) | **DELETE** /v0/organizations/{org_id}/models/{dataset_id}/schema/column/{column_id} | Delete the entity schema of a single column for a given dataset.
[**delete_entity_schema_metric**](ModelsApi.md#delete_entity_schema_metric) | **DELETE** /v0/organizations/{org_id}/models/{dataset_id}/schema/metric/{metric_label} | Delete the schema of a single metric for a given dataset.
[**get_entity_schema**](ModelsApi.md#get_entity_schema) | **GET** /v0/organizations/{org_id}/models/{dataset_id}/schema | Get the entity schema config for a given dataset.
[**get_entity_schema_column**](ModelsApi.md#get_entity_schema_column) | **GET** /v0/organizations/{org_id}/models/{dataset_id}/schema/column/{column_id} | Get the entity schema of a single column for a given dataset.
[**get_model**](ModelsApi.md#get_model) | **GET** /v0/organizations/{org_id}/models/{model_id} | Get a model metadata
[**list_models**](ModelsApi.md#list_models) | **GET** /v0/organizations/{org_id}/models | Get a list of all of the model ids for an organization.
[**put_entity_schema**](ModelsApi.md#put_entity_schema) | **PUT** /v0/organizations/{org_id}/models/{dataset_id}/schema | Save the entity schema config for a given dataset.
[**put_entity_schema_column**](ModelsApi.md#put_entity_schema_column) | **PUT** /v0/organizations/{org_id}/models/{dataset_id}/schema/column/{column_id} | Save the entity schema of a single column for a given dataset.
[**put_entity_schema_metric**](ModelsApi.md#put_entity_schema_metric) | **PUT** /v0/organizations/{org_id}/models/{dataset_id}/schema/metric | Save the schema of a single metric for a given dataset.
[**update_model**](ModelsApi.md#update_model) | **PUT** /v0/organizations/{org_id}/models/{model_id} | Update a model&#39;s metadata


# **create_model**
> ModelMetadataResponse create_model(org_id, model_name, time_period)

Create a model with a given name and a time period

Create a model

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from whylabs_client.model.model_metadata_response import ModelMetadataResponse
from whylabs_client.model.model_type import ModelType
from whylabs_client.model.time_period import TimePeriod
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
    api_instance = models_api.ModelsApi(api_client)
    org_id = "org-123" # str | The organization ID
    model_name = "Credit-Score-1" # str | The name of a model
    time_period = TimePeriod("P1D") # TimePeriod | The [TimePeriod] for data aggregation/alerting for a model
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

[**ModelMetadataResponse**](ModelMetadataResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The [ModelMetadataResponse] if operation succeeds |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_model**
> ModelMetadataResponse deactivate_model(org_id, model_id)

Mark a model as inactive

Mark a model as inactive

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from whylabs_client.model.model_metadata_response import ModelMetadataResponse
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

[**ModelMetadataResponse**](ModelMetadataResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The [ModelMetadataResponse] if operation succeeds |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_entity_schema**
> Response delete_entity_schema(org_id, dataset_id)

Delete the entity schema config for a given dataset.

Delete the entity schema config for a given dataset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
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
    api_instance = models_api.ModelsApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete the entity schema config for a given dataset.
        api_response = api_instance.delete_entity_schema(org_id, dataset_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->delete_entity_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |

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
**0** | DeleteEntitySchema default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_entity_schema_column**
> Response delete_entity_schema_column(org_id, dataset_id, column_id)

Delete the entity schema of a single column for a given dataset.

Delete the entity schema of a single column for a given dataset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
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

[**Response**](Response.md)

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

# **delete_entity_schema_metric**
> Response delete_entity_schema_metric(org_id, dataset_id, metric_label)

Delete the schema of a single metric for a given dataset.

Delete the schema of a single metric for a given dataset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
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
    api_instance = models_api.ModelsApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    metric_label = "feature-123" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete the schema of a single metric for a given dataset.
        api_response = api_instance.delete_entity_schema_metric(org_id, dataset_id, metric_label)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->delete_entity_schema_metric: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **metric_label** | **str**|  |

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
**0** | DeleteEntitySchemaMetric default response |  -  |

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
> ModelMetadataResponse get_model(org_id, model_id)

Get a model metadata

Returns various metadata about a model

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from whylabs_client.model.model_metadata_response import ModelMetadataResponse
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

[**ModelMetadataResponse**](ModelMetadataResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A [ModelMetadataResponse] object if operation succeeds |  -  |

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

# **put_entity_schema**
> Response put_entity_schema(org_id, dataset_id, entity_schema)

Save the entity schema config for a given dataset.

Save the entity schema config for a given dataset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from whylabs_client.model.entity_schema import EntitySchema
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
        metrics={
            "key": MetricSchema(
                label="estimated_prediction.median",
                column="estimated_prediction",
                default_metric="median",
            ),
        },
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

[**Response**](Response.md)

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
> Response put_entity_schema_column(org_id, dataset_id, column_id, column_schema)

Save the entity schema of a single column for a given dataset.

Save the entity schema of a single column for a given dataset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from whylabs_client.model.column_schema import ColumnSchema
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

[**Response**](Response.md)

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

# **put_entity_schema_metric**
> Response put_entity_schema_metric(org_id, dataset_id, metric_schema)

Save the schema of a single metric for a given dataset.

Save the schema of a single metric for a given dataset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from whylabs_client.model.metric_schema import MetricSchema
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
    api_instance = models_api.ModelsApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    metric_schema = MetricSchema(
        label="estimated_prediction.median",
        column="estimated_prediction",
        default_metric="median",
    ) # MetricSchema | 

    # example passing only required values which don't have defaults set
    try:
        # Save the schema of a single metric for a given dataset.
        api_response = api_instance.put_entity_schema_metric(org_id, dataset_id, metric_schema)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->put_entity_schema_metric: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **metric_schema** | [**MetricSchema**](MetricSchema.md)|  |

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
**0** | PutEntitySchemaMetric default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_model**
> ModelMetadataResponse update_model(org_id, model_id, model_name, time_period)

Update a model's metadata

Update a model's metadata

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import models_api
from whylabs_client.model.model_metadata_response import ModelMetadataResponse
from whylabs_client.model.model_type import ModelType
from whylabs_client.model.time_period import TimePeriod
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
    api_instance = models_api.ModelsApi(api_client)
    org_id = "org-123" # str | The organization ID
    model_id = "model-123" # str | The model ID
    model_name = "Credit-Score-1" # str | The name of a model
    time_period = TimePeriod("P1D") # TimePeriod | The [TimePeriod] for data aggregation/alerting for a model
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

[**ModelMetadataResponse**](ModelMetadataResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The [ModelMetadataResponse] if operation succeeds |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

