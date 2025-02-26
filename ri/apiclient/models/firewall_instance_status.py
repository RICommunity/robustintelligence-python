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


class FirewallInstanceStatus(str, Enum):
    """
    FirewallInstanceStatus
    """

    """
    allowed enum values
    """
    FIREWALL_INSTANCE_STATUS_UNSPECIFIED = 'FIREWALL_INSTANCE_STATUS_UNSPECIFIED'
    FIREWALL_INSTANCE_STATUS_PENDING = 'FIREWALL_INSTANCE_STATUS_PENDING'
    FIREWALL_INSTANCE_STATUS_READY = 'FIREWALL_INSTANCE_STATUS_READY'
    FIREWALL_INSTANCE_STATUS_REDEPLOYING = 'FIREWALL_INSTANCE_STATUS_REDEPLOYING'
    FIREWALL_INSTANCE_STATUS_UNRESPONSIVE = 'FIREWALL_INSTANCE_STATUS_UNRESPONSIVE'
    FIREWALL_INSTANCE_STATUS_REQUESTED = 'FIREWALL_INSTANCE_STATUS_REQUESTED'
    FIREWALL_INSTANCE_STATUS_DELETE_REQUESTED = 'FIREWALL_INSTANCE_STATUS_DELETE_REQUESTED'
    FIREWALL_INSTANCE_STATUS_DELETED = 'FIREWALL_INSTANCE_STATUS_DELETED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FirewallInstanceStatus from a JSON string"""
        return cls(json.loads(json_str))


