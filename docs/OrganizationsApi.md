# whylabs_client.OrganizationsApi

All URIs are relative to *https://api.whylabsapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_managed_organization**](OrganizationsApi.md#create_managed_organization) | **POST** /v1/organizations/managed-organization | Create a managed organization for a parent organization
[**get_managed_organizations**](OrganizationsApi.md#get_managed_organizations) | **GET** /v1/organizations/managed-organizations | List managed organizations for a parent organization
[**get_resource_tag_configuration**](OrganizationsApi.md#get_resource_tag_configuration) | **GET** /v1/organizations/resource-tag | Get resoruce tag configuration for an organization
[**upload_resource_tag_configuration**](OrganizationsApi.md#upload_resource_tag_configuration) | **PUT** /v1/organizations/resource-tag | Upload resoruce tag configuration for an organization


# **create_managed_organization**
> OrganizationIdentifier create_managed_organization(create_managed_organization_request)

Create a managed organization for a parent organization

Create a managed organization for a parent organization

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import organizations_api
from whylabs_client.model.create_managed_organization_request import CreateManagedOrganizationRequest
from whylabs_client.model.organization_identifier import OrganizationIdentifier
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
    api_instance = organizations_api.OrganizationsApi(api_client)
    create_managed_organization_request = CreateManagedOrganizationRequest(
        name="name_example",
    ) # CreateManagedOrganizationRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a managed organization for a parent organization
        api_response = api_instance.create_managed_organization(create_managed_organization_request)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling OrganizationsApi->create_managed_organization: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_managed_organization_request** | [**CreateManagedOrganizationRequest**](CreateManagedOrganizationRequest.md)|  |

### Return type

[**OrganizationIdentifier**](OrganizationIdentifier.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CreateManagedOrganization 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_managed_organizations**
> [OrganizationIdentifier] get_managed_organizations()

List managed organizations for a parent organization

List managed organizations for a parent organization

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import organizations_api
from whylabs_client.model.organization_identifier import OrganizationIdentifier
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
    api_instance = organizations_api.OrganizationsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List managed organizations for a parent organization
        api_response = api_instance.get_managed_organizations()
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling OrganizationsApi->get_managed_organizations: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[OrganizationIdentifier]**](OrganizationIdentifier.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GetManagedOrganizations 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_tag_configuration**
> str get_resource_tag_configuration()

Get resoruce tag configuration for an organization

Get resoruce tag configuration for an organization

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import organizations_api
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
    api_instance = organizations_api.OrganizationsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get resoruce tag configuration for an organization
        api_response = api_instance.get_resource_tag_configuration()
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling OrganizationsApi->get_resource_tag_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GetResourceTagConfiguration 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_resource_tag_configuration**
> Response upload_resource_tag_configuration(body)

Upload resoruce tag configuration for an organization

Upload resoruce tag configuration for an organization

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import organizations_api
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
    api_instance = organizations_api.OrganizationsApi(api_client)
    body = "body_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Upload resoruce tag configuration for an organization
        api_response = api_instance.upload_resource_tag_configuration(body)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling OrganizationsApi->upload_resource_tag_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  |

### Return type

[**Response**](Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UploadResourceTagConfiguration 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

