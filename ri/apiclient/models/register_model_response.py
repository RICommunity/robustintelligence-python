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
from typing import Optional, Set
from typing_extensions import Self

class RegisterModelResponse(BaseModel):
    """
    RegisterModelResponse
    """ # noqa: E501
    model_id: Optional[ID] = Field(default=None, alias="modelId")
    registry_validation_job_id: Optional[ID] = Field(default=None, alias="registryValidationJobId")
    __properties: ClassVar[List[str]] = ["modelId", "registryValidationJobId"]

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
        """Create an instance of RegisterModelResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of model_id
        if self.model_id:
            _dict['modelId'] = self.model_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of registry_validation_job_id
        if self.registry_validation_job_id:
            _dict['registryValidationJobId'] = self.registry_validation_job_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RegisterModelResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "modelId": ID.from_dict(obj["modelId"]) if obj.get("modelId") is not None else None,
            "registryValidationJobId": ID.from_dict(obj["registryValidationJobId"]) if obj.get("registryValidationJobId") is not None else None
        })
        return _obj


