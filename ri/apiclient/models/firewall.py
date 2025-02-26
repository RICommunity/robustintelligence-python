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
from ri.apiclient.models.id import ID
from ri.apiclient.models.latest_run_info import LatestRunInfo
from ri.apiclient.models.risk_score import RiskScore
from ri.apiclient.models.scheduled_ct_info import ScheduledCTInfo
from ri.apiclient.models.test_category_severity import TestCategorySeverity
from typing import Optional, Set
from typing_extensions import Self

class Firewall(BaseModel):
    """
    Firewall
    """ # noqa: E501
    firewall_id: Optional[ID] = Field(default=None, alias="firewallId")
    project_id: Optional[ID] = Field(default=None, alias="projectId")
    model_id: Optional[ID] = Field(default=None, alias="modelId")
    bin_size: Optional[StrictStr] = Field(default=None, alias="binSize")
    ref_data_id: Optional[StrictStr] = Field(default=None, description="The semantic ID of the reference dataset. This should correspond with the primary key in the Dataset Registry.", alias="refDataId")
    scheduled_ct_info: Optional[ScheduledCTInfo] = Field(default=None, alias="scheduledCtInfo")
    risk_scores: Optional[List[RiskScore]] = Field(default=None, alias="riskScores")
    test_category_severities: Optional[List[TestCategorySeverity]] = Field(default=None, alias="testCategorySeverities")
    latest_run_info: Optional[LatestRunInfo] = Field(default=None, alias="latestRunInfo")
    __properties: ClassVar[List[str]] = ["firewallId", "projectId", "modelId", "binSize", "refDataId", "scheduledCtInfo", "riskScores", "testCategorySeverities", "latestRunInfo"]

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
        """Create an instance of Firewall from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of firewall_id
        if self.firewall_id:
            _dict['firewallId'] = self.firewall_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project_id
        if self.project_id:
            _dict['projectId'] = self.project_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model_id
        if self.model_id:
            _dict['modelId'] = self.model_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of scheduled_ct_info
        if self.scheduled_ct_info:
            _dict['scheduledCtInfo'] = self.scheduled_ct_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in risk_scores (list)
        _items = []
        if self.risk_scores:
            for _item in self.risk_scores:
                if _item:
                    _items.append(_item.to_dict())
            _dict['riskScores'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in test_category_severities (list)
        _items = []
        if self.test_category_severities:
            for _item in self.test_category_severities:
                if _item:
                    _items.append(_item.to_dict())
            _dict['testCategorySeverities'] = _items
        # override the default output from pydantic by calling `to_dict()` of latest_run_info
        if self.latest_run_info:
            _dict['latestRunInfo'] = self.latest_run_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Firewall from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "firewallId": ID.from_dict(obj["firewallId"]) if obj.get("firewallId") is not None else None,
            "projectId": ID.from_dict(obj["projectId"]) if obj.get("projectId") is not None else None,
            "modelId": ID.from_dict(obj["modelId"]) if obj.get("modelId") is not None else None,
            "binSize": obj.get("binSize"),
            "refDataId": obj.get("refDataId"),
            "scheduledCtInfo": ScheduledCTInfo.from_dict(obj["scheduledCtInfo"]) if obj.get("scheduledCtInfo") is not None else None,
            "riskScores": [RiskScore.from_dict(_item) for _item in obj["riskScores"]] if obj.get("riskScores") is not None else None,
            "testCategorySeverities": [TestCategorySeverity.from_dict(_item) for _item in obj["testCategorySeverities"]] if obj.get("testCategorySeverities") is not None else None,
            "latestRunInfo": LatestRunInfo.from_dict(obj["latestRunInfo"]) if obj.get("latestRunInfo") is not None else None
        })
        return _obj


