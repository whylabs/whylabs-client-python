# whylabs_client.SessionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dataset_profile_upload**](SessionsApi.md#create_dataset_profile_upload) | **POST** /v0/sessions/{session_id}/upload | Create an upload for a given session.
[**create_session**](SessionsApi.md#create_session) | **POST** /v0/sessions | Create a new session that can be used to upload dataset profiles from whylogs for display in whylabs.
[**get_session**](SessionsApi.md#get_session) | **GET** /v0/sessions/{session_id} | Get information about a session.


# **create_dataset_profile_upload**
> AsyncLogResponse create_dataset_profile_upload(session_id, log_async_request)

Create an upload for a given session.

Create an upload for a given session.

### Example


```python
import time
import whylabs_client
from whylabs_client.api import sessions_api
from whylabs_client.model.log_async_request import LogAsyncRequest
from whylabs_client.model.async_log_response import AsyncLogResponse
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
    session_id = "session_id_example" # str | 
    log_async_request = LogAsyncRequest(
        dataset_timestamp=1,
        segment_tags=[
            SegmentTag(
                key="key_example",
                value="value_example",
            ),
        ],
    ) # LogAsyncRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create an upload for a given session.
        api_response = api_instance.create_dataset_profile_upload(session_id, log_async_request)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling SessionsApi->create_dataset_profile_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  |
 **log_async_request** | [**LogAsyncRequest**](LogAsyncRequest.md)|  |

### Return type

[**AsyncLogResponse**](AsyncLogResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A url that a dataset profile can be uploaded to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_session**
> CreateSessionResponse create_session(create_session_request)

Create a new session that can be used to upload dataset profiles from whylogs for display in whylabs.

Create a new session that can be used to upload dataset profiles from whylogs for display in whylabs.

### Example


```python
import time
import whylabs_client
from whylabs_client.api import sessions_api
from whylabs_client.model.create_session_response import CreateSessionResponse
from whylabs_client.model.create_session_request import CreateSessionRequest
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
    create_session_request = CreateSessionRequest(
        user_id="user_id_example",
    ) # CreateSessionRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new session that can be used to upload dataset profiles from whylogs for display in whylabs.
        api_response = api_instance.create_session(create_session_request)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling SessionsApi->create_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_session_request** | [**CreateSessionRequest**](CreateSessionRequest.md)|  |

### Return type

[**CreateSessionResponse**](CreateSessionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A new session id that can be used to upload dataset profiles. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session**
> GetSessionResponse get_session(session_id)

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
    session_id = "session_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get information about a session.
        api_response = api_instance.get_session(session_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling SessionsApi->get_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  |

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

