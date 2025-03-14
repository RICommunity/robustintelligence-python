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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from ri.apiclient.models.excluded_transforms import ExcludedTransforms
from ri.apiclient.models.threshold import Threshold
from typing import Optional, Set
from typing_extensions import Self

class TestCaseMonitorInfo(BaseModel):
    """
    TestCaseMonitorInfo
    """ # noqa: E501
    threshold: Optional[Threshold] = None
    is_subset_metric: Optional[StrictBool] = Field(default=None, alias="isSubsetMetric")
    excluded_transforms: Optional[ExcludedTransforms] = Field(default=None, alias="excludedTransforms")
    __properties: ClassVar[List[str]] = ["threshold", "isSubsetMetric", "excludedTransforms"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TestCaseMonitorInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of threshold
        if self.threshold:
            _dict['threshold'] = self.threshold.to_dict()
        # override the default output from pydantic by calling `to_dict()` of excluded_transforms
        if self.excluded_transforms:
            _dict['excludedTransforms'] = self.excluded_transforms.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TestCaseMonitorInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "threshold": Threshold.from_dict(obj["threshold"]) if obj.get("threshold") is not None else None,
            "isSubsetMetric": obj.get("isSubsetMetric"),
            "excludedTransforms": ExcludedTransforms.from_dict(obj["excludedTransforms"]) if obj.get("excludedTransforms") is not None else None
        })
        return _obj


