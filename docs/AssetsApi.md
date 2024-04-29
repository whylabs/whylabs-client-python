# whylabs_client.AssetsApi

All URIs are relative to *https://api.whylabsapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset**](AssetsApi.md#get_asset) | **GET** /v1/assets/{asset_id} | Endpoint to retrieve assets
[**upload_asset**](AssetsApi.md#upload_asset) | **POST** /v1/assets/{asset_id}/upload | Endpoint to upload an asset


# **get_asset**
> GetAssetResponse get_asset(asset_id)

Endpoint to retrieve assets

Endpoint to retrieve assets

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import assets_api
from whylabs_client.model.get_asset_response import GetAssetResponse
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
    api_instance = assets_api.AssetsApi(api_client)
    asset_id = "asset-123" # str | 
    tag = "tag_example" # str, none_type |  (optional)
    version = 1 # int, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Endpoint to retrieve assets
        api_response = api_instance.get_asset(asset_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling AssetsApi->get_asset: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Endpoint to retrieve assets
        api_response = api_instance.get_asset(asset_id, tag=tag, version=version)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling AssetsApi->get_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **tag** | **str, none_type**|  | [optional]
 **version** | **int, none_type**|  | [optional]

### Return type

[**GetAssetResponse**](GetAssetResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GetAsset 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_asset**
> UploadAssetResponse upload_asset(asset_id, upload_asset_request)

Endpoint to upload an asset

Endpoint to upload an asset

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import assets_api
from whylabs_client.model.upload_asset_response import UploadAssetResponse
from whylabs_client.model.upload_asset_request import UploadAssetRequest
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
    api_instance = assets_api.AssetsApi(api_client)
    asset_id = "asset-123" # str | 
    upload_asset_request = UploadAssetRequest(
        file_name="file_name_example",
        tag="tag_example",
    ) # UploadAssetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Endpoint to upload an asset
        api_response = api_instance.upload_asset(asset_id, upload_asset_request)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling AssetsApi->upload_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **upload_asset_request** | [**UploadAssetRequest**](UploadAssetRequest.md)|  |

### Return type

[**UploadAssetResponse**](UploadAssetResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UploadAsset 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

