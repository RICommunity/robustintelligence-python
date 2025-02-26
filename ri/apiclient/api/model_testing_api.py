# coding: utf-8

"""
    Robust Intelligence REST API

    API methods for Robust Intelligence. Users must authenticate using the `rime-api-key` header.

    The version of the OpenAPI document: 1.0
    Contact: dev@robustintelligence.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501
import warnings
from datetime import datetime
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr
from typing_extensions import Annotated
from ri.apiclient.models.start_continuous_test_request import StartContinuousTestRequest
from ri.apiclient.models.start_continuous_test_response import StartContinuousTestResponse
from ri.apiclient.models.start_file_scan_request import StartFileScanRequest
from ri.apiclient.models.start_file_scan_response import StartFileScanResponse
from ri.apiclient.models.start_stress_test_request import StartStressTestRequest
from ri.apiclient.models.start_stress_test_response import StartStressTestResponse

from ri.apiclient.models import *
from ri.apiclient.api_client import ApiClient, RequestSerialized
from ri.apiclient.api_response import ApiResponse
from ri.apiclient.rest import RESTResponseType


class ModelTestingApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def start_continuous_test(
        self,
        firewall_id_uuid: str,
        firewall_id: Optional[object] = None,
        test_run_incremental_config: Optional[TestRunIncrementalConfig] = None,
        override_existing_bins: Optional[bool] = None,
        agent_id: Optional[ID] = None,
        experimental_fields: Optional[Dict[str, object]] = None,
    ) -> StartContinuousTestResponse:
        """StartContinuousTest

        Starts a Continuous Test and returns a Job object containing metadata for the Test Run.

        :param firewall_id_uuid: Unique object ID. (required)
        :type firewall_id_uuid: str
        :param firewall_id: Uniquely specifies a Firewall.
        :type firewall_id: object
        :param test_run_incremental_config:
        :type test_run_incremental_config: TestRunIncrementalConfig
        :param override_existing_bins:
        :type override_existing_bins: bool
        :param agent_id:
        :type agent_id: ID
        :param experimental_fields: Fields that enable experimental functionality.  WARNING: these fields are experimental; ie, their functionality may not be reliable or backwards-compatible. Do not use these fields in production.
        :type experimental_fields: Dict[str, object]
        :return: Returns the result object.
        """ # noqa: E501

        body = StartContinuousTestRequest(
          firewall_id=firewall_id,
          test_run_incremental_config=test_run_incremental_config,
          override_existing_bins=override_existing_bins,
          agent_id=agent_id,
          experimental_fields=experimental_fields,
        )

        _param = self._start_continuous_test_serialize(
            firewall_id_uuid=firewall_id_uuid,
            body=body,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "StartContinuousTestResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _start_continuous_test_serialize(
        self,
        firewall_id_uuid,
        body,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        if firewall_id_uuid is not None:
            _path_params['firewallId.uuid'] = firewall_id_uuid
        if body is not None:
            _body_params = body
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )

        _default_content_type = (
            self.api_client.select_header_content_type(
                [
                    'application/json'
                ]
            )
        )
        if _default_content_type is not None:
            _header_params['Content-Type'] = _default_content_type

        _auth_settings: List[str] = [
            'rime-api-key'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/v1/continuous-tests/{firewallId.uuid}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
        )

    @validate_call
    def start_file_scan(
        self,
        project_id: ID,
        model_id: ID,
        run_time_info: Optional[RunTimeInfo] = None,
        agent_id: Optional[ID] = None,
    ) -> StartFileScanResponse:
        """StartFileScan

        Starts a File Scan for the specified model.

        :param project_id: (required)
        :type project_id: ID
        :param model_id: (required)
        :type model_id: ID
        :param run_time_info:
        :type run_time_info: RunTimeInfo
        :param agent_id:
        :type agent_id: ID
        :return: Returns the result object.
        """ # noqa: E501

        body = StartFileScanRequest(
          project_id=project_id,
          model_id=model_id,
          run_time_info=run_time_info,
          agent_id=agent_id,
        )

        _param = self._start_file_scan_serialize(
            body=body,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "StartFileScanResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _start_file_scan_serialize(
        self,
        body,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        if body is not None:
            _body_params = body
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )

        _default_content_type = (
            self.api_client.select_header_content_type(
                [
                    'application/json'
                ]
            )
        )
        if _default_content_type is not None:
            _header_params['Content-Type'] = _default_content_type

        _auth_settings: List[str] = [
            'rime-api-key'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/v1/file-scans',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
        )

    @validate_call
    def start_file_scan2(
        self,
        project_id: ID,
        model_id: ID,
        run_time_info: Optional[RunTimeInfo] = None,
        agent_id: Optional[ID] = None,
    ) -> StartFileScanResponse:
        """StartFileScan

        Starts a File Scan for the specified model.

        :param project_id: (required)
        :type project_id: ID
        :param model_id: (required)
        :type model_id: ID
        :param run_time_info:
        :type run_time_info: RunTimeInfo
        :param agent_id:
        :type agent_id: ID
        :return: Returns the result object.
        """ # noqa: E501

        body = StartFileScanRequest(
          project_id=project_id,
          model_id=model_id,
          run_time_info=run_time_info,
          agent_id=agent_id,
        )

        _param = self._start_file_scan2_serialize(
            body=body,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "StartFileScanResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _start_file_scan2_serialize(
        self,
        body,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        if body is not None:
            _body_params = body
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )

        _default_content_type = (
            self.api_client.select_header_content_type(
                [
                    'application/json'
                ]
            )
        )
        if _default_content_type is not None:
            _header_params['Content-Type'] = _default_content_type

        _auth_settings: List[str] = [
            'rime-api-key'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/v1-beta/file-scans',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
        )

    @validate_call
    def start_stress_test(
        self,
        project_id_uuid: str,
        project_id: Optional[object] = None,
        test_run_config: Optional[TestRunConfig] = None,
        agent_id: Optional[ID] = None,
        experimental_fields: Optional[Dict[str, object]] = None,
    ) -> StartStressTestResponse:
        """StartStressTest

        Starts a Stress Test and returns a Job object containing metadata for the Test Run.

        :param project_id_uuid: Unique object ID. (required)
        :type project_id_uuid: str
        :param project_id: Uniquely specifies a Project.
        :type project_id: object
        :param test_run_config:
        :type test_run_config: TestRunConfig
        :param agent_id:
        :type agent_id: ID
        :param experimental_fields: Fields that enable experimental functionality.  WARNING: these fields are experimental; ie, their functionality may not be reliable or backwards-compatible. Do not use these fields in production.
        :type experimental_fields: Dict[str, object]
        :return: Returns the result object.
        """ # noqa: E501

        body = StartStressTestRequest(
          project_id=project_id,
          test_run_config=test_run_config,
          agent_id=agent_id,
          experimental_fields=experimental_fields,
        )

        _param = self._start_stress_test_serialize(
            project_id_uuid=project_id_uuid,
            body=body,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "StartStressTestResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _start_stress_test_serialize(
        self,
        project_id_uuid,
        body,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        if project_id_uuid is not None:
            _path_params['projectId.uuid'] = project_id_uuid
        if body is not None:
            _body_params = body
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )

        _default_content_type = (
            self.api_client.select_header_content_type(
                [
                    'application/json'
                ]
            )
        )
        if _default_content_type is not None:
            _header_params['Content-Type'] = _default_content_type

        _auth_settings: List[str] = [
            'rime-api-key'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/v1/stress-tests/{projectId.uuid}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
        )
