# whylabs_client.TracesApi

All URIs are relative to *https://api.whylabsapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_traces**](TracesApi.md#export_traces) | **POST** /v1/traces | Export traces into WhyLabs


# **export_traces**
> ExportTraceServiceResponse export_traces(request_body)

Export traces into WhyLabs

API to export traces into WhyLabs

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import traces_api
from whylabs_client.model.export_trace_service_response import ExportTraceServiceResponse
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
    api_instance = traces_api.TracesApi(api_client)
    request_body = [
        'YQ==',
    ] # [str] | 
    x_whylabs_resource = "resource-1" # str, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export traces into WhyLabs
        api_response = api_instance.export_traces(request_body)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling TracesApi->export_traces: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export traces into WhyLabs
        api_response = api_instance.export_traces(request_body, x_whylabs_resource=x_whylabs_resource)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling TracesApi->export_traces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **[str]**|  |
 **x_whylabs_resource** | **str, none_type**|  | [optional]

### Return type

[**ExportTraceServiceResponse**](ExportTraceServiceResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-protobuf
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ExportTraces 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

