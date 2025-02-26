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


class TableColumnType(str, Enum):
    """
     - TABLE_COLUMN_TYPE_PICKABLE: Used for columns that support selection, including multi-selection.
    """

    """
    allowed enum values
    """
    TABLE_COLUMN_TYPE_STRING = 'TABLE_COLUMN_TYPE_STRING'
    TABLE_COLUMN_TYPE_NUMERICAL = 'TABLE_COLUMN_TYPE_NUMERICAL'
    TABLE_COLUMN_TYPE_DATE = 'TABLE_COLUMN_TYPE_DATE'
    TABLE_COLUMN_TYPE_PICKABLE = 'TABLE_COLUMN_TYPE_PICKABLE'
    TABLE_COLUMN_TYPE_UNSPECIFIED = 'TABLE_COLUMN_TYPE_UNSPECIFIED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TableColumnType from a JSON string"""
        return cls(json.loads(json_str))


