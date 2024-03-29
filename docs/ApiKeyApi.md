# whylabs_client.ApiKeyApi

All URIs are relative to *https://api.whylabsapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key**](ApiKeyApi.md#create_api_key) | **POST** /v0/organizations/{org_id}/api-key | Generate an API key for a user.
[**revoke_api_key**](ApiKeyApi.md#revoke_api_key) | **DELETE** /v0/organizations/{org_id}/api-key | Revoke the given API Key, removing its ability to access WhyLabs systems


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
    alias = "MLApplicationName" # str, none_type | A human-friendly name for the API Key  An object with key ID and other metadata about the key (optional)

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
 **alias** | **str, none_type**| A human-friendly name for the API Key  An object with key ID and other metadata about the key | [optional]

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
**0** | A object with key ID and other metadata about the key |  -  |

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
    key_id = "HMiFAgQeNb" # str | ID of the key to revoke  Metadata for the revoked API Key

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
 **key_id** | **str**| ID of the key to revoke  Metadata for the revoked API Key |

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
**0** | Revoked API Key&#39;s metadata |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

