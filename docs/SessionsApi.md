# whylabs_client.SessionsApi

All URIs are relative to *https://api.whylabsapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_create_reference_profile_upload**](SessionsApi.md#batch_create_reference_profile_upload) | **POST** /v0/sessions/{session_id}/references | Create multiple reference profile uploads for a given session.
[**claim_guest_session**](SessionsApi.md#claim_guest_session) | **POST** /v0/sessions/{session_id}/claim | Claim a guest session, copying its model data into another org and expiring the session.
[**create_dataset_profile_upload**](SessionsApi.md#create_dataset_profile_upload) | **POST** /v0/sessions/{session_id}/upload | Create an upload for a given session.
[**create_reference_profile_upload**](SessionsApi.md#create_reference_profile_upload) | **POST** /v0/sessions/{session_id}/reference | Create a reference profile upload for a given session.
[**create_session**](SessionsApi.md#create_session) | **POST** /v0/sessions | Create a new session that can be used to upload dataset profiles from whylogs for display in whylabs.
[**get_session**](SessionsApi.md#get_session) | **GET** /v0/sessions/{session_id} | Get information about a session.
[**get_session_profile_observatory_link**](SessionsApi.md#get_session_profile_observatory_link) | **POST** /v0/sessions/observatory-link/{session_id} | Get observatory links for profiles in a given session. A max of 3 profiles can be viewed a a time.


# **batch_create_reference_profile_upload**
> BatchLogSessionReferenceResponse batch_create_reference_profile_upload(session_id, batch_log_reference_request)

Create multiple reference profile uploads for a given session.

Create multiple reference profile uploads for a given session.

### Example


```python
import time
import whylabs_client
from whylabs_client.api import sessions_api
from whylabs_client.model.batch_log_session_reference_response import BatchLogSessionReferenceResponse
from whylabs_client.model.batch_log_reference_request import BatchLogReferenceRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.whylabsapp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "https://api.whylabsapp.com"
)


# Enter a context with an instance of the API client
with whylabs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sessions_api.SessionsApi(api_client)
    session_id = "session_id_example" # str | 
    batch_log_reference_request = BatchLogReferenceRequest(
        references=[
            LogReferenceRequest(
                alias="alias_example",
                dataset_timestamp=1,
            ),
        ],
    ) # BatchLogReferenceRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create multiple reference profile uploads for a given session.
        api_response = api_instance.batch_create_reference_profile_upload(session_id, batch_log_reference_request)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling SessionsApi->batch_create_reference_profile_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  |
 **batch_log_reference_request** | [**BatchLogReferenceRequest**](BatchLogReferenceRequest.md)|  |

### Return type

[**BatchLogSessionReferenceResponse**](BatchLogSessionReferenceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | BatchCreateReferenceProfileUpload default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **claim_guest_session**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} claim_guest_session(session_id, org_id)

Claim a guest session, copying its model data into another org and expiring the session.

Claim a guest session, copying its model data into another org and expiring the session.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import sessions_api
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
    api_instance = sessions_api.SessionsApi(api_client)
    session_id = "session_id_example" # str | 
    org_id = "org_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Claim a guest session, copying its model data into another org and expiring the session.
        api_response = api_instance.claim_guest_session(session_id, org_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling SessionsApi->claim_guest_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  |
 **org_id** | **str**|  |

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
**0** | ClaimGuestSession default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dataset_profile_upload**
> CreateDatasetProfileUploadResponse create_dataset_profile_upload(session_id, log_async_request)

Create an upload for a given session.

Create an upload for a given session.

### Example


```python
import time
import whylabs_client
from whylabs_client.api import sessions_api
from whylabs_client.model.log_async_request import LogAsyncRequest
from whylabs_client.model.create_dataset_profile_upload_response import CreateDatasetProfileUploadResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.whylabsapp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "https://api.whylabsapp.com"
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

[**CreateDatasetProfileUploadResponse**](CreateDatasetProfileUploadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CreateDatasetProfileUpload default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_reference_profile_upload**
> LogSessionReferenceResponse create_reference_profile_upload(session_id, log_reference_request)

Create a reference profile upload for a given session.

Create a reference profile upload for a given session.

### Example


```python
import time
import whylabs_client
from whylabs_client.api import sessions_api
from whylabs_client.model.log_reference_request import LogReferenceRequest
from whylabs_client.model.log_session_reference_response import LogSessionReferenceResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.whylabsapp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "https://api.whylabsapp.com"
)


# Enter a context with an instance of the API client
with whylabs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sessions_api.SessionsApi(api_client)
    session_id = "session_id_example" # str | 
    log_reference_request = LogReferenceRequest(
        alias="alias_example",
        dataset_timestamp=1,
    ) # LogReferenceRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a reference profile upload for a given session.
        api_response = api_instance.create_reference_profile_upload(session_id, log_reference_request)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling SessionsApi->create_reference_profile_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  |
 **log_reference_request** | [**LogReferenceRequest**](LogReferenceRequest.md)|  |

### Return type

[**LogSessionReferenceResponse**](LogSessionReferenceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CreateReferenceProfileUpload default response |  -  |

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
# Defining the host is optional and defaults to https://api.whylabsapp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "https://api.whylabsapp.com"
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

# **get_session_profile_observatory_link**
> GetProfileObservatoryLinkResponse get_session_profile_observatory_link(session_id, get_profile_observatory_link_request)

Get observatory links for profiles in a given session. A max of 3 profiles can be viewed a a time.

Get observatory links for profiles in a given session. A max of 3 profiles can be viewed a a time.

### Example


```python
import time
import whylabs_client
from whylabs_client.api import sessions_api
from whylabs_client.model.get_profile_observatory_link_response import GetProfileObservatoryLinkResponse
from whylabs_client.model.get_profile_observatory_link_request import GetProfileObservatoryLinkRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.whylabsapp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(
    host = "https://api.whylabsapp.com"
)


# Enter a context with an instance of the API client
with whylabs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sessions_api.SessionsApi(api_client)
    session_id = "session_id_example" # str | 
    get_profile_observatory_link_request = GetProfileObservatoryLinkRequest(
        batch_profile_timestamps=[
            1,
        ],
        reference_profile_ids=[
            "reference_profile_ids_example",
        ],
    ) # GetProfileObservatoryLinkRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get observatory links for profiles in a given session. A max of 3 profiles can be viewed a a time.
        api_response = api_instance.get_session_profile_observatory_link(session_id, get_profile_observatory_link_request)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling SessionsApi->get_session_profile_observatory_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  |
 **get_profile_observatory_link_request** | [**GetProfileObservatoryLinkRequest**](GetProfileObservatoryLinkRequest.md)|  |

### Return type

[**GetProfileObservatoryLinkResponse**](GetProfileObservatoryLinkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GetSessionProfileObservatoryLink default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

