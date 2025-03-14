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
from ri.apiclient.models.create_model_card_request import CreateModelCardRequest
from ri.apiclient.models.create_model_card_response import CreateModelCardResponse
from ri.apiclient.models.delete_model_card_response import DeleteModelCardResponse
from ri.apiclient.models.get_model_card_response import GetModelCardResponse
from ri.apiclient.models.list_model_cards_response import ListModelCardsResponse
from ri.apiclient.models.update_model_card_request import UpdateModelCardRequest
from ri.apiclient.models.update_model_card_response import UpdateModelCardResponse

from ri.apiclient.models import *
from ri.apiclient.api_client import ApiClient, RequestSerialized
from ri.apiclient.api_response import ApiResponse
from ri.apiclient.rest import RESTResponseType


class ModelCardServiceApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def create_model_card(
        self,
        model_card: Optional[ModelCard] = None,
        project_id: Optional[ID] = None,
    ) -> CreateModelCardResponse:
        """CreateModelCard

        Create a new Model Card.

        :param model_card:
        :type model_card: ModelCard
        :param project_id:
        :type project_id: ID
        :return: Returns the result object.
        """ # noqa: E501

        body = CreateModelCardRequest(
          model_card=model_card,
          project_id=project_id,
        )

        _param = self._create_model_card_serialize(
            body=body,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "CreateModelCardResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _create_model_card_serialize(
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
            resource_path='/v1-beta/modelcards',
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
    def delete_model_card(
        self,
        model_card_id_uuid: str,
    ) -> DeleteModelCardResponse:
        """DeleteModelCard

        Delete Model Card.

        :param model_card_id_uuid: Unique object ID. (required)
        :type model_card_id_uuid: str
        :return: Returns the result object.
        """ # noqa: E501


        _param = self._delete_model_card_serialize(
            model_card_id_uuid=model_card_id_uuid,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "DeleteModelCardResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _delete_model_card_serialize(
        self,
        model_card_id_uuid,
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

        if model_card_id_uuid is not None:
            _path_params['modelCardId.uuid'] = model_card_id_uuid
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        _auth_settings: List[str] = [
            'rime-api-key'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/v1-beta/modelcards/{modelCardId.uuid}',
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
    def get_model_card(
        self,
        model_card_id_uuid: str,
    ) -> GetModelCardResponse:
        """GetModelCard

        Get Model Card By ID.

        :param model_card_id_uuid: Unique object ID. (required)
        :type model_card_id_uuid: str
        :return: Returns the result object.
        """ # noqa: E501


        _param = self._get_model_card_serialize(
            model_card_id_uuid=model_card_id_uuid,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetModelCardResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _get_model_card_serialize(
        self,
        model_card_id_uuid,
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

        if model_card_id_uuid is not None:
            _path_params['modelCardId.uuid'] = model_card_id_uuid
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        _auth_settings: List[str] = [
            'rime-api-key'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1-beta/modelcards/{modelCardId.uuid}',
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
    def list_model_cards(
        self,
        project_id: str,
    ) -> ListModelCardsResponse:
        """ListModelCards

        List Model Cards by Project.

        :param project_id: Uniquely specifies a Project.  List queries are kept as strings as they are used in query  parameters. (required)
        :type project_id: str
        :return: Returns the result object.
        """ # noqa: E501


        _param = self._list_model_cards_serialize(
            project_id=project_id,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListModelCardsResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _list_model_cards_serialize(
        self,
        project_id,
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

        if project_id is not None:
            _path_params['projectId'] = project_id
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        _auth_settings: List[str] = [
            'rime-api-key'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1-beta/modelcards/projects/{projectId}',
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
    def update_model_card(
        self,
        model_card_model_card_id_uuid: str,
        model_card: Optional[UpdateModelCardRequestModelCard] = None,
    ) -> UpdateModelCardResponse:
        """UpdateModelCard

        Update Model Card by ID.

        :param model_card_model_card_id_uuid: Unique object ID. (required)
        :type model_card_model_card_id_uuid: str
        :param model_card:
        :type model_card: UpdateModelCardRequestModelCard
        :return: Returns the result object.
        """ # noqa: E501

        body = UpdateModelCardRequest(
          model_card=model_card,
        )

        _param = self._update_model_card_serialize(
            model_card_model_card_id_uuid=model_card_model_card_id_uuid,
            body=body,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "UpdateModelCardResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _update_model_card_serialize(
        self,
        model_card_model_card_id_uuid,
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

        if model_card_model_card_id_uuid is not None:
            _path_params['modelCard.modelCardId.uuid'] = model_card_model_card_id_uuid
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
            method='PUT',
            resource_path='/v1-beta/modelcards/{modelCard.modelCardId.uuid}',
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
