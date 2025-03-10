# coding: utf-8

"""
    Robust Intelligence REST API

    API methods for Robust Intelligence. Users must authenticate using the `rime-api-key` header.

    The version of the OpenAPI document: 1.0
    Contact: dev@robustintelligence.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ri.apiclient.models.id import ID
from ri.apiclient.models.run_time_info import RunTimeInfo
from typing import Optional, Set
from typing_extensions import Self

class StartFileScanRequest(BaseModel):
    """
    StartFileScanRequest
    """ # noqa: E501
    project_id: ID = Field(alias="projectId")
    model_id: ID = Field(alias="modelId")
    run_time_info: Optional[RunTimeInfo] = Field(default=None, alias="runTimeInfo")
    agent_id: Optional[ID] = Field(default=None, alias="agentId")
    __properties: ClassVar[List[str]] = ["projectId", "modelId", "runTimeInfo", "agentId"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of StartFileScanRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of project_id
        if self.project_id:
            _dict['projectId'] = self.project_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model_id
        if self.model_id:
            _dict['modelId'] = self.model_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of run_time_info
        if self.run_time_info:
            _dict['runTimeInfo'] = self.run_time_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of agent_id
        if self.agent_id:
            _dict['agentId'] = self.agent_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StartFileScanRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "projectId": ID.from_dict(obj["projectId"]) if obj.get("projectId") is not None else None,
            "modelId": ID.from_dict(obj["modelId"]) if obj.get("modelId") is not None else None,
            "runTimeInfo": RunTimeInfo.from_dict(obj["runTimeInfo"]) if obj.get("runTimeInfo") is not None else None,
            "agentId": ID.from_dict(obj["agentId"]) if obj.get("agentId") is not None else None
        })
        return _obj


