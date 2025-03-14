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


class ReferenceType(str, Enum):
    """
     - REFERENCE_TYPE_RIME_DOCKERHUB: Signifies an external image that is located in Robust Intelligence's Docker Hub repository.  - REFERENCE_TYPE_MANAGED: Signifies an image managed by the managed image registry.  - REFERENCE_TYPE_EXTERNAL_ECR: Signifies an external image located in an ECR repository.  - REFERENCE_TYPE_EXTERNAL_GAR: Signifies an external image located in a GAR repository.
    """

    """
    allowed enum values
    """
    REFERENCE_TYPE_RIME_DOCKERHUB = 'REFERENCE_TYPE_RIME_DOCKERHUB'
    REFERENCE_TYPE_MANAGED = 'REFERENCE_TYPE_MANAGED'
    REFERENCE_TYPE_EXTERNAL_ECR = 'REFERENCE_TYPE_EXTERNAL_ECR'
    REFERENCE_TYPE_EXTERNAL_GAR = 'REFERENCE_TYPE_EXTERNAL_GAR'
    REFERENCE_TYPE_UNSPECIFIED = 'REFERENCE_TYPE_UNSPECIFIED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ReferenceType from a JSON string"""
        return cls(json.loads(json_str))


