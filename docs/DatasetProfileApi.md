# whylabs_client.DatasetProfileApi

All URIs are relative to *https://api.whylabsapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_reference_profile**](DatasetProfileApi.md#create_reference_profile) | **POST** /v0/organizations/{org_id}/dataset-profiles/models/{dataset_id}/reference-profile | Returns data needed to uploading the reference profile
[**delete_analyzer_results**](DatasetProfileApi.md#delete_analyzer_results) | **DELETE** /v0/organizations/{org_id}/dataset-profiles/models/{dataset_id}/analyzer-results | Deletes a set of analyzer results
[**delete_dataset_profiles**](DatasetProfileApi.md#delete_dataset_profiles) | **DELETE** /v0/organizations/{org_id}/dataset-profiles/models/{dataset_id} | Deletes a set of dataset profiles
[**delete_reference_profile**](DatasetProfileApi.md#delete_reference_profile) | **DELETE** /v0/organizations/{org_id}/dataset-profiles/models/{model_id}/reference-profiles/{reference_id} | Delete a single reference profile
[**get_profile_traces**](DatasetProfileApi.md#get_profile_traces) | **GET** /v0/organizations/{org_id}/dataset-profiles/models/{dataset_id}/trace/{trace_id} | Returns a list for profile traces matching a trace id
[**get_reference_profile**](DatasetProfileApi.md#get_reference_profile) | **GET** /v0/organizations/{org_id}/dataset-profiles/models/{model_id}/reference-profiles/{reference_id} | Returns a single reference profile
[**list_delete_analyzer_results_requests**](DatasetProfileApi.md#list_delete_analyzer_results_requests) | **GET** /v0/organizations/{org_id}/dataset-profiles/delete-requests/analyzer-results | List requests to delete analyzer results
[**list_delete_dataset_profiles_requests**](DatasetProfileApi.md#list_delete_dataset_profiles_requests) | **GET** /v0/organizations/{org_id}/dataset-profiles/delete-requests/dataset-profiles | List requests to delete dataset profiles
[**list_profile_traces**](DatasetProfileApi.md#list_profile_traces) | **GET** /v0/organizations/{org_id}/dataset-profiles/models/{dataset_id}/trace | Returns a list for profile traces
[**list_reference_profiles**](DatasetProfileApi.md#list_reference_profiles) | **GET** /v0/organizations/{org_id}/dataset-profiles/models/{model_id}/reference-profiles | Returns a list for reference profiles between the given time range filtered on the upload timestamp
[**list_segments**](DatasetProfileApi.md#list_segments) | **GET** /v0/organizations/{org_id}/dataset-profiles/models/{model_id}/segments | Returns a list of segments


# **create_reference_profile**
> CreateReferenceProfileResponse create_reference_profile(org_id, dataset_id, create_reference_profile_request)

Returns data needed to uploading the reference profile

Returns data needed to upload the reference profile. Supports uploading segmented reference profiles.              If segments are omitted, provides data needed to upload a single reference profile.              This replaces the deprecated LogReference operation.         

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import dataset_profile_api
from whylabs_client.model.create_reference_profile_request import CreateReferenceProfileRequest
from whylabs_client.model.create_reference_profile_response import CreateReferenceProfileResponse
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
    api_instance = dataset_profile_api.DatasetProfileApi(api_client)
    org_id = "org-123" # str | Your company's unique organization ID
    dataset_id = "model-123" # str | The unique model ID in your company.
    create_reference_profile_request = CreateReferenceProfileRequest(
        alias="alias_example",
        version="version_example",
        dataset_timestamp=1,
        segments=[
            Segment(
                tags=[
                    SegmentTag(
                        key="key_example",
                        value="value_example",
                    ),
                ],
            ),
        ],
        tags=[
            "tags_example",
        ],
        region="region_example",
    ) # CreateReferenceProfileRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Returns data needed to uploading the reference profile
        api_response = api_instance.create_reference_profile(org_id, dataset_id, create_reference_profile_request)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling DatasetProfileApi->create_reference_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Your company&#39;s unique organization ID |
 **dataset_id** | **str**| The unique model ID in your company. |
 **create_reference_profile_request** | [**CreateReferenceProfileRequest**](CreateReferenceProfileRequest.md)|  |

### Return type

[**CreateReferenceProfileResponse**](CreateReferenceProfileResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The metadata for the summarized reference profile data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
    api_instance = dataset_profile_api.DatasetProfileApi(api_client)
    org_id = "org-123" # str | Your company's unique organization ID
    dataset_id = "model-123" # str | The unique dataset ID in your company.
    analyzer_id = "drift-analyzer" # str, none_type |  (optional)
    start_timestamp = 1577836800000 # int, none_type |  (optional)
    end_timestamp = 1893456000000 # int, none_type |  (optional)

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
        api_response = api_instance.delete_analyzer_results(org_id, dataset_id, analyzer_id=analyzer_id, start_timestamp=start_timestamp, end_timestamp=end_timestamp)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling DatasetProfileApi->delete_analyzer_results: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Your company&#39;s unique organization ID |
 **dataset_id** | **str**| The unique dataset ID in your company. |
 **analyzer_id** | **str, none_type**|  | [optional]
 **start_timestamp** | **int, none_type**|  | [optional]
 **end_timestamp** | **int, none_type**|  | [optional]

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
**200** | The \\[DeleteAnalyzerResultsResponse\\] if operation succeeds |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dataset_profiles**
> DeleteDatasetProfilesResponse delete_dataset_profiles(org_id, dataset_id)

Deletes a set of dataset profiles

Deletes a set of dataset profiles. Returns false if scheduling deletion encountered some error.         Optionally deletes analyzer results for the same time range.          

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import dataset_profile_api
from whylabs_client.model.delete_dataset_profiles_response import DeleteDatasetProfilesResponse
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
    api_instance = dataset_profile_api.DatasetProfileApi(api_client)
    org_id = "org-123" # str | Your company's unique organization ID
    dataset_id = "model-123" # str | The unique dataset ID in your company.
    profile_start_timestamp = 1577836800000 # int, none_type | Optional, scope deleting profiles from and more recent than the timestamp (optional)
    profile_end_timestamp = 1893456000000 # int, none_type | Optional, scope deleting profiles older than the timestamp (optional)
    before_upload_timestamp = 1577836800000 # int, none_type | Optional, scope deleting profiles uploaded prior to the timestamp (optional)
    delete_analyzer_results = True # bool, none_type |  (optional)

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
        api_response = api_instance.delete_dataset_profiles(org_id, dataset_id, profile_start_timestamp=profile_start_timestamp, profile_end_timestamp=profile_end_timestamp, before_upload_timestamp=before_upload_timestamp, delete_analyzer_results=delete_analyzer_results)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling DatasetProfileApi->delete_dataset_profiles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Your company&#39;s unique organization ID |
 **dataset_id** | **str**| The unique dataset ID in your company. |
 **profile_start_timestamp** | **int, none_type**| Optional, scope deleting profiles from and more recent than the timestamp | [optional]
 **profile_end_timestamp** | **int, none_type**| Optional, scope deleting profiles older than the timestamp | [optional]
 **before_upload_timestamp** | **int, none_type**| Optional, scope deleting profiles uploaded prior to the timestamp | [optional]
 **delete_analyzer_results** | **bool, none_type**|  | [optional]

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
**200** | The \\[DeleteDatasetProfilesResponse\\] if operation succeeds |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reference_profile**
> bool delete_reference_profile(org_id, model_id, reference_id)

Delete a single reference profile

Delete a a Reference Profile. Returns false if the deletion encountered some error.          

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import dataset_profile_api
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
    api_instance = dataset_profile_api.DatasetProfileApi(api_client)
    org_id = "org-123" # str | Your company's unique organization ID
    model_id = "model-123" # str | The unique model ID in your company.
    reference_id = "ref-xxy" # str | Unique reference Id.

    # example passing only required values which don't have defaults set
    try:
        # Delete a single reference profile
        api_response = api_instance.delete_reference_profile(org_id, model_id, reference_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling DatasetProfileApi->delete_reference_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Your company&#39;s unique organization ID |
 **model_id** | **str**| The unique model ID in your company. |
 **reference_id** | **str**| Unique reference Id. |

### Return type

**bool**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | true if successful, false if we encounter failures |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile_traces**
> ProfileTracesResponse get_profile_traces(org_id, dataset_id, trace_id)

Returns a list for profile traces matching a trace id

Returns a list of profile traces matching a trace id          

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import dataset_profile_api
from whylabs_client.model.profile_traces_response import ProfileTracesResponse
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
    api_instance = dataset_profile_api.DatasetProfileApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    trace_id = "a756f8bb-de30-48a2-be41-178ae6af7100" # str | 
    limit = 50 # int, none_type |  (optional)
    offset = 0 # int, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list for profile traces matching a trace id
        api_response = api_instance.get_profile_traces(org_id, dataset_id, trace_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling DatasetProfileApi->get_profile_traces: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list for profile traces matching a trace id
        api_response = api_instance.get_profile_traces(org_id, dataset_id, trace_id, limit=limit, offset=offset)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling DatasetProfileApi->get_profile_traces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **trace_id** | **str**|  |
 **limit** | **int, none_type**|  | [optional]
 **offset** | **int, none_type**|  | [optional]

### Return type

[**ProfileTracesResponse**](ProfileTracesResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GetProfileTraces 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reference_profile**
> ReferenceProfileItemResponse get_reference_profile(org_id, model_id, reference_id)

Returns a single reference profile

Returns a Reference Profile.          

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import dataset_profile_api
from whylabs_client.model.reference_profile_item_response import ReferenceProfileItemResponse
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
    api_instance = dataset_profile_api.DatasetProfileApi(api_client)
    org_id = "org-123" # str | Your company's unique organization ID
    model_id = "model-123" # str | The unique model ID in your company.
    reference_id = "ref-xxy" # str | Unique reference Id.

    # example passing only required values which don't have defaults set
    try:
        # Returns a single reference profile
        api_response = api_instance.get_reference_profile(org_id, model_id, reference_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling DatasetProfileApi->get_reference_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Your company&#39;s unique organization ID |
 **model_id** | **str**| The unique model ID in your company. |
 **reference_id** | **str**| Unique reference Id. |

### Return type

[**ReferenceProfileItemResponse**](ReferenceProfileItemResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The metadata for the summarized dataset profile including paths to JSON and protobuf data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_delete_analyzer_results_requests**
> [DeleteAnalyzerResult] list_delete_analyzer_results_requests(org_id)

List requests to delete analyzer results

List the requests to delete analyzer results.          

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import dataset_profile_api
from whylabs_client.model.delete_analyzer_result import DeleteAnalyzerResult
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
    api_instance = dataset_profile_api.DatasetProfileApi(api_client)
    org_id = "org-123" # str | Your company's unique organization ID

    # example passing only required values which don't have defaults set
    try:
        # List requests to delete analyzer results
        api_response = api_instance.list_delete_analyzer_results_requests(org_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling DatasetProfileApi->list_delete_analyzer_results_requests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Your company&#39;s unique organization ID |

### Return type

[**[DeleteAnalyzerResult]**](DeleteAnalyzerResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of \\[DeleteAnalyzerResult\\] requests if operation succeeds |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_delete_dataset_profiles_requests**
> [DeleteProfile] list_delete_dataset_profiles_requests(org_id)

List requests to delete dataset profiles

List the requests to delete dataset profiles.          

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import dataset_profile_api
from whylabs_client.model.delete_profile import DeleteProfile
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
    api_instance = dataset_profile_api.DatasetProfileApi(api_client)
    org_id = "org-123" # str | Your company's unique organization ID

    # example passing only required values which don't have defaults set
    try:
        # List requests to delete dataset profiles
        api_response = api_instance.list_delete_dataset_profiles_requests(org_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling DatasetProfileApi->list_delete_dataset_profiles_requests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Your company&#39;s unique organization ID |

### Return type

[**[DeleteProfile]**](DeleteProfile.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of \\[DeleteProfile\\] requests if operation succeeds |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_profile_traces**
> ProfileTracesResponse list_profile_traces(org_id, dataset_id, from_epoch, to_epoch)

Returns a list for profile traces

Returns a list of profile traces.          

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import dataset_profile_api
from whylabs_client.model.segment_tag import SegmentTag
from whylabs_client.model.profile_traces_response import ProfileTracesResponse
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
    api_instance = dataset_profile_api.DatasetProfileApi(api_client)
    org_id = "org-123" # str | Your company's unique organization ID
    dataset_id = "model-123" # str | The unique dataset ID
    from_epoch = 1577836800000 # int | Milli epoch time that represents the end of the time range to query.
    to_epoch = 1893456000000 # int | Milli epoch time that represents the end of the time range to query.
    segment = [
        SegmentTag(
            key="key_example",
            value="value_example",
        ),
    ] # [SegmentTag], none_type |  (optional)
    limit = 50 # int, none_type |  (optional)
    offset = 0 # int, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list for profile traces
        api_response = api_instance.list_profile_traces(org_id, dataset_id, from_epoch, to_epoch)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling DatasetProfileApi->list_profile_traces: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list for profile traces
        api_response = api_instance.list_profile_traces(org_id, dataset_id, from_epoch, to_epoch, segment=segment, limit=limit, offset=offset)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling DatasetProfileApi->list_profile_traces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Your company&#39;s unique organization ID |
 **dataset_id** | **str**| The unique dataset ID |
 **from_epoch** | **int**| Milli epoch time that represents the end of the time range to query. |
 **to_epoch** | **int**| Milli epoch time that represents the end of the time range to query. |
 **segment** | [**[SegmentTag], none_type**](SegmentTag.md)|  | [optional]
 **limit** | **int, none_type**|  | [optional]
 **offset** | **int, none_type**|  | [optional]

### Return type

[**ProfileTracesResponse**](ProfileTracesResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The metadata for the summarized dataset profile including paths to JSON and protobuf data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_reference_profiles**
> [ReferenceProfileItemResponse] list_reference_profiles(org_id, model_id)

Returns a list for reference profiles between the given time range filtered on the upload timestamp

Returns a list of Reference Profiles between a given time range filtered on the upload timestamp.          

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import dataset_profile_api
from whylabs_client.model.reference_profile_item_response import ReferenceProfileItemResponse
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
    api_instance = dataset_profile_api.DatasetProfileApi(api_client)
    org_id = "org-123" # str | Your company's unique organization ID
    model_id = "model-123" # str | The unique model ID in your company.
    from_epoch = 1577836800000 # int, none_type | Milli epoch time that represents the end of the time range to query based on the upload timestamp. (optional)
    to_epoch = 1893456000000 # int, none_type | Milli epoch time that represents the end of the time range to query based on the upload timestamp. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list for reference profiles between the given time range filtered on the upload timestamp
        api_response = api_instance.list_reference_profiles(org_id, model_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling DatasetProfileApi->list_reference_profiles: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list for reference profiles between the given time range filtered on the upload timestamp
        api_response = api_instance.list_reference_profiles(org_id, model_id, from_epoch=from_epoch, to_epoch=to_epoch)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling DatasetProfileApi->list_reference_profiles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Your company&#39;s unique organization ID |
 **model_id** | **str**| The unique model ID in your company. |
 **from_epoch** | **int, none_type**| Milli epoch time that represents the end of the time range to query based on the upload timestamp. | [optional]
 **to_epoch** | **int, none_type**| Milli epoch time that represents the end of the time range to query based on the upload timestamp. | [optional]

### Return type

[**[ReferenceProfileItemResponse]**](ReferenceProfileItemResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The metadata for the summarized dataset profile including paths to JSON and protobuf data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_segments**
> SegmentListResponse list_segments(org_id, model_id)

Returns a list of segments

Returns a list of segments for the dataset.          

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import dataset_profile_api
from whylabs_client.model.segment_list_response import SegmentListResponse
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
    api_instance = dataset_profile_api.DatasetProfileApi(api_client)
    org_id = "org-123" # str | Your company's unique organization ID
    model_id = "model-123" # str | The unique model ID in your company.

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of segments
        api_response = api_instance.list_segments(org_id, model_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling DatasetProfileApi->list_segments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Your company&#39;s unique organization ID |
 **model_id** | **str**| The unique model ID in your company. |

### Return type

[**SegmentListResponse**](SegmentListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of segments for the dataset profile |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

