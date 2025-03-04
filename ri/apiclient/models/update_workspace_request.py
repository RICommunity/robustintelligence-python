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
from ri.apiclient.models.update_workspace_request_workspace import UpdateWorkspaceRequestWorkspace
from ri.apiclient.models.workspace_write_mask import WorkspaceWriteMask
from typing import Optional, Set
from typing_extensions import Self

class UpdateWorkspaceRequest(BaseModel):
    """
    UpdateWorkspaceRequest
    """ # noqa: E501
    workspace: Optional[UpdateWorkspaceRequestWorkspace] = None
    workspace_write_mask: Optional[WorkspaceWriteMask] = Field(default=None, alias="workspaceWriteMask")
    __properties: ClassVar[List[str]] = ["workspace", "workspaceWriteMask"]

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
        """Create an instance of UpdateWorkspaceRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of workspace
        if self.workspace:
            _dict['workspace'] = self.workspace.to_dict()
        # override the default output from pydantic by calling `to_dict()` of workspace_write_mask
        if self.workspace_write_mask:
            _dict['workspaceWriteMask'] = self.workspace_write_mask.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateWorkspaceRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "workspace": UpdateWorkspaceRequestWorkspace.from_dict(obj["workspace"]) if obj.get("workspace") is not None else None,
            "workspaceWriteMask": WorkspaceWriteMask.from_dict(obj["workspaceWriteMask"]) if obj.get("workspaceWriteMask") is not None else None
        })
        return _obj


