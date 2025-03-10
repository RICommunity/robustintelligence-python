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


class ManagedImagePackageType(str, Enum):
    """
    The type of package manager used to install system packages.   - PACKAGE_TYPE_APT: Specifies packages from the apt package manager available in distributions of Debian Linux.  - PACKAGE_TYPE_ROCKYLINUX: Specifies packages from the yum package manager available in distributions of Rocky Linux.
    """

    """
    allowed enum values
    """
    PACKAGE_TYPE_APT = 'PACKAGE_TYPE_APT'
    PACKAGE_TYPE_ROCKYLINUX = 'PACKAGE_TYPE_ROCKYLINUX'
    PACKAGE_TYPE_UNSPECIFIED = 'PACKAGE_TYPE_UNSPECIFIED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ManagedImagePackageType from a JSON string"""
        return cls(json.loads(json_str))


