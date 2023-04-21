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
from whylabs_client.model.delete_analyzer_results_response import DeleteAnalyzerResultsResponse
from whylabs_client.model.delete_dataset_profiles_response import DeleteDatasetProfilesResponse
from whylabs_client.model.reference_profile_item_response import ReferenceProfileItemResponse


class DatasetProfileApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.delete_analyzer_results_endpoint = _Endpoint(
            settings={
                'response_type': (DeleteAnalyzerResultsResponse,),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/v0/organizations/{org_id}/dataset-profiles/models/{dataset_id}/analyzer-results',
                'operation_id': 'delete_analyzer_results',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'org_id',
                    'dataset_id',
                    'start_timestamp',
                    'end_timestamp',
                ],
                'required': [
                    'org_id',
                    'dataset_id',
                ],
                'nullable': [
                    'start_timestamp',
                    'end_timestamp',
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
                    'org_id':
                        (str,),
                    'dataset_id':
                        (str,),
                    'start_timestamp':
                        (int, none_type,),
                    'end_timestamp':
                        (int, none_type,),
                },
                'attribute_map': {
                    'org_id': 'org_id',
                    'dataset_id': 'dataset_id',
                    'start_timestamp': 'start_timestamp',
                    'end_timestamp': 'end_timestamp',
                },
                'location_map': {
                    'org_id': 'path',
                    'dataset_id': 'path',
                    'start_timestamp': 'query',
                    'end_timestamp': 'query',
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
        self.delete_dataset_profiles_endpoint = _Endpoint(
            settings={
                'response_type': (DeleteDatasetProfilesResponse,),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/v0/organizations/{org_id}/dataset-profiles/models/{dataset_id}',
                'operation_id': 'delete_dataset_profiles',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'org_id',
                    'dataset_id',
                    'profile_start_timestamp',
                    'profile_end_timestamp',
                    'before_upload_timestamp',
                ],
                'required': [
                    'org_id',
                    'dataset_id',
                ],
                'nullable': [
                    'profile_start_timestamp',
                    'profile_end_timestamp',
                    'before_upload_timestamp',
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
                    'org_id':
                        (str,),
                    'dataset_id':
                        (str,),
                    'profile_start_timestamp':
                        (int, none_type,),
                    'profile_end_timestamp':
                        (int, none_type,),
                    'before_upload_timestamp':
                        (int, none_type,),
                },
                'attribute_map': {
                    'org_id': 'org_id',
                    'dataset_id': 'dataset_id',
                    'profile_start_timestamp': 'profile_start_timestamp',
                    'profile_end_timestamp': 'profile_end_timestamp',
                    'before_upload_timestamp': 'before_upload_timestamp',
                },
                'location_map': {
                    'org_id': 'path',
                    'dataset_id': 'path',
                    'profile_start_timestamp': 'query',
                    'profile_end_timestamp': 'query',
                    'before_upload_timestamp': 'query',
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
        self.list_reference_profiles_endpoint = _Endpoint(
            settings={
                'response_type': ([ReferenceProfileItemResponse],),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/v0/organizations/{org_id}/dataset-profiles/models/{model_id}/reference-profiles',
                'operation_id': 'list_reference_profiles',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'org_id',
                    'model_id',
                    'from_epoch',
                    'to_epoch',
                ],
                'required': [
                    'org_id',
                    'model_id',
                ],
                'nullable': [
                    'from_epoch',
                    'to_epoch',
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
                    'org_id':
                        (str,),
                    'model_id':
                        (str,),
                    'from_epoch':
                        (int, none_type,),
                    'to_epoch':
                        (int, none_type,),
                },
                'attribute_map': {
                    'org_id': 'org_id',
                    'model_id': 'model_id',
                    'from_epoch': 'from_epoch',
                    'to_epoch': 'to_epoch',
                },
                'location_map': {
                    'org_id': 'path',
                    'model_id': 'path',
                    'from_epoch': 'query',
                    'to_epoch': 'query',
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

    def delete_analyzer_results(
        self,
        org_id,
        dataset_id,
        **kwargs
    ):
        """Deletes a set of analyzer results  # noqa: E501

        Deletes a set of analyzer results. Returns false if scheduling deletion encountered some error.            # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_analyzer_results(org_id, dataset_id, async_req=True)
        >>> result = thread.get()

        Args:
            org_id (str): Your company's unique organization ID
            dataset_id (str): The unique dataset ID in your company.

        Keyword Args:
            start_timestamp (int, none_type): Optional, scope deleting analyzer results more recent than the timestamp. [optional]
            end_timestamp (int, none_type): Optional, scope deleting analyzer results older than the timestamp. [optional]
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
            DeleteAnalyzerResultsResponse
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
        kwargs['org_id'] = \
            org_id
        kwargs['dataset_id'] = \
            dataset_id
        return self.delete_analyzer_results_endpoint.call_with_http_info(**kwargs)

    def delete_dataset_profiles(
        self,
        org_id,
        dataset_id,
        **kwargs
    ):
        """Deletes a set of dataset profiles  # noqa: E501

        Deletes a set of dataset profiles. Returns false if scheduling deletion encountered some error.            # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_dataset_profiles(org_id, dataset_id, async_req=True)
        >>> result = thread.get()

        Args:
            org_id (str): Your company's unique organization ID
            dataset_id (str): The unique dataset ID in your company.

        Keyword Args:
            profile_start_timestamp (int, none_type): Optional, scope deleting profiles more recently than the timestamp. [optional]
            profile_end_timestamp (int, none_type): Optional, scope deleting profiles older than the timestamp. [optional]
            before_upload_timestamp (int, none_type): Optional, scope deleting profiles uploaded prior to the timestamp. [optional]
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
            DeleteDatasetProfilesResponse
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
        kwargs['org_id'] = \
            org_id
        kwargs['dataset_id'] = \
            dataset_id
        return self.delete_dataset_profiles_endpoint.call_with_http_info(**kwargs)

    def list_reference_profiles(
        self,
        org_id,
        model_id,
        **kwargs
    ):
        """Returns a list for reference profiles  # noqa: E501

        Returns a list of Reference Profiles.            # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_reference_profiles(org_id, model_id, async_req=True)
        >>> result = thread.get()

        Args:
            org_id (str): Your company's unique organization ID
            model_id (str): The unique model ID in your company.

        Keyword Args:
            from_epoch (int, none_type): Milli epoch time that represents the end of the time range to query.. [optional]
            to_epoch (int, none_type): Milli epoch time that represents the end of the time range to query.. [optional]
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
            [ReferenceProfileItemResponse]
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
        kwargs['org_id'] = \
            org_id
        kwargs['model_id'] = \
            model_id
        return self.list_reference_profiles_endpoint.call_with_http_info(**kwargs)

