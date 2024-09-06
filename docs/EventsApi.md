# whylabs_client.EventsApi

All URIs are relative to *https://api.whylabsapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_events**](EventsApi.md#get_events) | **GET** /v1/events | Endpoint to get all events
[**save_event**](EventsApi.md#save_event) | **POST** /v1/events | Endpoint to save an event


# **get_events**
> GetEventsResponse get_events(org_id, dataset_id)

Endpoint to get all events

Endpoint to get all events

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import events_api
from whylabs_client.model.get_events_response import GetEventsResponse
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
    api_instance = events_api.EventsApi(api_client)
    org_id = "org_id_example" # str | 
    dataset_id = "dataset_id_example" # str | 
    start_date = 1 # int, none_type |  (optional)
    end_date = 1 # int, none_type |  (optional)
    limit = 1 # int, none_type |  (optional)
    offset = 1 # int, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Endpoint to get all events
        api_response = api_instance.get_events(org_id, dataset_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling EventsApi->get_events: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Endpoint to get all events
        api_response = api_instance.get_events(org_id, dataset_id, start_date=start_date, end_date=end_date, limit=limit, offset=offset)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling EventsApi->get_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **start_date** | **int, none_type**|  | [optional]
 **end_date** | **int, none_type**|  | [optional]
 **limit** | **int, none_type**|  | [optional]
 **offset** | **int, none_type**|  | [optional]

### Return type

[**GetEventsResponse**](GetEventsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GetEvents 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_event**
> save_event(org_id, dataset_id, customer_event)

Endpoint to save an event

Endpoint to save an event

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import events_api
from whylabs_client.model.customer_event import CustomerEvent
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
    api_instance = events_api.EventsApi(api_client)
    org_id = "org_id_example" # str | 
    dataset_id = "dataset_id_example" # str | 
    customer_event = CustomerEvent(
        user_id="user_id_example",
        event_type="event_type_example",
        event_timestamp=1,
        description="description_example",
    ) # CustomerEvent | 

    # example passing only required values which don't have defaults set
    try:
        # Endpoint to save an event
        api_instance.save_event(org_id, dataset_id, customer_event)
    except whylabs_client.ApiException as e:
        print("Exception when calling EventsApi->save_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **customer_event** | [**CustomerEvent**](CustomerEvent.md)|  |

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SaveEvent 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

