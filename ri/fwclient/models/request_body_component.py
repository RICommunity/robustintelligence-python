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
import json
from enum import Enum
from typing_extensions import Self


class RequestBodyComponent(str, Enum):
    """
    RequestBodyComponent
    """

    """
    allowed enum values
    """
    REQUEST_BODY_COMPONENT_UNSPECIFIED = 'REQUEST_BODY_COMPONENT_UNSPECIFIED'
    REQUEST_BODY_COMPONENT_USER_INPUT = 'REQUEST_BODY_COMPONENT_USER_INPUT'
    REQUEST_BODY_COMPONENT_CONTEXTS = 'REQUEST_BODY_COMPONENT_CONTEXTS'
    REQUEST_BODY_COMPONENT_OUTPUT = 'REQUEST_BODY_COMPONENT_OUTPUT'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RequestBodyComponent from a JSON string"""
        return cls(json.loads(json_str))


