# whylabs_client.EventsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_events_data**](EventsApi.md#get_events_data) | **GET** /v0/organizations/{org_id}/events/models/{model_id}/data | Get the event data as multi-line JSON for a given time period.


# **get_events_data**
> file_type get_events_data(org_id, model_id, start_timestamp, end_timestamp)

Get the event data as multi-line JSON for a given time period.

Get the events from a given time period.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import events_api
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
    api_instance = events_api.EventsApi(api_client)
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
    version = "" # str, none_type | the version of the event (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the event data as multi-line JSON for a given time period.
        api_response = api_instance.get_events_data(org_id, model_id, start_timestamp, end_timestamp)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling EventsApi->get_events_data: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the event data as multi-line JSON for a given time period.
        api_response = api_instance.get_events_data(org_id, model_id, start_timestamp, end_timestamp, segment_tags=segment_tags, version=version)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling EventsApi->get_events_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Your company&#39;s unique organization ID |
 **model_id** | **str**| The unique model ID in your company. The model is created if it doesn&#39;t exist already. |
 **start_timestamp** | **int**| Start time exclusive |
 **end_timestamp** | **int**|  |
 **segment_tags** | [**[SegmentTag], none_type**](SegmentTag.md)| List of (key, value) pair tags for a segment. Must not contain duplicate values | [optional]
 **version** | **str, none_type**| the version of the event | [optional]

### Return type

**file_type**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-json-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A streaming JSON output in multiline JSON format |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

