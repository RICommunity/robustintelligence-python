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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from ri.apiclient.models.rime_severity import RimeSeverity
from ri.apiclient.models.test_case_display import TestCaseDisplay
from ri.apiclient.models.test_case_status import TestCaseStatus
from ri.apiclient.models.test_category_type import TestCategoryType
from ri.apiclient.models.test_metric import TestMetric
from typing import Optional, Set
from typing_extensions import Self

class TestCase(BaseModel):
    """
    TestCase returns information for a given test case.
    """ # noqa: E501
    test_run_id: Optional[StrictStr] = Field(default=None, description="Uniquely specifies a Test Run.", alias="testRunId")
    features: Optional[List[StrictStr]] = Field(default=None, description="The list of features used in the test case.")
    test_batch_type: Optional[StrictStr] = Field(default=None, description="The type of test batch.", alias="testBatchType")
    status: Optional[TestCaseStatus] = None
    severity: Optional[RimeSeverity] = None
    importance_score: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The model impact of the test case.", alias="importanceScore")
    test_category: Optional[TestCategoryType] = None
    category: Optional[StrictStr] = Field(default=None, description="The string field `category` is deprecated in v2.1 and will be removed in v2.3. Please use the enum field test_category instead, which provides the same info.")
    metrics: Optional[List[TestMetric]] = None
    url_safe_feature_id: Optional[StrictStr] = Field(default=None, description="Optional URL-safe feature ID if the test case is associated with a feature. This may be empty for modalities that do not have features or test cases that pertain to two or more features, such as subset tests.", alias="urlSafeFeatureId")
    test_case_id: Optional[StrictStr] = Field(default=None, description="Together with the Test Run ID and the test batch type, this forms the primary key for the test case.", alias="testCaseId")
    display: Optional[TestCaseDisplay] = None
    __properties: ClassVar[List[str]] = ["testRunId", "features", "testBatchType", "status", "severity", "importanceScore", "testCategory", "category", "metrics", "urlSafeFeatureId", "testCaseId", "display"]

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
        """Create an instance of TestCase from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in metrics (list)
        _items = []
        if self.metrics:
            for _item in self.metrics:
                if _item:
                    _items.append(_item.to_dict())
            _dict['metrics'] = _items
        # override the default output from pydantic by calling `to_dict()` of display
        if self.display:
            _dict['display'] = self.display.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TestCase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "testRunId": obj.get("testRunId"),
            "features": obj.get("features"),
            "testBatchType": obj.get("testBatchType"),
            "status": obj.get("status"),
            "severity": obj.get("severity"),
            "importanceScore": obj.get("importanceScore"),
            "testCategory": obj.get("testCategory"),
            "category": obj.get("category"),
            "metrics": [TestMetric.from_dict(_item) for _item in obj["metrics"]] if obj.get("metrics") is not None else None,
            "urlSafeFeatureId": obj.get("urlSafeFeatureId"),
            "testCaseId": obj.get("testCaseId"),
            "display": TestCaseDisplay.from_dict(obj["display"]) if obj.get("display") is not None else None
        })
        return _obj


