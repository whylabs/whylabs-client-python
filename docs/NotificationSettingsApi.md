# whylabs_client.NotificationSettingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_notification_action**](NotificationSettingsApi.md#delete_notification_action) | **DELETE** /v0/notification-settings/{org_id}/actions/{action_id} | Delete notification action
[**get_email_notification_action_payload**](NotificationSettingsApi.md#get_email_notification_action_payload) | **GET** /v0/notification-settings/actions/email/payload | Get dummy notification action payload
[**get_notification_action**](NotificationSettingsApi.md#get_notification_action) | **GET** /v0/notification-settings/{org_id}/actions/{action_id} | Get notification action for id
[**get_notification_settings**](NotificationSettingsApi.md#get_notification_settings) | **GET** /v0/notification-settings/{org_id} | Get notification settings for an org
[**get_pager_duty_notification_action_payload**](NotificationSettingsApi.md#get_pager_duty_notification_action_payload) | **GET** /v0/notification-settings/actions/pagerduty/payload | Get dummy notification action payload
[**get_slack_notification_action_payload**](NotificationSettingsApi.md#get_slack_notification_action_payload) | **GET** /v0/notification-settings/actions/slack/payload | Get dummy notification action payload
[**list_notification_actions**](NotificationSettingsApi.md#list_notification_actions) | **GET** /v0/notification-settings/{org_id}/actions | List notification actions for an org
[**put_notification_action**](NotificationSettingsApi.md#put_notification_action) | **PUT** /v0/notification-settings/{org_id}/actions/{type}/{action_id} | Add new notification action
[**update_notification_action**](NotificationSettingsApi.md#update_notification_action) | **PATCH** /v0/notification-settings/{org_id}/actions/{type}/{action_id} | Update notification action
[**update_notification_settings**](NotificationSettingsApi.md#update_notification_settings) | **POST** /v0/notification-settings/{org_id} | Update notification settings for an org


# **delete_notification_action**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_notification_action(org_id, action_id)

Delete notification action

Delete notification action

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import notification_settings_api
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
    api_instance = notification_settings_api.NotificationSettingsApi(api_client)
    org_id = "org-123" # str | 
    action_id = "users-email-action" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete notification action
        api_response = api_instance.delete_notification_action(org_id, action_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling NotificationSettingsApi->delete_notification_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **action_id** | **str**|  |

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
**0** | DeleteNotificationAction default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_notification_action_payload**
> EmailNotificationAction get_email_notification_action_payload()

Get dummy notification action payload

Get dummy notification action payload

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import notification_settings_api
from whylabs_client.model.email_notification_action import EmailNotificationAction
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
    api_instance = notification_settings_api.NotificationSettingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get dummy notification action payload
        api_response = api_instance.get_email_notification_action_payload()
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling NotificationSettingsApi->get_email_notification_action_payload: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**EmailNotificationAction**](EmailNotificationAction.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | getEmailNotificationActionPayload default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_action**
> NotificationAction get_notification_action(org_id, action_id)

Get notification action for id

Get notification action for id

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import notification_settings_api
from whylabs_client.model.notification_action import NotificationAction
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
    api_instance = notification_settings_api.NotificationSettingsApi(api_client)
    org_id = "org-123" # str | 
    action_id = "users-email-action" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get notification action for id
        api_response = api_instance.get_notification_action(org_id, action_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling NotificationSettingsApi->get_notification_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **action_id** | **str**|  |

### Return type

[**NotificationAction**](NotificationAction.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GetNotificationAction default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_settings**
> GetNotificationSettingsResponse get_notification_settings(org_id)

Get notification settings for an org

Get notification settings for an org

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import notification_settings_api
from whylabs_client.model.get_notification_settings_response import GetNotificationSettingsResponse
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
    api_instance = notification_settings_api.NotificationSettingsApi(api_client)
    org_id = "org_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get notification settings for an org
        api_response = api_instance.get_notification_settings(org_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling NotificationSettingsApi->get_notification_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |

### Return type

[**GetNotificationSettingsResponse**](GetNotificationSettingsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GetNotificationSettings default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pager_duty_notification_action_payload**
> PagerDutyNotificationAction get_pager_duty_notification_action_payload()

Get dummy notification action payload

Get dummy notification action payload

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import notification_settings_api
from whylabs_client.model.pager_duty_notification_action import PagerDutyNotificationAction
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
    api_instance = notification_settings_api.NotificationSettingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get dummy notification action payload
        api_response = api_instance.get_pager_duty_notification_action_payload()
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling NotificationSettingsApi->get_pager_duty_notification_action_payload: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**PagerDutyNotificationAction**](PagerDutyNotificationAction.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | getPagerDutyNotificationActionPayload default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_slack_notification_action_payload**
> SlackNotificationAction get_slack_notification_action_payload()

Get dummy notification action payload

Get dummy notification action payload

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import notification_settings_api
from whylabs_client.model.slack_notification_action import SlackNotificationAction
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
    api_instance = notification_settings_api.NotificationSettingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get dummy notification action payload
        api_response = api_instance.get_slack_notification_action_payload()
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling NotificationSettingsApi->get_slack_notification_action_payload: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SlackNotificationAction**](SlackNotificationAction.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | getSlackNotificationActionPayload default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notification_actions**
> [NotificationAction] list_notification_actions(org_id)

List notification actions for an org

Get notification actions for an org

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import notification_settings_api
from whylabs_client.model.notification_action import NotificationAction
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
    api_instance = notification_settings_api.NotificationSettingsApi(api_client)
    org_id = "org-123" # str | 

    # example passing only required values which don't have defaults set
    try:
        # List notification actions for an org
        api_response = api_instance.list_notification_actions(org_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling NotificationSettingsApi->list_notification_actions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |

### Return type

[**[NotificationAction]**](NotificationAction.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ListNotificationActions default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_notification_action**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} put_notification_action(org_id, type, action_id, body)

Add new notification action

Add new notification action

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import notification_settings_api
from whylabs_client.model.action_type import ActionType
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
    api_instance = notification_settings_api.NotificationSettingsApi(api_client)
    org_id = "org-123" # str | 
    type = ActionType("EMAIL") # ActionType | 
    action_id = "users-email-action" # str | 
    body = "body_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Add new notification action
        api_response = api_instance.put_notification_action(org_id, type, action_id, body)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling NotificationSettingsApi->put_notification_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **type** | **ActionType**|  |
 **action_id** | **str**|  |
 **body** | **str**|  |

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
**0** | PutNotificationAction default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification_action**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_notification_action(org_id, type, action_id, body)

Update notification action

Update notification action

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import notification_settings_api
from whylabs_client.model.action_type import ActionType
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
    api_instance = notification_settings_api.NotificationSettingsApi(api_client)
    org_id = "org-123" # str | 
    type = ActionType("EMAIL") # ActionType | 
    action_id = "users-email-action" # str | 
    body = "body_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Update notification action
        api_response = api_instance.update_notification_action(org_id, type, action_id, body)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling NotificationSettingsApi->update_notification_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **type** | **ActionType**|  |
 **action_id** | **str**|  |
 **body** | **str**|  |

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
**0** | UpdateNotificationAction default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification_settings**
> NotificationSettings update_notification_settings(org_id, notification_settings)

Update notification settings for an org

Update notification settings for an org

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import whylabs_client
from whylabs_client.api import notification_settings_api
from whylabs_client.model.notification_settings import NotificationSettings
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
    api_instance = notification_settings_api.NotificationSettingsApi(api_client)
    org_id = "org_id_example" # str | 
    notification_settings = NotificationSettings(
        email_settings=UberNotificationSchedule(
            enabled=True,
            cadence=NotificationSqsMessageCadence("HOURLY"),
            day_of_week=NotificationSettingsDay("SUNDAY"),
            local24_hour_of_day=1,
            local_minute_of_hour=1,
            local_timezone="local_timezone_example",
        ),
        slack_settings=UberNotificationSchedule(
            enabled=True,
            cadence=NotificationSqsMessageCadence("HOURLY"),
            day_of_week=NotificationSettingsDay("SUNDAY"),
            local24_hour_of_day=1,
            local_minute_of_hour=1,
            local_timezone="local_timezone_example",
        ),
        pager_duty_settings=UberNotificationSchedule(
            enabled=True,
            cadence=NotificationSqsMessageCadence("HOURLY"),
            day_of_week=NotificationSettingsDay("SUNDAY"),
            local24_hour_of_day=1,
            local_minute_of_hour=1,
            local_timezone="local_timezone_example",
        ),
    ) # NotificationSettings | 

    # example passing only required values which don't have defaults set
    try:
        # Update notification settings for an org
        api_response = api_instance.update_notification_settings(org_id, notification_settings)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling NotificationSettingsApi->update_notification_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **notification_settings** | [**NotificationSettings**](NotificationSettings.md)|  |

### Return type

[**NotificationSettings**](NotificationSettings.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | UpdateNotificationSettings default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

