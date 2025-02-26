# coding: utf-8

"""
    Robust Intelligence Firewall REST API

    API methods for Robust Intelligence. Users must authenticate using the `X-Firewall-Auth-Token` header. Your AI Firewall Agent domain forms the base of the URL for REST API calls. To find the Agent domain in the Robust Intelligence UI, click AI Firewall: Settings icon: Firewall Settings. Find your agent in the Firewall Agent Status: Agents Setup page, and copy its URL from the table.

    The version of the OpenAPI document: 1.0
    Contact: dev@robustintelligence.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from ri.fwclient.models.flagged_substring import FlaggedSubstring
from ri.fwclient.models.pii_entity_type import PiiEntityType
from typing import Optional, Set
from typing_extensions import Self

class FlaggedEntity(BaseModel):
    """
    FlaggedEntity
    """ # noqa: E501
    entity_type: Optional[PiiEntityType] = None
    custom_entity_name: Optional[StrictStr] = Field(default=None, description="Custom entity name is the name of the custom-defined entity that was detected for this substring, if applicable.", alias="customEntityName")
    flagged_substring: Optional[FlaggedSubstring] = Field(default=None, alias="flaggedSubstring")
    confidence_score: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Confidence score is a metric of how confident (on a scale of 0-1) the rule is about this entity being flagged.", alias="confidenceScore")
    __properties: ClassVar[List[str]] = ["entityType", "customEntityName", "flaggedSubstring", "confidenceScore"]

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
        """Create an instance of FlaggedEntity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of flagged_substring
        if self.flagged_substring:
            _dict['flaggedSubstring'] = self.flagged_substring.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FlaggedEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "entityType": obj.get("entityType"),
            "customEntityName": obj.get("customEntityName"),
            "flaggedSubstring": FlaggedSubstring.from_dict(obj["flaggedSubstring"]) if obj.get("flaggedSubstring") is not None else None,
            "confidenceScore": obj.get("confidenceScore")
        })
        return _obj


