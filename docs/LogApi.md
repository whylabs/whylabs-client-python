# whylabs_client.LogApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**log_async**](LogApi.md#log_async) | **POST** /v0/organizations/{org_id}/log/async/{dataset_id} | Like /log, except this api doesn&#39;t take the actual profile content. It returns an upload link that can be used to upload the profile to.
[**log_reference**](LogApi.md#log_reference) | **POST** /v0/organizations/{org_id}/log/reference/{model_id} | Returns a presigned URL for uploading the reference profile to.


# **log_async**
> AsyncLogResponse log_async(org_id, dataset_id, log_async_request)

Like /log, except this api doesn't take the actual profile content. It returns an upload link that can be used to upload the profile to.

Like /log, except this api doesn't take the actual profile content. It returns an upload link that can be used to upload the profile to.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import log_api
from whylabs_client.model.log_async_request import LogAsyncRequest
from whylabs_client.model.async_log_response import AsyncLogResponse
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
    api_instance = log_api.LogApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
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
        # Like /log, except this api doesn't take the actual profile content. It returns an upload link that can be used to upload the profile to.
        api_response = api_instance.log_async(org_id, dataset_id, log_async_request)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling LogApi->log_async: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **log_async_request** | [**LogAsyncRequest**](LogAsyncRequest.md)|  |

### Return type

[**AsyncLogResponse**](AsyncLogResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | LogAsync default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_reference**
> LogReferenceResponse log_reference(org_id, model_id, log_reference_request)

Returns a presigned URL for uploading the reference profile to.

Reference profiles can be used for.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import log_api
from whylabs_client.model.log_reference_response import LogReferenceResponse
from whylabs_client.model.log_reference_request import LogReferenceRequest
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
    api_instance = log_api.LogApi(api_client)
    org_id = "org-123" # str | 
    model_id = "model-123" # str | 
    log_reference_request = LogReferenceRequest(
        alias="alias_example",
        dataset_timestamp=1,
    ) # LogReferenceRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a presigned URL for uploading the reference profile to.
        api_response = api_instance.log_reference(org_id, model_id, log_reference_request)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling LogApi->log_reference: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **model_id** | **str**|  |
 **log_reference_request** | [**LogReferenceRequest**](LogReferenceRequest.md)|  |

### Return type

[**LogReferenceResponse**](LogReferenceResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | LogReference default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

