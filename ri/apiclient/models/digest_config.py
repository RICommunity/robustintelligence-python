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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from ri.apiclient.models.digest_frequency import DigestFrequency
from typing import Optional, Set
from typing_extensions import Self

class DigestConfig(BaseModel):
    """
    DigestConfig is a configuration for digest notifications. These notifications are helpful for receiving a succinct summary of activity under a given project.
    """ # noqa: E501
    frequency: Optional[DigestFrequency] = None
    hour_offset: Optional[StrictInt] = Field(default=None, description="The offset in the day when the digest starts. The offset is taken in the configured timezone for the workspace. Uses a default value of 08:00 when not provided.", alias="hourOffset")
    last_digest_time: Optional[datetime] = Field(default=None, description="The last time that the RI platform sent the digest. This timestamp is zero when no digests have ever been sent.", alias="lastDigestTime")
    __properties: ClassVar[List[str]] = ["frequency", "hourOffset", "lastDigestTime"]

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
        """Create an instance of DigestConfig from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DigestConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "frequency": obj.get("frequency"),
            "hourOffset": obj.get("hourOffset"),
            "lastDigestTime": obj.get("lastDigestTime")
        })
        return _obj


