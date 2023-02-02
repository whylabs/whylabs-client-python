"""
    WhyLabs API client

    WhyLabs API that enables end-to-end AI observability  # noqa: E501

    The version of the OpenAPI document: 0.1
    Contact: support@whylabs.ai
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from whylabs_client.api_client import ApiClient, Endpoint as _Endpoint
from whylabs_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from whylabs_client.model.close_session_response import CloseSessionResponse
from whylabs_client.model.create_session_response import CreateSessionResponse
from whylabs_client.model.create_session_upload_response import CreateSessionUploadResponse
from whylabs_client.model.get_session_response import GetSessionResponse


class SessionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.close_session_endpoint = _Endpoint(
            settings={
                'response_type': (CloseSessionResponse,),
                'auth': [],
                'endpoint_path': '/v0/sessions/{session_token}/close',
                'operation_id': 'close_session',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'session_token',
                ],
                'required': [
                    'session_token',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'session_token':
                        (str,),
                },
                'attribute_map': {
                    'session_token': 'session_token',
                },
                'location_map': {
                    'session_token': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.create_dataset_profile_upload_endpoint = _Endpoint(
            settings={
                'response_type': (CreateSessionUploadResponse,),
                'auth': [],
                'endpoint_path': '/v0/sessions/{session_token}/upload',
                'operation_id': 'create_dataset_profile_upload',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'session_token',
                    'dataset_timestamp',
                ],
                'required': [
                    'session_token',
                ],
                'nullable': [
                    'dataset_timestamp',
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'session_token':
                        (str,),
                    'dataset_timestamp':
                        (int, none_type,),
                },
                'attribute_map': {
                    'session_token': 'session_token',
                    'dataset_timestamp': 'dataset_timestamp',
                },
                'location_map': {
                    'session_token': 'path',
                    'dataset_timestamp': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.create_session_endpoint = _Endpoint(
            settings={
                'response_type': (CreateSessionResponse,),
                'auth': [],
                'endpoint_path': '/v0/sessions',
                'operation_id': 'create_session',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_session_endpoint = _Endpoint(
            settings={
                'response_type': (GetSessionResponse,),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/v0/sessions/{session_token}',
                'operation_id': 'get_session',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'session_token',
                ],
                'required': [
                    'session_token',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'session_token':
                        (str,),
                },
                'attribute_map': {
                    'session_token': 'session_token',
                },
                'location_map': {
                    'session_token': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def close_session(
        self,
        session_token,
        **kwargs
    ):
        """naddeo Close a session, triggering its display in whylabs and making it no longer accept any additional data.  # noqa: E501

        naddeo Close a session, triggering its display in whylabs and making it no longer accept any additional data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.close_session(session_token, async_req=True)
        >>> result = thread.get()

        Args:
            session_token (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CloseSessionResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['session_token'] = \
            session_token
        return self.close_session_endpoint.call_with_http_info(**kwargs)

    def create_dataset_profile_upload(
        self,
        session_token,
        **kwargs
    ):
        """Create an upload for a given session.  # noqa: E501

        Create an upload for a given session.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_dataset_profile_upload(session_token, async_req=True)
        >>> result = thread.get()

        Args:
            session_token (str):

        Keyword Args:
            dataset_timestamp (int, none_type): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CreateSessionUploadResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['session_token'] = \
            session_token
        return self.create_dataset_profile_upload_endpoint.call_with_http_info(**kwargs)

    def create_session(
        self,
        **kwargs
    ):
        """Create a new session that can be used to upload dataset profiles from whylogs for display in whylabs.  # noqa: E501

        Create a new session that can be used to upload dataset profiles from whylogs for display in whylabs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_session(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CreateSessionResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.create_session_endpoint.call_with_http_info(**kwargs)

    def get_session(
        self,
        session_token,
        **kwargs
    ):
        """Get information about a session.  # noqa: E501

        Get information about a session.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_session(session_token, async_req=True)
        >>> result = thread.get()

        Args:
            session_token (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            GetSessionResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['session_token'] = \
            session_token
        return self.get_session_endpoint.call_with_http_info(**kwargs)

