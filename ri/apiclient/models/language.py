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
import json
from enum import Enum
from typing_extensions import Self


class Language(str, Enum):
    """
    Language for generative language tasks.  User facing strings should match their ISO 639-1 code. See https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes for more details.   - LANGUAGE_EN: We use EN as the default value because prior to 2.10 we didn't have a language option  for generative testing, and we implicity assumed english was the language. By making EN the default we ensure these previous versions are compatible, and will default to using EN correctly. protolint:disable:next ENUM_FIELD_NAMES_ZERO_VALUE_END_WITH
    """

    """
    allowed enum values
    """
    LANGUAGE_EN = 'LANGUAGE_EN'
    LANGUAGE_JA = 'LANGUAGE_JA'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Language from a JSON string"""
        return cls(json.loads(json_str))


