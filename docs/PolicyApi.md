# whylabs_client.PolicyApi

All URIs are relative to *https://api.whylabsapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_policy**](PolicyApi.md#get_policy) | **GET** /v1/policy | Endpoint to get the policy configuration


# **get_policy**
> str get_policy(dataset_id)

Endpoint to get the policy configuration

Endpoint to get the policy configuration

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import policy_api
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
    api_instance = policy_api.PolicyApi(api_client)
    dataset_id = "model-123" # str | 
    label = "label_example" # str, none_type |  (optional)
    version = 1 # int, none_type |  (optional)
    schema_version = "schema_version_example" # str, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Endpoint to get the policy configuration
        api_response = api_instance.get_policy(dataset_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling PolicyApi->get_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Endpoint to get the policy configuration
        api_response = api_instance.get_policy(dataset_id, label=label, version=version, schema_version=schema_version)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling PolicyApi->get_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  |
 **label** | **str, none_type**|  | [optional]
 **version** | **int, none_type**|  | [optional]
 **schema_version** | **str, none_type**|  | [optional]

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GetPolicy 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

