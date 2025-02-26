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


class LicenseLimit(str, Enum):
    """
    LicenseLimit contains all feature flags to enforce limit as an int.   - LICENSE_LIMIT_EXPIRATION: A UNIX timestamp that specifies the expiration date of the license.  - LICENSE_LIMIT_STRESS_TEST_RUNS: The number of stress tests run to date and the total number of stress tests enabled by the license.  - LICENSE_LIMIT_FIREWALL: The number of firewalls created and the total number of firewalls enabled by the license.  - LICENSE_LIMIT_WORKSPACES: The number of workspaces enabled by the license.  - LICENSE_LIMIT_FIREWALL_REQUESTS: The number of firewall requets allowed by the license.
    """

    """
    allowed enum values
    """
    LICENSE_LIMIT_EXPIRATION = 'LICENSE_LIMIT_EXPIRATION'
    LICENSE_LIMIT_STRESS_TEST_RUNS = 'LICENSE_LIMIT_STRESS_TEST_RUNS'
    LICENSE_LIMIT_FIREWALL = 'LICENSE_LIMIT_FIREWALL'
    LICENSE_LIMIT_WORKSPACES = 'LICENSE_LIMIT_WORKSPACES'
    LICENSE_LIMIT_FIREWALL_REQUESTS = 'LICENSE_LIMIT_FIREWALL_REQUESTS'
    LICENSE_LIMIT_UNSPECIFIED = 'LICENSE_LIMIT_UNSPECIFIED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LicenseLimit from a JSON string"""
        return cls(json.loads(json_str))


