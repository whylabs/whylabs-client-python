# whylabs_client.ApiKeyApi

All URIs are relative to *https://api.whylabsapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key**](ApiKeyApi.md#create_api_key) | **POST** /v0/organizations/{org_id}/api-key | Generate an API key for a user.
[**delete_api_key**](ApiKeyApi.md#delete_api_key) | **DELETE** /v1/api-key | Revoke the given API Key, removing its ability to access WhyLabs systems
[**generate_api_key**](ApiKeyApi.md#generate_api_key) | **POST** /v1/api-key | Generate an API key for a user.
[**list_api_key_metadata**](ApiKeyApi.md#list_api_key_metadata) | **GET** /v1/api-key | List API key metadata for a given organization
[**revoke_api_key**](ApiKeyApi.md#revoke_api_key) | **DELETE** /v0/organizations/{org_id}/api-key | Revoke the given API Key, removing its ability to access WhyLabs systems
[**validate_api_key**](ApiKeyApi.md#validate_api_key) | **GET** /v1/api-key/validate | Validate API key access


# **create_api_key**
> UserApiKey create_api_key(org_id, user_id)

Generate an API key for a user.

Generates an API key for a given user. Must be called either by system administrator or by the user themselves

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import api_key_api
from whylabs_client.model.user_api_key import UserApiKey
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
    api_instance = api_key_api.ApiKeyApi(api_client)
    org_id = "org-123" # str | Your company's unique organization ID
    user_id = "user-123" # str | The unique user ID in an organization.
    expiration_time = 1577836800000 # int, none_type | Expiration time in epoch milliseconds (optional)
    scopes = [
        ":user",
    ] # [str], none_type | Scopes of the token (optional)
    alias = "MLApplicationName" # str, none_type | A human-friendly name for the API Key (optional)

    # example passing only required values which don't have defaults set
    try:
        # Generate an API key for a user.
        api_response = api_instance.create_api_key(org_id, user_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ApiKeyApi->create_api_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate an API key for a user.
        api_response = api_instance.create_api_key(org_id, user_id, expiration_time=expiration_time, scopes=scopes, alias=alias)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ApiKeyApi->create_api_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Your company&#39;s unique organization ID |
 **user_id** | **str**| The unique user ID in an organization. |
 **expiration_time** | **int, none_type**| Expiration time in epoch milliseconds | [optional]
 **scopes** | **[str], none_type**| Scopes of the token | [optional]
 **alias** | **str, none_type**| A human-friendly name for the API Key | [optional]

### Return type

[**UserApiKey**](UserApiKey.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A object with key ID and other metadata about the key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key**
> UserApiKey delete_api_key(key_id)

Revoke the given API Key, removing its ability to access WhyLabs systems

Revokes the given API Key

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import api_key_api
from whylabs_client.model.user_api_key import UserApiKey
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
    api_instance = api_key_api.ApiKeyApi(api_client)
    key_id = "HMiFAgQeNb" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Revoke the given API Key, removing its ability to access WhyLabs systems
        api_response = api_instance.delete_api_key(key_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ApiKeyApi->delete_api_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**|  |

### Return type

[**UserApiKey**](UserApiKey.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DeleteApiKey 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_api_key**
> UserApiKey generate_api_key()

Generate an API key for a user.

Generates an API key for a given user. Must be called either by system administrator or by the user themselves

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import api_key_api
from whylabs_client.model.user_api_key import UserApiKey
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
    api_instance = api_key_api.ApiKeyApi(api_client)
    expiration_time = 1577836800000 # int, none_type |  (optional)
    scopes = [
        ":user",
    ] # [str], none_type |  (optional)
    resource_id = "model-123" # str, none_type |  (optional)
    alias = "MLApplicationName" # str, none_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate an API key for a user.
        api_response = api_instance.generate_api_key(expiration_time=expiration_time, scopes=scopes, resource_id=resource_id, alias=alias)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ApiKeyApi->generate_api_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expiration_time** | **int, none_type**|  | [optional]
 **scopes** | **[str], none_type**|  | [optional]
 **resource_id** | **str, none_type**|  | [optional]
 **alias** | **str, none_type**|  | [optional]

### Return type

[**UserApiKey**](UserApiKey.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A object with key ID and other metadata about the key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_key_metadata**
> ListUserApiKeys list_api_key_metadata()

List API key metadata for a given organization

Returns the API key metadata for a given organization

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import api_key_api
from whylabs_client.model.list_user_api_keys import ListUserApiKeys
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
    api_instance = api_key_api.ApiKeyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List API key metadata for a given organization
        api_response = api_instance.list_api_key_metadata()
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ApiKeyApi->list_api_key_metadata: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListUserApiKeys**](ListUserApiKeys.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of objects with key ID and other metadata about the keys, but no secret values |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_api_key**
> UserApiKey revoke_api_key(org_id, user_id, key_id)

Revoke the given API Key, removing its ability to access WhyLabs systems

Revokes the given API Key

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import api_key_api
from whylabs_client.model.user_api_key import UserApiKey
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
    api_instance = api_key_api.ApiKeyApi(api_client)
    org_id = "org-123" # str | 
    user_id = "user-123" # str | 
    key_id = "HMiFAgQeNb" # str | ID of the key to revoke

    # example passing only required values which don't have defaults set
    try:
        # Revoke the given API Key, removing its ability to access WhyLabs systems
        api_response = api_instance.revoke_api_key(org_id, user_id, key_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ApiKeyApi->revoke_api_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **user_id** | **str**|  |
 **key_id** | **str**| ID of the key to revoke |

### Return type

[**UserApiKey**](UserApiKey.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Revoked API Key&#39;s metadata |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_api_key**
> Response validate_api_key()

Validate API key access

Returns the status code 200 if the API key is valid, 403 if the API key is invalid

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import api_key_api
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
    api_instance = api_key_api.ApiKeyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Validate API key access
        api_response = api_instance.validate_api_key()
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ApiKeyApi->validate_api_key: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**200** | ValidateApiKey 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

