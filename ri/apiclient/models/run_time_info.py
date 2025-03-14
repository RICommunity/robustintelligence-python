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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ri.apiclient.models.custom_image_type import CustomImageType
from ri.apiclient.models.resource_request import ResourceRequest
from typing import Optional, Set
from typing_extensions import Self

class RunTimeInfo(BaseModel):
    """
    Configures run-time details about how a job should be run.
    """ # noqa: E501
    custom_image: Optional[CustomImageType] = Field(default=None, alias="customImage")
    resource_request: Optional[ResourceRequest] = Field(default=None, alias="resourceRequest")
    explicit_errors: Optional[StrictBool] = Field(default=None, description="Specifies whether the job will return silent errors. By default, this is set to false, and silent errors are not returned.", alias="explicitErrors")
    random_seed: Optional[StrictStr] = Field(default=None, description="Random seed to use for the Job, so that Test Job result will be deterministic.", alias="randomSeed")
    __properties: ClassVar[List[str]] = ["customImage", "resourceRequest", "explicitErrors", "randomSeed"]

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
        """Create an instance of RunTimeInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of custom_image
        if self.custom_image:
            _dict['customImage'] = self.custom_image.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resource_request
        if self.resource_request:
            _dict['resourceRequest'] = self.resource_request.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RunTimeInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "customImage": CustomImageType.from_dict(obj["customImage"]) if obj.get("customImage") is not None else None,
            "resourceRequest": ResourceRequest.from_dict(obj["resourceRequest"]) if obj.get("resourceRequest") is not None else None,
            "explicitErrors": obj.get("explicitErrors"),
            "randomSeed": obj.get("randomSeed")
        })
        return _obj


