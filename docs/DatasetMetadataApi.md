# whylabs_client.DatasetMetadataApi

All URIs are relative to *https://api.whylabsapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_dataset_metadata**](DatasetMetadataApi.md#delete_dataset_metadata) | **DELETE** /v0/organizations/{org_id}/dataset/{dataset_id}/metadata | Delete dataset metadata for the specified dataset
[**get_dataset_metadata**](DatasetMetadataApi.md#get_dataset_metadata) | **GET** /v0/organizations/{org_id}/dataset/{dataset_id}/metadata | Get dataset metadata for the specified dataset
[**put_dataset_metadata**](DatasetMetadataApi.md#put_dataset_metadata) | **PUT** /v0/organizations/{org_id}/dataset/{dataset_id}/metadata | Put dataset metadata for the specified dataset


# **delete_dataset_metadata**
> Response delete_dataset_metadata(org_id, dataset_id)

Delete dataset metadata for the specified dataset

Delete dataset metadata for the specified dataset

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import dataset_metadata_api
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
    api_instance = dataset_metadata_api.DatasetMetadataApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete dataset metadata for the specified dataset
        api_response = api_instance.delete_dataset_metadata(org_id, dataset_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling DatasetMetadataApi->delete_dataset_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |

### Return type

[**Response**](Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DeleteDatasetMetadata default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_metadata**
> GetDatasetMetadataResponse get_dataset_metadata(org_id, dataset_id)

Get dataset metadata for the specified dataset

Get dataset metadata for the specified dataset

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import dataset_metadata_api
from whylabs_client.model.get_dataset_metadata_response import GetDatasetMetadataResponse
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
    api_instance = dataset_metadata_api.DatasetMetadataApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get dataset metadata for the specified dataset
        api_response = api_instance.get_dataset_metadata(org_id, dataset_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling DatasetMetadataApi->get_dataset_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |

### Return type

[**GetDatasetMetadataResponse**](GetDatasetMetadataResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GetDatasetMetadata default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_dataset_metadata**
> Response put_dataset_metadata(org_id, dataset_id, body)

Put dataset metadata for the specified dataset

Put dataset metadata for the specified dataset

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import dataset_metadata_api
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
    api_instance = dataset_metadata_api.DatasetMetadataApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    body = "body_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Put dataset metadata for the specified dataset
        api_response = api_instance.put_dataset_metadata(org_id, dataset_id, body)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling DatasetMetadataApi->put_dataset_metadata: %s\n" % e)
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
**0** | PutDatasetMetadata default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

