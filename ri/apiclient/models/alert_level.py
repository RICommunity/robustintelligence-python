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


class AlertLevel(str, Enum):
    """
    AlertLevel allows users to configure their desired notification sensitivity. Low severity degradation events will only trigger notifications for the WARNING_AND_ALERTS level.   - ALERT_LEVEL_WARNINGS_AND_ALERTS: Receive notifications when there are events with Warning or Alert severity.  - ALERT_LEVEL_ONLY_ALERTS: Only receive notifications when there are events with Alert severity.
    """

    """
    allowed enum values
    """
    ALERT_LEVEL_WARNINGS_AND_ALERTS = 'ALERT_LEVEL_WARNINGS_AND_ALERTS'
    ALERT_LEVEL_ONLY_ALERTS = 'ALERT_LEVEL_ONLY_ALERTS'
    ALERT_LEVEL_UNSPECIFIED = 'ALERT_LEVEL_UNSPECIFIED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AlertLevel from a JSON string"""
        return cls(json.loads(json_str))


