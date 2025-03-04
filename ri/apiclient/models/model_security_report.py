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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ri.apiclient.models.securitydb_file_scan_result import SecuritydbFileScanResult
from ri.apiclient.models.securitydb_repo_metadata import SecuritydbRepoMetadata
from typing import Optional, Set
from typing_extensions import Self

class ModelSecurityReport(BaseModel):
    """
    ModelSecurityReport
    """ # noqa: E501
    repo_id: Optional[StrictStr] = Field(default=None, description="The ID of the model repository on Hugging Face.", alias="repoId")
    description: Optional[StrictStr] = Field(default=None, description="Description of the availability of the security report such as 'Scan completed' or 'Scan in progress. Please check back later for results'.")
    repo_metadata: Optional[SecuritydbRepoMetadata] = Field(default=None, alias="repoMetadata")
    file_scan_result: Optional[SecuritydbFileScanResult] = Field(default=None, alias="fileScanResult")
    __properties: ClassVar[List[str]] = ["repoId", "description", "repoMetadata", "fileScanResult"]

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
        """Create an instance of ModelSecurityReport from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of repo_metadata
        if self.repo_metadata:
            _dict['repoMetadata'] = self.repo_metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of file_scan_result
        if self.file_scan_result:
            _dict['fileScanResult'] = self.file_scan_result.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ModelSecurityReport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "repoId": obj.get("repoId"),
            "description": obj.get("description"),
            "repoMetadata": SecuritydbRepoMetadata.from_dict(obj["repoMetadata"]) if obj.get("repoMetadata") is not None else None,
            "fileScanResult": SecuritydbFileScanResult.from_dict(obj["fileScanResult"]) if obj.get("fileScanResult") is not None else None
        })
        return _obj


