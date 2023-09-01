# whylabs_client.DebugEventsApi

All URIs are relative to *https://api.whylabsapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**log_debug_event**](DebugEventsApi.md#log_debug_event) | **POST** /v0/organizations/{org_id}/debug-events/resources/{dataset_id}/debug-events/log | Log a debug event


# **log_debug_event**
> str log_debug_event(org_id, dataset_id, debug_event)

Log a debug event

Create a debug event.         

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import debug_events_api
from whylabs_client.model.debug_event import DebugEvent
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
    api_instance = debug_events_api.DebugEventsApi(api_client)
    org_id = "org-123" # str | Your company's unique organization ID
    dataset_id = "model-123" # str | The resource ID to log the event to
    debug_event = DebugEvent(
        trace_id="trace_id_example",
        segment=Segment(
            tags=[
                SegmentTag(
                    key="key_example",
                    value="value_example",
                ),
            ],
        ),
        tags=[
            "tags_example",
        ],
        content="content_example",
        dataset_timestamp=1,
        creation_timestamp=1,
    ) # DebugEvent | 

    # example passing only required values which don't have defaults set
    try:
        # Log a debug event
        api_response = api_instance.log_debug_event(org_id, dataset_id, debug_event)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling DebugEventsApi->log_debug_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Your company&#39;s unique organization ID |
 **dataset_id** | **str**| The resource ID to log the event to |
 **debug_event** | [**DebugEvent**](DebugEvent.md)|  |

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | 202 if the response is accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

