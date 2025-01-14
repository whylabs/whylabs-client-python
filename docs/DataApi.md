# whylabs_client.DataApi

All URIs are relative to *https://api.whylabsapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analysis_results_data**](DataApi.md#analysis_results_data) | **POST** /v0/organizations/{org_id}/dataset/{dataset_id}/data/analysis-results | Endpoint to query analysis results for a dataset
[**metric_timeseries_data**](DataApi.md#metric_timeseries_data) | **POST** /v0/organizations/{org_id}/dataset/{dataset_id}/data/metric-timeseries | Endpoint to query a single metric timeseries for a dataset


# **analysis_results_data**
> AnalysisResultsResponse analysis_results_data(org_id, dataset_id, analysis_results_request)

Endpoint to query analysis results for a dataset

Returns analysis results for a dataset over a specified interval

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import data_api
from whylabs_client.model.analysis_results_request import AnalysisResultsRequest
from whylabs_client.model.analysis_results_response import AnalysisResultsResponse
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
    api_instance = data_api.DataApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    analysis_results_request = AnalysisResultsRequest(
        interval="2024-01-01T00:00:00Z/2024-01-12T00:00:00Z",
        column_names=[
            "column_names_example",
        ],
        metrics=[
            "metrics_example",
        ],
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
        analyzer_ids=[
            "analyzer_ids_example",
        ],
        analyzer_types=[
            "analyzer_types_example",
        ],
        monitor_ids=[
            "monitor_ids_example",
        ],
        include_unhelpful=True,
        only_anomalies=True,
        include_failures=True,
        offset=1,
        limit=1,
        order=None,
    ) # AnalysisResultsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Endpoint to query analysis results for a dataset
        api_response = api_instance.analysis_results_data(org_id, dataset_id, analysis_results_request)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling DataApi->analysis_results_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **analysis_results_request** | [**AnalysisResultsRequest**](AnalysisResultsRequest.md)|  |

### Return type

[**AnalysisResultsResponse**](AnalysisResultsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AnalysisResultsData 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metric_timeseries_data**
> MetricTimeseriesResponse metric_timeseries_data(org_id, dataset_id, metric_timeseries_request)

Endpoint to query a single metric timeseries for a dataset

Returns a single column or dataset metric over a specified interval

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import data_api
from whylabs_client.model.metric_timeseries_request import MetricTimeseriesRequest
from whylabs_client.model.metric_timeseries_response import MetricTimeseriesResponse
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
    api_instance = data_api.DataApi(api_client)
    org_id = "org-123" # str | 
    dataset_id = "model-123" # str | 
    metric_timeseries_request = MetricTimeseriesRequest(
        interval="2024-01-01T00:00:00Z/2024-01-12T00:00:00Z",
        column="column_example",
        metric="metric_example",
        segment=None,
        analyzer_id="analyzer_id_example",
        monitor_id="monitor_id_example",
        granularity=None,
    ) # MetricTimeseriesRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Endpoint to query a single metric timeseries for a dataset
        api_response = api_instance.metric_timeseries_data(org_id, dataset_id, metric_timeseries_request)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling DataApi->metric_timeseries_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **dataset_id** | **str**|  |
 **metric_timeseries_request** | [**MetricTimeseriesRequest**](MetricTimeseriesRequest.md)|  |

### Return type

[**MetricTimeseriesResponse**](MetricTimeseriesResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MetricTimeseriesData 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

