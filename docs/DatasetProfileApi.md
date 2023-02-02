# whylabs_client.DatasetProfileApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_analyzer_results**](DatasetProfileApi.md#delete_analyzer_results) | **DELETE** /v0/organizations/{org_id}/dataset-profiles/models/{dataset_id}/analyzer-results | Deletes a set of analyzer results
[**delete_dataset_profiles**](DatasetProfileApi.md#delete_dataset_profiles) | **DELETE** /v0/organizations/{org_id}/dataset-profiles/models/{dataset_id} | Deletes a set of dataset profiles


# **delete_analyzer_results**
> DeleteAnalyzerResultsResponse delete_analyzer_results(org_id, dataset_id)

Deletes a set of analyzer results

Deletes a set of analyzer results. Returns false if scheduling deletion encountered some error.          

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import dataset_profile_api
from whylabs_client.model.delete_analyzer_results_response import DeleteAnalyzerResultsResponse
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
    api_instance = dataset_profile_api.DatasetProfileApi(api_client)
    org_id = "org-123" # str | Your company's unique organization ID
    dataset_id = "model-123" # str | The unique dataset ID in your company.
    start_timestamp = 1577836800000 # int, none_type | Optional, scope deleting analyzer results more recent than the timestamp (optional)
    end_timestamp = 1893456000000 # int, none_type | Optional, scope deleting analyzer results older than the timestamp (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deletes a set of analyzer results
        api_response = api_instance.delete_analyzer_results(org_id, dataset_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling DatasetProfileApi->delete_analyzer_results: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletes a set of analyzer results
        api_response = api_instance.delete_analyzer_results(org_id, dataset_id, start_timestamp=start_timestamp, end_timestamp=end_timestamp)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling DatasetProfileApi->delete_analyzer_results: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Your company&#39;s unique organization ID |
 **dataset_id** | **str**| The unique dataset ID in your company. |
 **start_timestamp** | **int, none_type**| Optional, scope deleting analyzer results more recent than the timestamp | [optional]
 **end_timestamp** | **int, none_type**| Optional, scope deleting analyzer results older than the timestamp | [optional]

### Return type

[**DeleteAnalyzerResultsResponse**](DeleteAnalyzerResultsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The [DeleteAnalyzerResultsResponse] if operation succeeds |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dataset_profiles**
> DeleteDatasetProfilesResponse delete_dataset_profiles(org_id, dataset_id)

Deletes a set of dataset profiles

Deletes a set of dataset profiles. Returns false if scheduling deletion encountered some error.          

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import dataset_profile_api
from whylabs_client.model.delete_dataset_profiles_response import DeleteDatasetProfilesResponse
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
    api_instance = dataset_profile_api.DatasetProfileApi(api_client)
    org_id = "org-123" # str | Your company's unique organization ID
    dataset_id = "model-123" # str | The unique dataset ID in your company.
    profile_start_timestamp = 1577836800000 # int, none_type | Optional, scope deleting profiles more recently than the timestamp (optional)
    profile_end_timestamp = 1893456000000 # int, none_type | Optional, scope deleting profiles older than the timestamp (optional)
    before_upload_timestamp = 1577836800000 # int, none_type | Optional, scope deleting profiles uploaded prior to the timestamp (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deletes a set of dataset profiles
        api_response = api_instance.delete_dataset_profiles(org_id, dataset_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling DatasetProfileApi->delete_dataset_profiles: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletes a set of dataset profiles
        api_response = api_instance.delete_dataset_profiles(org_id, dataset_id, profile_start_timestamp=profile_start_timestamp, profile_end_timestamp=profile_end_timestamp, before_upload_timestamp=before_upload_timestamp)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling DatasetProfileApi->delete_dataset_profiles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Your company&#39;s unique organization ID |
 **dataset_id** | **str**| The unique dataset ID in your company. |
 **profile_start_timestamp** | **int, none_type**| Optional, scope deleting profiles more recently than the timestamp | [optional]
 **profile_end_timestamp** | **int, none_type**| Optional, scope deleting profiles older than the timestamp | [optional]
 **before_upload_timestamp** | **int, none_type**| Optional, scope deleting profiles uploaded prior to the timestamp | [optional]

### Return type

[**DeleteDatasetProfilesResponse**](DeleteDatasetProfilesResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The [DeleteDatasetProfilesResponse] if operation succeeds |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

