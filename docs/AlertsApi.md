# whylabs_client.AlertsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_alerts_paths**](AlertsApi.md#get_alerts_paths) | **GET** /v0/organizations/{org_id}/alerts/models/{model_id}/paths | Get the alerts for a given time period.


# **get_alerts_paths**
> GetAlertsPathsResponse get_alerts_paths(org_id, model_id, start_timestamp, end_timestamp)

Get the alerts for a given time period.

Get the alerts from a given time period.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import alerts_api
from whylabs_client.model.get_alerts_paths_response import GetAlertsPathsResponse
from whylabs_client.model.segment_tag import SegmentTag
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
    api_instance = alerts_api.AlertsApi(api_client)
    org_id = "org-123" # str | Your company's unique organization ID
    model_id = "model-123" # str | The unique model ID in your company. The model is created if it doesn't exist already.
    start_timestamp = 1577836800000 # int | Start time exclusive
    end_timestamp = 1893456000000 # int | 
    segment_tags = [
        SegmentTag(
            key="key_example",
            value="value_example",
        ),
    ] # [SegmentTag], none_type | List of (key, value) pair tags for a segment. Must not contain duplicate values (optional)
    version = "" # str, none_type | the version of the alert in case we have multiple schemas (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the alerts for a given time period.
        api_response = api_instance.get_alerts_paths(org_id, model_id, start_timestamp, end_timestamp)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling AlertsApi->get_alerts_paths: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the alerts for a given time period.
        api_response = api_instance.get_alerts_paths(org_id, model_id, start_timestamp, end_timestamp, segment_tags=segment_tags, version=version)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling AlertsApi->get_alerts_paths: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Your company&#39;s unique organization ID |
 **model_id** | **str**| The unique model ID in your company. The model is created if it doesn&#39;t exist already. |
 **start_timestamp** | **int**| Start time exclusive |
 **end_timestamp** | **int**|  |
 **segment_tags** | [**[SegmentTag], none_type**](SegmentTag.md)| List of (key, value) pair tags for a segment. Must not contain duplicate values | [optional]
 **version** | **str, none_type**| the version of the alert in case we have multiple schemas | [optional]

### Return type

[**GetAlertsPathsResponse**](GetAlertsPathsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | a list of AlertsPath in the given time period, de-duped with the latest updated entries |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

