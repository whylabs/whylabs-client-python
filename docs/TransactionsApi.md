# whylabs_client.TransactionsApi

All URIs are relative to *https://api.whylabsapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_transaction**](TransactionsApi.md#abort_transaction) | **POST** /v1/transaction/abort | Abort a transaction which has not yet been committed
[**commit_transaction**](TransactionsApi.md#commit_transaction) | **POST** /v1/transaction/commit | Commit a log transaction
[**log_transaction**](TransactionsApi.md#log_transaction) | **POST** /v1/transaction/log | Add to a log transaction
[**start_transaction**](TransactionsApi.md#start_transaction) | **POST** /v1/transaction | Start a log transaction
[**transaction_status**](TransactionsApi.md#transaction_status) | **GET** /v1/transaction | Get the status of a log transaction


# **abort_transaction**
> Response abort_transaction(transaction_id)

Abort a transaction which has not yet been committed

Abort a transaction which has not yet been committed

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import transactions_api
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
    api_instance = transactions_api.TransactionsApi(api_client)
    transaction_id = "28541e19-72c2-4c43-bbce-84e4de362101" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Abort a transaction which has not yet been committed
        api_response = api_instance.abort_transaction(transaction_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling TransactionsApi->abort_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  |

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
**200** | AbortTransaction 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commit_transaction**
> Response commit_transaction(transaction_id, transaction_commit_request)

Commit a log transaction

API to commit a log transaction

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import transactions_api
from whylabs_client.model.transaction_commit_request import TransactionCommitRequest
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
    api_instance = transactions_api.TransactionsApi(api_client)
    transaction_id = "28541e19-72c2-4c43-bbce-84e4de362101" # str | 
    transaction_commit_request = TransactionCommitRequest(
        verbose=True,
    ) # TransactionCommitRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Commit a log transaction
        api_response = api_instance.commit_transaction(transaction_id, transaction_commit_request)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling TransactionsApi->commit_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  |
 **transaction_commit_request** | [**TransactionCommitRequest**](TransactionCommitRequest.md)|  |

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
**200** | CommitTransaction 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_transaction**
> AsyncLogResponse log_transaction(transaction_id, transaction_log_request)

Add to a log transaction

API to add to a log transaction

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import transactions_api
from whylabs_client.model.transaction_log_request import TransactionLogRequest
from whylabs_client.model.async_log_response import AsyncLogResponse
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
    api_instance = transactions_api.TransactionsApi(api_client)
    transaction_id = "28541e19-72c2-4c43-bbce-84e4de362101" # str | 
    transaction_log_request = TransactionLogRequest(
        dataset_timestamp=1,
        segment_tags=[
            SegmentTag(
                key="key_example",
                value="value_example",
            ),
        ],
        region="region_example",
    ) # TransactionLogRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Add to a log transaction
        api_response = api_instance.log_transaction(transaction_id, transaction_log_request)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling TransactionsApi->log_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  |
 **transaction_log_request** | [**TransactionLogRequest**](TransactionLogRequest.md)|  |

### Return type

[**AsyncLogResponse**](AsyncLogResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LogTransaction 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_transaction**
> LogTransactionMetadata start_transaction(transaction_start_request)

Start a log transaction

API to start a log transaction

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import transactions_api
from whylabs_client.model.log_transaction_metadata import LogTransactionMetadata
from whylabs_client.model.transaction_start_request import TransactionStartRequest
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
    api_instance = transactions_api.TransactionsApi(api_client)
    transaction_start_request = TransactionStartRequest(
        dataset_id="dataset_id_example",
    ) # TransactionStartRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Start a log transaction
        api_response = api_instance.start_transaction(transaction_start_request)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling TransactionsApi->start_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_start_request** | [**TransactionStartRequest**](TransactionStartRequest.md)|  |

### Return type

[**LogTransactionMetadata**](LogTransactionMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | StartTransaction 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transaction_status**
> TransactionStatusResponse transaction_status(transaction_id)

Get the status of a log transaction

API to get the status of a log transaction

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import transactions_api
from whylabs_client.model.transaction_status_response import TransactionStatusResponse
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
    api_instance = transactions_api.TransactionsApi(api_client)
    transaction_id = "28541e19-72c2-4c43-bbce-84e4de362101" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get the status of a log transaction
        api_response = api_instance.transaction_status(transaction_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling TransactionsApi->transaction_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  |

### Return type

[**TransactionStatusResponse**](TransactionStatusResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TransactionStatus 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

