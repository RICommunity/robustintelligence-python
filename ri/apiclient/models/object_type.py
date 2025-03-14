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


class ObjectType(str, Enum):
    """
     - OBJECT_TYPE_PROJECT: Used for notifications associated with an project. The Notification object ID is the Project ID.
    """

    """
    allowed enum values
    """
    OBJECT_TYPE_PROJECT = 'OBJECT_TYPE_PROJECT'
    OBJECT_TYPE_UNSPECIFIED = 'OBJECT_TYPE_UNSPECIFIED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ObjectType from a JSON string"""
        return cls(json.loads(json_str))


