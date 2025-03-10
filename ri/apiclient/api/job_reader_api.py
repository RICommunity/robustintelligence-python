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

from pydantic import Field, StrictStr, field_validator
from typing import Any, Dict, List, Optional
from typing_extensions import Annotated
from ri.apiclient.models.get_job_response import GetJobResponse
from ri.apiclient.models.get_project_id_response import GetProjectIDResponse
from ri.apiclient.models.get_test_run_id_response import GetTestRunIDResponse
from ri.apiclient.models.list_gai_test_job_response import ListGAITestJobResponse
from ri.apiclient.models.list_jobs_for_project_response import ListJobsForProjectResponse

from ri.apiclient.models import *
from ri.apiclient.api_client import ApiClient, RequestSerialized
from ri.apiclient.api_response import ApiResponse
from ri.apiclient.rest import RESTResponseType


class JobReaderApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def cancel_job(
        self,
        job_id: str,
    ) -> object:
        """CancelJob

        Cancels the job with the specified ID.

        :param job_id: Unique job ID of job to be cancelled. (required)
        :type job_id: str
        :return: Returns the result object.
        """ # noqa: E501


        _param = self._cancel_job_serialize(
            job_id=job_id,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
        }
        response_data = self.api_client.call_api(
            *_param,
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _cancel_job_serialize(
        self,
        job_id,
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

        if job_id is not None:
            _path_params['jobId'] = job_id
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        _auth_settings: List[str] = [
            'rime-api-key'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/v1/jobs/cancel/{jobId}',
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
    def get_job(
        self,
        job_id: str,
        view: Optional[str] = None,
    ) -> GetJobResponse:
        """GetJob

        Get a single job by ID.

        :param job_id: Unique job ID (required)
        :type job_id: str
        :param view: Specifies how much information about the job to retrieve. The default behavior is the Basic view.   - JOB_VIEW_BASIC: Server responses only include basic information about the job, including type, status, and some job data.  - JOB_VIEW_FULL: Server responses include all available information about the job, including progress. Has greater performance requirements than the Basic view.
        :type view: str
        :return: Returns the result object.
        """ # noqa: E501


        _param = self._get_job_serialize(
            job_id=job_id,
            view=view,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetJobResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _get_job_serialize(
        self,
        job_id,
        view,
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

        if job_id is not None:
            _path_params['jobId'] = job_id
        if view is not None:
            
            _query_params.append(('view', view))
            
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
            resource_path='/v1/jobs/{jobId}',
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
    def get_project_id(
        self,
        job_id: str,
    ) -> GetProjectIDResponse:
        """GetProjectID

        Returns the project ID of the project running the job with the specified job ID.

        :param job_id: Unique job ID belonging to the project. (required)
        :type job_id: str
        :return: Returns the result object.
        """ # noqa: E501


        _param = self._get_project_id_serialize(
            job_id=job_id,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetProjectIDResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _get_project_id_serialize(
        self,
        job_id,
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

        if job_id is not None:
            _path_params['jobId'] = job_id
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
            resource_path='/v1/jobs/{jobId}/project-id',
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
    def get_test_run_id(
        self,
        job_id: str,
    ) -> GetTestRunIDResponse:
        """GetTestRunID

        Returns a test run ID based on a specified job ID. The job ID must be for a completed stress test job.

        :param job_id: Unique job ID associated with the test run. (required)
        :type job_id: str
        :return: Returns the result object.
        """ # noqa: E501


        _param = self._get_test_run_id_serialize(
            job_id=job_id,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetTestRunIDResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _get_test_run_id_serialize(
        self,
        job_id,
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

        if job_id is not None:
            _path_params['jobId'] = job_id
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
            resource_path='/v1/jobs/{jobId}/test-run-id',
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
    def list_gai_test_job(
        self,
        workspace_id_uuid: str,
        first_page_query_selected_statuses: Optional[List[str]] = None,
        page_token: Optional[str] = None,
        page_size: Optional[str] = None,
        view: Optional[str] = None,
    ) -> ListGAITestJobResponse:
        """ListGAITestJob is a method to list all GAI test jobs for a given workspace.

        They will be sorted in descending order by creation time.

        :param workspace_id_uuid: Unique object ID. (required)
        :type workspace_id_uuid: str
        :param first_page_query_selected_statuses: Specifies a set of statuses. The query only returns results with a status in the specified set. Specify no statuses to return all results.   - JOB_STATUS_PENDING: Resources have been created for the job but the job has not started yet.  - JOB_STATUS_FAILED: Blanket status for user or system-related job failure.  - JOB_STATUS_REQUESTED: The job descriptor exists but has no resources allocated. Jobs that remain in this status without moving to the PENDING status are at risk of entering the FAILED status.  - JOB_STATUS_CANCELLED: Job has been cancelled. Cancelled jobs cannot be recovered.
        :type first_page_query_selected_statuses: List[str]
        :param page_token: The ListJobs query returns a pageToken after the first request.
        :type page_token: str
        :param page_size: The maximum number of Job objects to return in a single page.
        :type page_size: str
        :param view: Specifies how much information about each job to retrieve.   - JOB_VIEW_BASIC: Server responses only include basic information about the job, including type, status, and some job data.  - JOB_VIEW_FULL: Server responses include all available information about the job, including progress. Has greater performance requirements than the Basic view.
        :type view: str
        :return: Returns the result object.
        """ # noqa: E501


        _param = self._list_gai_test_job_serialize(
            workspace_id_uuid=workspace_id_uuid,
            first_page_query_selected_statuses=first_page_query_selected_statuses,
            page_token=page_token,
            page_size=page_size,
            view=view,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListGAITestJobResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _list_gai_test_job_serialize(
        self,
        workspace_id_uuid,
        first_page_query_selected_statuses,
        page_token,
        page_size,
        view,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'firstPageQuery.selectedStatuses': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        if workspace_id_uuid is not None:
            _path_params['workspaceId.uuid'] = workspace_id_uuid
        if first_page_query_selected_statuses is not None:
            
            _query_params.append(('firstPageQuery.selectedStatuses', first_page_query_selected_statuses))
            
        if page_token is not None:
            
            _query_params.append(('pageToken', page_token))
            
        if page_size is not None:
            
            _query_params.append(('pageSize', page_size))
            
        if view is not None:
            
            _query_params.append(('view', view))
            
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
            resource_path='/v1-beta/jobs/generative/workspaces/{workspaceId.uuid}',
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
    def list_jobs_for_project(
        self,
        project_id_uuid: str,
        first_page_query_selected_statuses: Optional[List[str]] = None,
        first_page_query_selected_types: Optional[List[str]] = None,
        page_token: Optional[str] = None,
        page_size: Optional[str] = None,
        view: Optional[str] = None,
    ) -> ListJobsForProjectResponse:
        """ListJobsForProject

        Returns a paginated list of jobs for a given project. The list can be filtered by job type and status.  #### Python pagination example:  ```python all_objects = [] # Required for authentication to all methods in the API. headers = {\"rime-api-key\": \"INSERT_API_TOKEN\"} # TODO page_token = \"\" # Initialize query parameters in a dictionary params = {\"INSERT_QUERY_PARAMETER\": \"INSERT_QUERY_VALUE\"} # TODO # Make requests until all results have been returned. while True:     # If the page_token from a previous response is not empty, we need to specify this     # token as a parameter to the next request in order to return the next page.     if page_token != \"\":         params = {\"page_token\": page_token}     res = requests.get(\"INSERT_METHOD_URI\", params=params, headers=headers) # TODO     if res.status_code != 200 :         raise ValueError(res)     res_json = res.json()     all_objects.extend(res_json['INSERT_OBJECT_KEY']) # TODO     page_token = res_json['nextPageToken']     # If all results have been returned, res_json['hasMore'] is false.     if not res_json[\"hasMore\"]:         break ```

        :param project_id_uuid: Unique object ID. (required)
        :type project_id_uuid: str
        :param first_page_query_selected_statuses: Specifies a set of statuses. The query only returns results with a status in the specified set. Specify no statuses to return all results.   - JOB_STATUS_PENDING: Resources have been created for the job but the job has not started yet.  - JOB_STATUS_FAILED: Blanket status for user or system-related job failure.  - JOB_STATUS_REQUESTED: The job descriptor exists but has no resources allocated. Jobs that remain in this status without moving to the PENDING status are at risk of entering the FAILED status.  - JOB_STATUS_CANCELLED: Job has been cancelled. Cancelled jobs cannot be recovered.
        :type first_page_query_selected_statuses: List[str]
        :param first_page_query_selected_types: Specifies a set of types. The query only returns jobs with types in the specified set. Specify no types to return all results. Job types not tied to projects will not be returned.
        :type first_page_query_selected_types: List[str]
        :param page_token: The ListJobs query returns a pageToken after the first request.
        :type page_token: str
        :param page_size: The maximum number of Job objects to return in a single page.
        :type page_size: str
        :param view: Specifies how much information about each job to retrieve.   - JOB_VIEW_BASIC: Server responses only include basic information about the job, including type, status, and some job data.  - JOB_VIEW_FULL: Server responses include all available information about the job, including progress. Has greater performance requirements than the Basic view.
        :type view: str
        :return: Returns the result object.
        """ # noqa: E501


        _param = self._list_jobs_for_project_serialize(
            project_id_uuid=project_id_uuid,
            first_page_query_selected_statuses=first_page_query_selected_statuses,
            first_page_query_selected_types=first_page_query_selected_types,
            page_token=page_token,
            page_size=page_size,
            view=view,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListJobsForProjectResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _list_jobs_for_project_serialize(
        self,
        project_id_uuid,
        first_page_query_selected_statuses,
        first_page_query_selected_types,
        page_token,
        page_size,
        view,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'firstPageQuery.selectedStatuses': 'multi',
            'firstPageQuery.selectedTypes': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        if project_id_uuid is not None:
            _path_params['projectId.uuid'] = project_id_uuid
        if first_page_query_selected_statuses is not None:
            
            _query_params.append(('firstPageQuery.selectedStatuses', first_page_query_selected_statuses))
            
        if first_page_query_selected_types is not None:
            
            _query_params.append(('firstPageQuery.selectedTypes', first_page_query_selected_types))
            
        if page_token is not None:
            
            _query_params.append(('pageToken', page_token))
            
        if page_size is not None:
            
            _query_params.append(('pageSize', page_size))
            
        if view is not None:
            
            _query_params.append(('view', view))
            
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
            resource_path='/v1/jobs/project/{projectId.uuid}',
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
