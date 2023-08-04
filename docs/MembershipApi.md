# whylabs_client.MembershipApi

All URIs are relative to *https://api.whylabsapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization_membership**](MembershipApi.md#create_organization_membership) | **POST** /v0/organizations/{org_id}/membership | Create a membership for a user, making them apart of an organization. Uses the user&#39;s current email address.
[**list_organization_memberships**](MembershipApi.md#list_organization_memberships) | **GET** /v0/organizations/{org_id}/membership | List organization memberships
[**remove_organization_membership**](MembershipApi.md#remove_organization_membership) | **DELETE** /v0/organizations/{org_id}/membership | Removes membership in a given org from a user, using the user&#39;s email address.
[**update_organization_membership**](MembershipApi.md#update_organization_membership) | **PUT** /v0/organizations/{org_id}/membership | Updates the role in an membership


# **create_organization_membership**
> MembershipMetadata create_organization_membership(org_id, email, role)

Create a membership for a user, making them apart of an organization. Uses the user's current email address.

Create a membership for a user, making them apart of an organization. Uses the user's current email address.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import membership_api
from whylabs_client.model.role import Role
from whylabs_client.model.membership_metadata import MembershipMetadata
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
    api_instance = membership_api.MembershipApi(api_client)
    org_id = "org-123" # str | 
    email = "user@whylabs.ai" # str | 
    role = Role("ADMIN") # Role | 
    set_default = False # bool, none_type |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Create a membership for a user, making them apart of an organization. Uses the user's current email address.
        api_response = api_instance.create_organization_membership(org_id, email, role)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MembershipApi->create_organization_membership: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a membership for a user, making them apart of an organization. Uses the user's current email address.
        api_response = api_instance.create_organization_membership(org_id, email, role, set_default=set_default)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MembershipApi->create_organization_membership: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **email** | **str**|  |
 **role** | **Role**|  |
 **set_default** | **bool, none_type**|  | [optional] if omitted the server will use the default value of False

### Return type

[**MembershipMetadata**](MembershipMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CreateOrganizationMembership default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organization_memberships**
> ListOrganizationMembershipsResponse list_organization_memberships(org_id)

List organization memberships

list memberships for an organization

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import membership_api
from whylabs_client.model.list_organization_memberships_response import ListOrganizationMembershipsResponse
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
    api_instance = membership_api.MembershipApi(api_client)
    org_id = "org-123" # str | 

    # example passing only required values which don't have defaults set
    try:
        # List organization memberships
        api_response = api_instance.list_organization_memberships(org_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MembershipApi->list_organization_memberships: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |

### Return type

[**ListOrganizationMembershipsResponse**](ListOrganizationMembershipsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ListOrganizationMemberships default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_organization_membership**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} remove_organization_membership(org_id, email)

Removes membership in a given org from a user, using the user's email address.

Removes membership in a given org from a user, using the user's email address.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import membership_api
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
    api_instance = membership_api.MembershipApi(api_client)
    org_id = "org-123" # str | 
    email = "user@whylabs.ai" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Removes membership in a given org from a user, using the user's email address.
        api_response = api_instance.remove_organization_membership(org_id, email)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MembershipApi->remove_organization_membership: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **email** | **str**|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | RemoveOrganizationMembership default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization_membership**
> MembershipMetadata update_organization_membership(org_id, email, role)

Updates the role in an membership

Updates the role in an membership, given the organization and the user's email address.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import membership_api
from whylabs_client.model.role import Role
from whylabs_client.model.membership_metadata import MembershipMetadata
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
    api_instance = membership_api.MembershipApi(api_client)
    org_id = "org-123" # str | 
    email = "user@whylabs.ai" # str | 
    role = Role("ADMIN") # Role | 

    # example passing only required values which don't have defaults set
    try:
        # Updates the role in an membership
        api_response = api_instance.update_organization_membership(org_id, email, role)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MembershipApi->update_organization_membership: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **email** | **str**|  |
 **role** | **Role**|  |

### Return type

[**MembershipMetadata**](MembershipMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | UpdateOrganizationMembership default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

