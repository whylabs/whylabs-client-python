# whylabs_client.DiagnosticsApi

All URIs are relative to *https://api.whylabsapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_diagnostics**](DiagnosticsApi.md#send_diagnostics) | **POST** /v1/diagnostics/{type} | Send diagnostics data


# **send_diagnostics**
> Response send_diagnostics(type, body)

Send diagnostics data

Endpoint to store diagnostics data

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import diagnostics_api
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
    api_instance = diagnostics_api.DiagnosticsApi(api_client)
    type = "type_example" # str | 
    body = "body_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Send diagnostics data
        api_response = api_instance.send_diagnostics(type, body)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling DiagnosticsApi->send_diagnostics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  |
 **body** | **str**|  |

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
**200** | SendDiagnostics 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

