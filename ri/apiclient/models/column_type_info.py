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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ColumnTypeInfo(BaseModel):
    """
    Specifies configuration values for column types.
    """ # noqa: E501
    min_nunique_for_numeric: Optional[StrictStr] = Field(default=None, description="Specifies a minimum number of unique values in a column. Columns with at least the specified number of unique values are considered numeric columns. Columns with fewer unique values are considered categorical.", alias="minNuniqueForNumeric")
    numeric_violation_threshold: Optional[Union[Annotated[float, Field(le=1, strict=True)], Annotated[int, Field(le=1, strict=True)]]] = Field(default=None, description="Maximum fraction of violations when assigning numeric columns (not including missing values).", alias="numericViolationThreshold")
    categorical_violation_threshold: Optional[Union[Annotated[float, Field(le=1, strict=True)], Annotated[int, Field(le=1, strict=True)]]] = Field(default=None, description="Maximum fraction of violations when assigning categorical subtypes (not including missing values).", alias="categoricalViolationThreshold")
    min_unique_prop: Optional[Union[Annotated[float, Field(le=1, strict=True)], Annotated[int, Field(le=1, strict=True)]]] = Field(default=None, description="If data has at least min_unique_prop proportion of unique values then classify as a column that must have unique values.", alias="minUniqueProp")
    allow_float_unique: Optional[StrictBool] = Field(default=None, description="Allow float columns to be inferred as unique values.", alias="allowFloatUnique")
    numeric_range_inference_threshold: Optional[Union[Annotated[float, Field(le=1, strict=True)], Annotated[int, Field(le=1, strict=True)]]] = Field(default=None, description="The percent of non-null values which must fall within an inferrable numeric range ([0,1], [0,inf), (-inf, inf)) for that to be inferred as the valid range for a numeric column. If 1.0 (default), then all non-null values must fall within the range for that range to be inferred. For ex: if 98% of feature X falls in [0, 1] but 100% of feature X falls in [0, inf) then we'll infer [0, inf) as the valid range for feature X. However, if this threshold is 0.98, we'll instead infer [0, 1] as feature X's range.", alias="numericRangeInferenceThreshold")
    unseen_values_allowed_criteria: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Either the fraction or count of unique values in the ref set required to infer that a categorical feature is allowed to have unseen values in the eval set. If the criteria is provided as a float in [0.0, 1.0] it will be treated as the fraction of unique non-null values divided by the total number of non-null values required to infer that unseen values are allowed. If provided as an integer in [2, inf), it will be treated as the count of non-null unique values required to infer that unseen values are allowed.", alias="unseenValuesAllowedCriteria")
    __properties: ClassVar[List[str]] = ["minNuniqueForNumeric", "numericViolationThreshold", "categoricalViolationThreshold", "minUniqueProp", "allowFloatUnique", "numericRangeInferenceThreshold", "unseenValuesAllowedCriteria"]

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
        """Create an instance of ColumnTypeInfo from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ColumnTypeInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "minNuniqueForNumeric": obj.get("minNuniqueForNumeric"),
            "numericViolationThreshold": obj.get("numericViolationThreshold"),
            "categoricalViolationThreshold": obj.get("categoricalViolationThreshold"),
            "minUniqueProp": obj.get("minUniqueProp"),
            "allowFloatUnique": obj.get("allowFloatUnique"),
            "numericRangeInferenceThreshold": obj.get("numericRangeInferenceThreshold"),
            "unseenValuesAllowedCriteria": obj.get("unseenValuesAllowedCriteria")
        })
        return _obj


