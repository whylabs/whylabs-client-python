# whylabs_client.SessionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close_session**](SessionsApi.md#close_session) | **POST** /v0/sessions/{session_token}/close | naddeo Close a session, triggering its display in whylabs and making it no longer accept any additional data.
[**create_dataset_profile_upload**](SessionsApi.md#create_dataset_profile_upload) | **POST** /v0/sessions/{session_token}/upload | Create an upload for a given session.
[**create_session**](SessionsApi.md#create_session) | **POST** /v0/sessions | Create a new session that can be used to upload dataset profiles from whylogs for display in whylabs.
[**get_session**](SessionsApi.md#get_session) | **GET** /v0/sessions/{session_token} | Get information about a session.


# **close_session**
> CloseSessionResponse close_session(session_token)

naddeo Close a session, triggering its display in whylabs and making it no longer accept any additional data.

naddeo Close a session, triggering its display in whylabs and making it no longer accept any additional data.

### Example


```python
import time
import whylabs_client
from whylabs_client.api import sessions_api
from whylabs_client.model.close_session_response import CloseSessionResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with whylabs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sessions_api.SessionsApi(api_client)
    session_token = "session_token_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # naddeo Close a session, triggering its display in whylabs and making it no longer accept any additional data.
        api_response = api_instance.close_session(session_token)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling SessionsApi->close_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_token** | **str**|  |

### Return type

[**CloseSessionResponse**](CloseSessionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CloseSession default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dataset_profile_upload**
> CreateSessionUploadResponse create_dataset_profile_upload(session_token)

Create an upload for a given session.

Create an upload for a given session.

### Example


```python
import time
import whylabs_client
from whylabs_client.api import sessions_api
from whylabs_client.model.create_session_upload_response import CreateSessionUploadResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with whylabs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sessions_api.SessionsApi(api_client)
    session_token = "session_token_example" # str | 
    dataset_timestamp = 1577836800000 # int, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an upload for a given session.
        api_response = api_instance.create_dataset_profile_upload(session_token)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling SessionsApi->create_dataset_profile_upload: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an upload for a given session.
        api_response = api_instance.create_dataset_profile_upload(session_token, dataset_timestamp=dataset_timestamp)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling SessionsApi->create_dataset_profile_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_token** | **str**|  |
 **dataset_timestamp** | **int, none_type**|  | [optional]

### Return type

[**CreateSessionUploadResponse**](CreateSessionUploadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A url that a dataset profile can be uploaded to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_session**
> CreateSessionResponse create_session()

Create a new session that can be used to upload dataset profiles from whylogs for display in whylabs.

Create a new session that can be used to upload dataset profiles from whylogs for display in whylabs.

### Example


```python
import time
import whylabs_client
from whylabs_client.api import sessions_api
from whylabs_client.model.create_session_response import CreateSessionResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with whylabs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sessions_api.SessionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Create a new session that can be used to upload dataset profiles from whylogs for display in whylabs.
        api_response = api_instance.create_session()
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling SessionsApi->create_session: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateSessionResponse**](CreateSessionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A new session id that can be used to upload dataset profiles. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session**
> GetSessionResponse get_session(session_token)

Get information about a session.

Get information about a session.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import sessions_api
from whylabs_client.model.get_session_response import GetSessionResponse
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
    api_instance = sessions_api.SessionsApi(api_client)
    session_token = "session_token_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get information about a session.
        api_response = api_instance.get_session(session_token)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling SessionsApi->get_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_token** | **str**|  |

### Return type

[**GetSessionResponse**](GetSessionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GetSession default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

