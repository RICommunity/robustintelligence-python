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
from ri.apiclient.models.filters import Filters
from ri.apiclient.models.language import Language
from ri.apiclient.models.model_connection_spec import ModelConnectionSpec
from ri.apiclient.models.prompt_bank import PromptBank
from typing import Optional, Set
from typing_extensions import Self

class GenerativeValidationConfig(BaseModel):
    """
    GenerativeValidationConfig is the configuration to run a generative model test.
    """ # noqa: E501
    prompt_bank: Optional[PromptBank] = None
    system_prompt: Optional[StrictStr] = Field(default=None, description="The system prompt that is currently active on the provided endpoint. If this is not set, system prompt extraction tests will be skipped.", alias="systemPrompt")
    connection: Optional[ModelConnectionSpec] = None
    model_output_is_sensitive: Optional[StrictBool] = Field(default=None, description="Will not be saved to the database, logged in plaintext, etc.", alias="modelOutputIsSensitive")
    filters: Optional[Filters] = None
    language: Optional[Language] = None
    __properties: ClassVar[List[str]] = ["promptBank", "systemPrompt", "connection", "modelOutputIsSensitive", "filters", "language"]

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
        """Create an instance of GenerativeValidationConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of connection
        if self.connection:
            _dict['connection'] = self.connection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of filters
        if self.filters:
            _dict['filters'] = self.filters.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GenerativeValidationConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "promptBank": obj.get("promptBank"),
            "systemPrompt": obj.get("systemPrompt"),
            "connection": ModelConnectionSpec.from_dict(obj["connection"]) if obj.get("connection") is not None else None,
            "modelOutputIsSensitive": obj.get("modelOutputIsSensitive"),
            "filters": Filters.from_dict(obj["filters"]) if obj.get("filters") is not None else None,
            "language": obj.get("language")
        })
        return _obj


