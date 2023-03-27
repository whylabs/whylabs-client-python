# whylabs_client.FeatureWeightsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_column_weights**](FeatureWeightsApi.md#get_column_weights) | **GET** /v0/organizations/{org_id}/dataset/{dataset_id}/weights | Get column weights for the specified dataset
[**put_column_weights**](FeatureWeightsApi.md#put_column_weights) | **PUT** /v0/organizations/{org_id}/dataset/{dataset_id}/weights | Put column weights for the specified dataset


# **get_column_weights**
> EntityWeightRecord get_column_weights(org_id, dataset_id)

Get column weights for the specified dataset

Get column weights for the specified dataset

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import feature_weights_api
from whylabs_client.model.entity_weight_record import EntityWeightRecord
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
    api_instance = feature_weights_api.FeatureWeightsApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get column weights for the specified dataset
        api_response = api_instance.get_column_weights(org_id, dataset_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling FeatureWeightsApi->get_column_weights: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |

### Return type

[**EntityWeightRecord**](EntityWeightRecord.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GetColumnWeights default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_column_weights**
> Response put_column_weights(org_id, dataset_id, body)

Put column weights for the specified dataset

Put column weights for the specified dataset

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import feature_weights_api
from whylabs_client.model.response import Response
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
    api_instance = feature_weights_api.FeatureWeightsApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    body = "body_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Put column weights for the specified dataset
        api_response = api_instance.put_column_weights(org_id, dataset_id, body)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling FeatureWeightsApi->put_column_weights: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
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
**0** | PutColumnWeights default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

