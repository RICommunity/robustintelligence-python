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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ri.fwclient.models.rule_sensitivity import RuleSensitivity
from typing import Optional, Set
from typing_extensions import Self

class OffTopicRuleConfig(BaseModel):
    """
    OffTopicRuleConfig
    """ # noqa: E501
    in_domain_intents: Optional[List[StrictStr]] = Field(default=None, description="In_domain_intents is a list of strings that are considered on-topic. Total number of data points in in_domain_intents and restricted_intents should not exceed 500 and total bytes should not exceed 300KB.", alias="inDomainIntents")
    restricted_intents: Optional[List[StrictStr]] = Field(default=None, alias="restrictedIntents")
    in_domain_intents_sensitivity: Optional[RuleSensitivity] = None
    restricted_intents_sensitivity: Optional[RuleSensitivity] = None
    __properties: ClassVar[List[str]] = ["inDomainIntents", "restrictedIntents", "inDomainIntentsSensitivity", "restrictedIntentsSensitivity"]

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
        """Create an instance of OffTopicRuleConfig from a JSON string"""
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
        """Create an instance of OffTopicRuleConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "inDomainIntents": obj.get("inDomainIntents"),
            "restrictedIntents": obj.get("restrictedIntents"),
            "inDomainIntentsSensitivity": obj.get("inDomainIntentsSensitivity"),
            "restrictedIntentsSensitivity": obj.get("restrictedIntentsSensitivity")
        })
        return _obj


