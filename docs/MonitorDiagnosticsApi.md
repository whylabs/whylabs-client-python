# whylabs_client.MonitorDiagnosticsApi

All URIs are relative to *https://api.whylabsapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**detect_noisy_analyzers**](MonitorDiagnosticsApi.md#detect_noisy_analyzers) | **POST** /v0/organizations/{org_id}/diagnostics/monitor/analyzers | Endpoint to detect noisy or failing analyzers
[**detect_noisy_columns**](MonitorDiagnosticsApi.md#detect_noisy_columns) | **POST** /v0/organizations/{org_id}/diagnostics/monitor/analyzer/segment/columns | Endpoint to detect the noisiest columns for a specific analyzer and segment
[**detect_noisy_segments**](MonitorDiagnosticsApi.md#detect_noisy_segments) | **POST** /v0/organizations/{org_id}/diagnostics/monitor/analyzer/segments | Endpoint to detect the noisiest segments for a specific analyzer
[**diagnose_analyzer_sync**](MonitorDiagnosticsApi.md#diagnose_analyzer_sync) | **POST** /v0/organizations/{org_id}/diagnostics/monitor/diagnose/analyzer/sync | Endpoint to diagnose a specific analyzer
[**recommend_diagnostic_interval**](MonitorDiagnosticsApi.md#recommend_diagnostic_interval) | **POST** /v0/organizations/{org_id}/diagnostics/monitor/interval | Endpoint to recommend a diagnostic interval


# **detect_noisy_analyzers**
> AnalyzersDiagnosticResponse detect_noisy_analyzers(org_id, analyzers_diagnostic_request)

Endpoint to detect noisy or failing analyzers

Returns a list of analyzers sorted so the noisiest (most anomalies per column) is first. Also includes a similar list for analyzer failures.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import monitor_diagnostics_api
from whylabs_client.model.analyzers_diagnostic_request import AnalyzersDiagnosticRequest
from whylabs_client.model.analyzers_diagnostic_response import AnalyzersDiagnosticResponse
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
    api_instance = monitor_diagnostics_api.MonitorDiagnosticsApi(api_client)
    org_id = "org-123" # str | 
    analyzers_diagnostic_request = AnalyzersDiagnosticRequest(
        interval="2024-01-01T00:00:00Z/2024-01-12T00:00:00Z",
        dataset_id="dataset_id_example",
    ) # AnalyzersDiagnosticRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Endpoint to detect noisy or failing analyzers
        api_response = api_instance.detect_noisy_analyzers(org_id, analyzers_diagnostic_request)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MonitorDiagnosticsApi->detect_noisy_analyzers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **analyzers_diagnostic_request** | [**AnalyzersDiagnosticRequest**](AnalyzersDiagnosticRequest.md)|  |

### Return type

[**AnalyzersDiagnosticResponse**](AnalyzersDiagnosticResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DetectNoisyAnalyzers 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detect_noisy_columns**
> AnalyzerSegmentColumnsDiagnosticResponse detect_noisy_columns(org_id, analyzer_segment_columns_diagnostic_request)

Endpoint to detect the noisiest columns for a specific analyzer and segment

Returns a list of column names sorted so the noisiest (most anomalies) is first. Also includes a similar list for columns with analyzer failures.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import monitor_diagnostics_api
from whylabs_client.model.analyzer_segment_columns_diagnostic_response import AnalyzerSegmentColumnsDiagnosticResponse
from whylabs_client.model.analyzer_segment_columns_diagnostic_request import AnalyzerSegmentColumnsDiagnosticRequest
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
    api_instance = monitor_diagnostics_api.MonitorDiagnosticsApi(api_client)
    org_id = "org-123" # str | 
    analyzer_segment_columns_diagnostic_request = AnalyzerSegmentColumnsDiagnosticRequest(
        interval="2024-01-01T00:00:00Z/2024-01-12T00:00:00Z",
        dataset_id="dataset_id_example",
        analyzer_id="analyzer_id_example",
        segment=Segment(
            tags=[
                SegmentTag(
                    key="key_example",
                    value="value_example",
                ),
            ],
        ),
    ) # AnalyzerSegmentColumnsDiagnosticRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Endpoint to detect the noisiest columns for a specific analyzer and segment
        api_response = api_instance.detect_noisy_columns(org_id, analyzer_segment_columns_diagnostic_request)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MonitorDiagnosticsApi->detect_noisy_columns: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **analyzer_segment_columns_diagnostic_request** | [**AnalyzerSegmentColumnsDiagnosticRequest**](AnalyzerSegmentColumnsDiagnosticRequest.md)|  |

### Return type

[**AnalyzerSegmentColumnsDiagnosticResponse**](AnalyzerSegmentColumnsDiagnosticResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DetectNoisyColumns 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detect_noisy_segments**
> AnalyzerSegmentsDiagnosticResponse detect_noisy_segments(org_id, analyzer_segments_diagnostic_request)

Endpoint to detect the noisiest segments for a specific analyzer

Returns a list of segments sorted so the noisiest (most anomalies per column) is first. Also includes a similar list for segments with analyzer failures.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import monitor_diagnostics_api
from whylabs_client.model.analyzer_segments_diagnostic_request import AnalyzerSegmentsDiagnosticRequest
from whylabs_client.model.analyzer_segments_diagnostic_response import AnalyzerSegmentsDiagnosticResponse
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
    api_instance = monitor_diagnostics_api.MonitorDiagnosticsApi(api_client)
    org_id = "org-123" # str | 
    analyzer_segments_diagnostic_request = AnalyzerSegmentsDiagnosticRequest(
        interval="2024-01-01T00:00:00Z/2024-01-12T00:00:00Z",
        dataset_id="dataset_id_example",
        analyzer_id="analyzer_id_example",
    ) # AnalyzerSegmentsDiagnosticRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Endpoint to detect the noisiest segments for a specific analyzer
        api_response = api_instance.detect_noisy_segments(org_id, analyzer_segments_diagnostic_request)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MonitorDiagnosticsApi->detect_noisy_segments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **analyzer_segments_diagnostic_request** | [**AnalyzerSegmentsDiagnosticRequest**](AnalyzerSegmentsDiagnosticRequest.md)|  |

### Return type

[**AnalyzerSegmentsDiagnosticResponse**](AnalyzerSegmentsDiagnosticResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DetectNoisySegments 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **diagnose_analyzer_sync**
> DiagnosisReport diagnose_analyzer_sync(org_id, diagnosis_request)

Endpoint to diagnose a specific analyzer

Returns a diagnosis report for a specific analyzer, segment, and interval. Only suitable for small datasets.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import monitor_diagnostics_api
from whylabs_client.model.diagnosis_request import DiagnosisRequest
from whylabs_client.model.diagnosis_report import DiagnosisReport
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
    api_instance = monitor_diagnostics_api.MonitorDiagnosticsApi(api_client)
    org_id = "org-123" # str | 
    diagnosis_request = DiagnosisRequest(
        dataset_id="dataset_id_example",
        analyzer_id="analyzer_id_example",
        segment=Segment(
            tags=[
                SegmentTag(
                    key="key_example",
                    value="value_example",
                ),
            ],
        ),
        interval="interval_example",
        columns=[
            "columns_example",
        ],
    ) # DiagnosisRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Endpoint to diagnose a specific analyzer
        api_response = api_instance.diagnose_analyzer_sync(org_id, diagnosis_request)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MonitorDiagnosticsApi->diagnose_analyzer_sync: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **diagnosis_request** | [**DiagnosisRequest**](DiagnosisRequest.md)|  |

### Return type

[**DiagnosisReport**](DiagnosisReport.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DiagnoseAnalyzerSync 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recommend_diagnostic_interval**
> DiagnosticIntervalResponse recommend_diagnostic_interval(org_id, diagnostic_interval_request)

Endpoint to recommend a diagnostic interval

Returns an interval containing the last 30 batches of data

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import monitor_diagnostics_api
from whylabs_client.model.diagnostic_interval_request import DiagnosticIntervalRequest
from whylabs_client.model.diagnostic_interval_response import DiagnosticIntervalResponse
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
    api_instance = monitor_diagnostics_api.MonitorDiagnosticsApi(api_client)
    org_id = "org-123" # str | 
    diagnostic_interval_request = DiagnosticIntervalRequest(
        dataset_id="dataset_id_example",
        batches=1,
    ) # DiagnosticIntervalRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Endpoint to recommend a diagnostic interval
        api_response = api_instance.recommend_diagnostic_interval(org_id, diagnostic_interval_request)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MonitorDiagnosticsApi->recommend_diagnostic_interval: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **diagnostic_interval_request** | [**DiagnosticIntervalRequest**](DiagnosticIntervalRequest.md)|  |

### Return type

[**DiagnosticIntervalResponse**](DiagnosticIntervalResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RecommendDiagnosticInterval 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

