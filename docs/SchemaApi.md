# whylabs_client.SchemaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_monitor_config_schema**](SchemaApi.md#get_monitor_config_schema) | **GET** /v0/organizations/{org_id}/schema/monitor-config | Get the current supported schema of the monitor configuration


# **get_monitor_config_schema**
> str get_monitor_config_schema(org_id)

Get the current supported schema of the monitor configuration

Get the current supported schema of the  monitor configuration

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import schema_api
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
    api_instance = schema_api.SchemaApi(api_client)
    org_id = "org-123" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get the current supported schema of the monitor configuration
        api_response = api_instance.get_monitor_config_schema(org_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling SchemaApi->get_monitor_config_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GetMonitorConfigSchema default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

