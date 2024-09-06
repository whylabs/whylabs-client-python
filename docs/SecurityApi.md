# whylabs_client.SecurityApi

All URIs are relative to *https://api.whylabsapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**revoke_user_session**](SecurityApi.md#revoke_user_session) | **POST** /v1/security/session/revoke | Endpoint to revoke user session permissions
[**validate_user_session**](SecurityApi.md#validate_user_session) | **GET** /v1/security/session/validate | Endpoint to check if a user session is revoked


# **revoke_user_session**
> Response revoke_user_session(revoke_user_session_request)

Endpoint to revoke user session permissions

Endpoint to revoke user session permissions

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import security_api
from whylabs_client.model.revoke_user_session_request import RevokeUserSessionRequest
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
    api_instance = security_api.SecurityApi(api_client)
    revoke_user_session_request = RevokeUserSessionRequest(
        session_id="session_id_example",
    ) # RevokeUserSessionRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Endpoint to revoke user session permissions
        api_response = api_instance.revoke_user_session(revoke_user_session_request)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling SecurityApi->revoke_user_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **revoke_user_session_request** | [**RevokeUserSessionRequest**](RevokeUserSessionRequest.md)|  |

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
**200** | RevokeUserSession 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_user_session**
> ValidateUserSessionResponse validate_user_session(session_id)

Endpoint to check if a user session is revoked

Endpoint to check if a user session is revoked

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import security_api
from whylabs_client.model.validate_user_session_response import ValidateUserSessionResponse
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
    api_instance = security_api.SecurityApi(api_client)
    session_id = "session_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Endpoint to check if a user session is revoked
        api_response = api_instance.validate_user_session(session_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling SecurityApi->validate_user_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  |

### Return type

[**ValidateUserSessionResponse**](ValidateUserSessionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ValidateUserSession 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

