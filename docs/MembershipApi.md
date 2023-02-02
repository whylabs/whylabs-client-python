# whylabs_client.MembershipApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_membership**](MembershipApi.md#create_membership) | **POST** /v0/membership | Create a membership for a user, making them apart of an organization. Uses the user&#39;s current email address.
[**create_organization_membership**](MembershipApi.md#create_organization_membership) | **POST** /v0/organizations/{org_id}/membership | Create a membership for a user, making them apart of an organization. Uses the user&#39;s current email address.
[**get_default_membership_for_email**](MembershipApi.md#get_default_membership_for_email) | **GET** /v0/membership/default | Get the default membership for a user.
[**get_memberships**](MembershipApi.md#get_memberships) | **GET** /v0/membership/user/{user_id} | Get memberships for a user.
[**get_memberships_by_email**](MembershipApi.md#get_memberships_by_email) | **GET** /v0/membership/user | Get memberships for a user given that user&#39;s email address.
[**get_memberships_by_org**](MembershipApi.md#get_memberships_by_org) | **GET** /v0/membership/org/{org_id} | Get memberships for an org.
[**list_organization_memberships**](MembershipApi.md#list_organization_memberships) | **GET** /v0/organizations/{org_id}/membership | List organization memberships
[**remove_membership_by_email**](MembershipApi.md#remove_membership_by_email) | **DELETE** /v0/membership | Removes membership in a given org from a user, using the user&#39;s email address.
[**remove_organization_membership**](MembershipApi.md#remove_organization_membership) | **DELETE** /v0/organizations/{org_id}/membership | Removes membership in a given org from a user, using the user&#39;s email address.
[**set_default_membership**](MembershipApi.md#set_default_membership) | **POST** /v0/membership/default | Sets the organization that should be used when logging a user in
[**update_membership_by_email**](MembershipApi.md#update_membership_by_email) | **PUT** /v0/membership | Updates the role in an membership
[**update_organization_membership**](MembershipApi.md#update_organization_membership) | **PUT** /v0/organizations/{org_id}/membership | Updates the role in an membership


# **create_membership**
> MembershipMetadata create_membership(add_membership_request)

Create a membership for a user, making them apart of an organization. Uses the user's current email address.

Create a membership for a user, making them apart of an organization. Uses the user's current email address.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import membership_api
from whylabs_client.model.add_membership_request import AddMembershipRequest
from whylabs_client.model.membership_metadata import MembershipMetadata
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
    api_instance = membership_api.MembershipApi(api_client)
    add_membership_request = AddMembershipRequest(
        org_id="org_id_example",
        email="email_example",
        role=Role("ADMIN"),
        created_by="created_by_example",
        default=True,
    ) # AddMembershipRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a membership for a user, making them apart of an organization. Uses the user's current email address.
        api_response = api_instance.create_membership(add_membership_request)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MembershipApi->create_membership: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_membership_request** | [**AddMembershipRequest**](AddMembershipRequest.md)|  |

### Return type

[**MembershipMetadata**](MembershipMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CreateMembership default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **get_default_membership_for_email**
> GetDefaultMembershipResponse get_default_membership_for_email(email)

Get the default membership for a user.

Get the default membership for a user.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import membership_api
from whylabs_client.model.get_default_membership_response import GetDefaultMembershipResponse
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
    api_instance = membership_api.MembershipApi(api_client)
    email = "email_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get the default membership for a user.
        api_response = api_instance.get_default_membership_for_email(email)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MembershipApi->get_default_membership_for_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  |

### Return type

[**GetDefaultMembershipResponse**](GetDefaultMembershipResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GetDefaultMembershipForEmail default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_memberships**
> GetMembershipsResponse get_memberships(user_id)

Get memberships for a user.

Get memberships for a user.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import membership_api
from whylabs_client.model.get_memberships_response import GetMembershipsResponse
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
    api_instance = membership_api.MembershipApi(api_client)
    user_id = "user_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get memberships for a user.
        api_response = api_instance.get_memberships(user_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MembershipApi->get_memberships: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |

### Return type

[**GetMembershipsResponse**](GetMembershipsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GetMemberships default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_memberships_by_email**
> GetMembershipsResponse get_memberships_by_email(email)

Get memberships for a user given that user's email address.

Get memberships for a user given that user's email address.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import membership_api
from whylabs_client.model.get_memberships_response import GetMembershipsResponse
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
    api_instance = membership_api.MembershipApi(api_client)
    email = "email_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get memberships for a user given that user's email address.
        api_response = api_instance.get_memberships_by_email(email)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MembershipApi->get_memberships_by_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  |

### Return type

[**GetMembershipsResponse**](GetMembershipsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GetMembershipsByEmail default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_memberships_by_org**
> GetMembershipsResponse get_memberships_by_org(org_id)

Get memberships for an org.

Get memberships for an org.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import membership_api
from whylabs_client.model.get_memberships_response import GetMembershipsResponse
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
    api_instance = membership_api.MembershipApi(api_client)
    org_id = "org_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get memberships for an org.
        api_response = api_instance.get_memberships_by_org(org_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MembershipApi->get_memberships_by_org: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |

### Return type

[**GetMembershipsResponse**](GetMembershipsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GetMembershipsByOrg default response |  -  |

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

# **remove_membership_by_email**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} remove_membership_by_email(remove_membership_request)

Removes membership in a given org from a user, using the user's email address.

Removes membership in a given org from a user, using the user's email address.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import membership_api
from whylabs_client.model.remove_membership_request import RemoveMembershipRequest
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
    api_instance = membership_api.MembershipApi(api_client)
    remove_membership_request = RemoveMembershipRequest(
        org_id="org_id_example",
        email="email_example",
    ) # RemoveMembershipRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Removes membership in a given org from a user, using the user's email address.
        api_response = api_instance.remove_membership_by_email(remove_membership_request)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MembershipApi->remove_membership_by_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_membership_request** | [**RemoveMembershipRequest**](RemoveMembershipRequest.md)|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | RemoveMembershipByEmail default response |  -  |

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

# **set_default_membership**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} set_default_membership(set_default_membership_request)

Sets the organization that should be used when logging a user in

Sets the organization that should be used when logging a user in

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import membership_api
from whylabs_client.model.set_default_membership_request import SetDefaultMembershipRequest
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
    api_instance = membership_api.MembershipApi(api_client)
    set_default_membership_request = SetDefaultMembershipRequest(
        org_id="org_id_example",
        user_id="user_id_example",
    ) # SetDefaultMembershipRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Sets the organization that should be used when logging a user in
        api_response = api_instance.set_default_membership(set_default_membership_request)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MembershipApi->set_default_membership: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_default_membership_request** | [**SetDefaultMembershipRequest**](SetDefaultMembershipRequest.md)|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | SetDefaultMembership default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_membership_by_email**
> MembershipMetadata update_membership_by_email(update_membership_request)

Updates the role in an membership

Updates the role in an membership, given the organization and the user's email address.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import membership_api
from whylabs_client.model.update_membership_request import UpdateMembershipRequest
from whylabs_client.model.membership_metadata import MembershipMetadata
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
    api_instance = membership_api.MembershipApi(api_client)
    update_membership_request = UpdateMembershipRequest(
        org_id="org_id_example",
        email="email_example",
        role=Role("ADMIN"),
    ) # UpdateMembershipRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Updates the role in an membership
        api_response = api_instance.update_membership_by_email(update_membership_request)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling MembershipApi->update_membership_by_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_membership_request** | [**UpdateMembershipRequest**](UpdateMembershipRequest.md)|  |

### Return type

[**MembershipMetadata**](MembershipMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | UpdateMembershipByEmail default response |  -  |

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

