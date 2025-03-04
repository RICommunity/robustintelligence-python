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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ri.apiclient.models.column_type_info import ColumnTypeInfo
from ri.apiclient.models.feature_relationship_info import FeatureRelationshipInfo
from typing import Optional, Set
from typing_extensions import Self

class DataProfiling(BaseModel):
    """
    Specifies configuration values for profiling a dataset.
    """ # noqa: E501
    num_quantiles: Optional[StrictStr] = Field(default=None, description="The number of quantiles to split numeric subsets into.", alias="numQuantiles")
    num_subsets: Optional[StrictStr] = Field(default=None, description="The number of subsets to test. This field is sorted by count.", alias="numSubsets")
    column_type_info: Optional[ColumnTypeInfo] = Field(default=None, alias="columnTypeInfo")
    feature_relationship_info: Optional[FeatureRelationshipInfo] = Field(default=None, alias="featureRelationshipInfo")
    __properties: ClassVar[List[str]] = ["numQuantiles", "numSubsets", "columnTypeInfo", "featureRelationshipInfo"]

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
        """Create an instance of DataProfiling from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of column_type_info
        if self.column_type_info:
            _dict['columnTypeInfo'] = self.column_type_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of feature_relationship_info
        if self.feature_relationship_info:
            _dict['featureRelationshipInfo'] = self.feature_relationship_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataProfiling from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "numQuantiles": obj.get("numQuantiles"),
            "numSubsets": obj.get("numSubsets"),
            "columnTypeInfo": ColumnTypeInfo.from_dict(obj["columnTypeInfo"]) if obj.get("columnTypeInfo") is not None else None,
            "featureRelationshipInfo": FeatureRelationshipInfo.from_dict(obj["featureRelationshipInfo"]) if obj.get("featureRelationshipInfo") is not None else None
        })
        return _obj


