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


class RiskCategoryType(str, Enum):
    """
    Specifies the type of risk a Monitor is evaluating. RISK_CATEGORY_TYPE_OPERATIONAL_HEALTH, and RISK_CATEGORY_TYPE_ETHICAL_RISK only support `MetricDegradationConfig` monitors while RISK_CATEGORY_TYPE_SECURITY_RISK only supports `AnomalyConfig` monitors.
    """

    """
    allowed enum values
    """
    RISK_CATEGORY_TYPE_OPERATIONAL_HEALTH = 'RISK_CATEGORY_TYPE_OPERATIONAL_HEALTH'
    RISK_CATEGORY_TYPE_ETHICAL_RISK = 'RISK_CATEGORY_TYPE_ETHICAL_RISK'
    RISK_CATEGORY_TYPE_SECURITY_RISK = 'RISK_CATEGORY_TYPE_SECURITY_RISK'
    RISK_CATEGORY_TYPE_CUSTOM = 'RISK_CATEGORY_TYPE_CUSTOM'
    RISK_CATEGORY_TYPE_UNSPECIFIED = 'RISK_CATEGORY_TYPE_UNSPECIFIED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RiskCategoryType from a JSON string"""
        return cls(json.loads(json_str))


