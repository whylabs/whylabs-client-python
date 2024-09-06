# whylabs_client.MembershipApi

All URIs are relative to *https://api.whylabsapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_saml_role_mapping**](MembershipApi.md#add_saml_role_mapping) | **POST** /v1/membership/saml/role-mapping | Add SAML JIT role claim mapping.
[**create_organization_membership**](MembershipApi.md#create_organization_membership) | **POST** /v0/organizations/{org_id}/membership | Create a membership for a user, making them a part of an organization. Uses the user&#39;s current email address.
[**delete_saml_role_mapping**](MembershipApi.md#delete_saml_role_mapping) | **DELETE** /v1/membership/saml/role-mapping | Delete SAML JIT role claim mapping.
[**get_saml_role_mapping**](MembershipApi.md#get_saml_role_mapping) | **GET** /v1/membership/saml/role-mapping | Get SAML JIT role claim mapping.
[**list_organization_memberships**](MembershipApi.md#list_organization_memberships) | **GET** /v0/organizations/{org_id}/membership | List organization memberships
[**remove_organization_membership**](MembershipApi.md#remove_organization_membership) | **DELETE** /v0/organizations/{org_id}/membership | Removes membership in a given org from a user, using the user&#39;s email address.
[**update_organization_membership**](MembershipApi.md#update_organization_membership) | **PUT** /v0/organizations/{org_id}/membership | Updates the role in an membership


# **add_saml_role_mapping**
> Response add_saml_role_mapping(connection, group, claim_configuration_membership)

Add SAML JIT role claim mapping.

Add SAML JIT role claim mapping.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import membership_api
from whylabs_client.model.claim_configuration_membership import ClaimConfigurationMembership
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
    api_instance = membership_api.MembershipApi(api_client)
    connection = "connection_example" # str | 
    group = "group_example" # str | 
    claim_configuration_membership = [
        ClaimConfigurationMembership(
            org_id="org_id_example",
            role=Role("ADMIN"),
        ),
    ] # [ClaimConfigurationMembership] | 

    # example passing only required values which don't have defaults set
    try:
        # Add SAML JIT role claim mapping.
        api_response = api_instance.add_saml_role_mapping(connection, group, claim_configuration_membership)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MembershipApi->add_saml_role_mapping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection** | **str**|  |
 **group** | **str**|  |
 **claim_configuration_membership** | [**[ClaimConfigurationMembership]**](ClaimConfigurationMembership.md)|  |

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
**200** | AddSamlRoleMapping 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_organization_membership**
> MembershipMetadata create_organization_membership(org_id, email, role)

Create a membership for a user, making them a part of an organization. Uses the user's current email address.

Create a membership for a user, making them a part of an organization. Uses the user's current email address.

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
        # Create a membership for a user, making them a part of an organization. Uses the user's current email address.
        api_response = api_instance.create_organization_membership(org_id, email, role)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MembershipApi->create_organization_membership: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a membership for a user, making them a part of an organization. Uses the user's current email address.
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
**200** | CreateOrganizationMembership 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_saml_role_mapping**
> Response delete_saml_role_mapping(connection, group)

Delete SAML JIT role claim mapping.

DeleteSAML JIT role claim mapping.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import membership_api
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
    api_instance = membership_api.MembershipApi(api_client)
    connection = "connection_example" # str | 
    group = "group_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete SAML JIT role claim mapping.
        api_response = api_instance.delete_saml_role_mapping(connection, group)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MembershipApi->delete_saml_role_mapping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection** | **str**|  |
 **group** | **str**|  |

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
**200** | DeleteSamlRoleMapping 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_saml_role_mapping**
> ClaimMembershipRoleConfiguration get_saml_role_mapping(connection)

Get SAML JIT role claim mapping.

Get SAML JIT role claim mapping.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import membership_api
from whylabs_client.model.claim_membership_role_configuration import ClaimMembershipRoleConfiguration
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
    connection = "connection_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get SAML JIT role claim mapping.
        api_response = api_instance.get_saml_role_mapping(connection)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MembershipApi->get_saml_role_mapping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection** | **str**|  |

### Return type

[**ClaimMembershipRoleConfiguration**](ClaimMembershipRoleConfiguration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GetSamlRoleMapping 200 response |  -  |

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
**200** | ListOrganizationMemberships 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_organization_membership**
> remove_organization_membership(org_id, email)

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
        api_instance.remove_organization_membership(org_id, email)
    except whylabs_client.ApiException as e:
        print("Exception when calling MembershipApi->remove_organization_membership: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **email** | **str**|  |

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RemoveOrganizationMembership 200 response |  -  |

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
**200** | UpdateOrganizationMembership 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

