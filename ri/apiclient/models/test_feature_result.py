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
from ri.apiclient.models.feature_type import FeatureType
from ri.apiclient.models.named_double import NamedDouble
from ri.apiclient.models.result_summary_counts import ResultSummaryCounts
from ri.apiclient.models.rime_severity import RimeSeverity
from ri.apiclient.models.test_feature_result_display import TestFeatureResultDisplay
from typing import Optional, Set
from typing_extensions import Self

class TestFeatureResult(BaseModel):
    """
    TestFeatureResult returns the feature results for a given test. Similar to results_upload.proto but with separation of uploading and querying.
    """ # noqa: E501
    url_safe_feature_id: Optional[StrictStr] = Field(default=None, description="The URL-compatible (base 64) encoding of feature name.", alias="urlSafeFeatureId")
    feature_name: Optional[StrictStr] = Field(default=None, description="The human-readable feature name.", alias="featureName")
    feature_type: Optional[FeatureType] = None
    severity: Optional[RimeSeverity] = None
    summary_counts: Optional[ResultSummaryCounts] = Field(default=None, alias="summaryCounts")
    failing_tests: Optional[List[StrictStr]] = Field(default=None, description="The list of tests that fail for the feature.", alias="failingTests")
    num_failing_rows: Optional[StrictStr] = Field(default=None, description="The number of rows that fail.", alias="numFailingRows")
    failing_rows_html: Optional[StrictStr] = Field(default=None, description="The names of the rows that fail; may contain HTML.", alias="failingRowsHtml")
    drift_statistic: Optional[NamedDouble] = Field(default=None, alias="driftStatistic")
    model_impact: Optional[NamedDouble] = Field(default=None, alias="modelImpact")
    feature_infos: Optional[List[StrictStr]] = Field(default=None, description="The list of feature information used.", alias="featureInfos")
    display: Optional[TestFeatureResultDisplay] = None
    __properties: ClassVar[List[str]] = ["urlSafeFeatureId", "featureName", "featureType", "severity", "summaryCounts", "failingTests", "numFailingRows", "failingRowsHtml", "driftStatistic", "modelImpact", "featureInfos", "display"]

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
        """Create an instance of TestFeatureResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of summary_counts
        if self.summary_counts:
            _dict['summaryCounts'] = self.summary_counts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of drift_statistic
        if self.drift_statistic:
            _dict['driftStatistic'] = self.drift_statistic.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model_impact
        if self.model_impact:
            _dict['modelImpact'] = self.model_impact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of display
        if self.display:
            _dict['display'] = self.display.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TestFeatureResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "urlSafeFeatureId": obj.get("urlSafeFeatureId"),
            "featureName": obj.get("featureName"),
            "featureType": obj.get("featureType"),
            "severity": obj.get("severity"),
            "summaryCounts": ResultSummaryCounts.from_dict(obj["summaryCounts"]) if obj.get("summaryCounts") is not None else None,
            "failingTests": obj.get("failingTests"),
            "numFailingRows": obj.get("numFailingRows"),
            "failingRowsHtml": obj.get("failingRowsHtml"),
            "driftStatistic": NamedDouble.from_dict(obj["driftStatistic"]) if obj.get("driftStatistic") is not None else None,
            "modelImpact": NamedDouble.from_dict(obj["modelImpact"]) if obj.get("modelImpact") is not None else None,
            "featureInfos": obj.get("featureInfos"),
            "display": TestFeatureResultDisplay.from_dict(obj["display"]) if obj.get("display") is not None else None
        })
        return _obj


