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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ri.apiclient.models.model_task import ModelTask
from ri.apiclient.models.project_status import ProjectStatus
from ri.apiclient.models.search_spec import SearchSpec
from ri.apiclient.models.sort_spec import SortSpec
from ri.apiclient.models.test_category_type import TestCategoryType
from ri.apiclient.models.time_interval import TimeInterval
from typing import Optional, Set
from typing_extensions import Self

class ListProjectsRequestQuery(BaseModel):
    """
    ListProjectsRequestQuery
    """ # noqa: E501
    is_published: Optional[StrictBool] = Field(default=None, description="Optional: If true, return published projects. If false, return unpublished projects. If not specified, return all projects.", alias="isPublished")
    creation_time_range: Optional[TimeInterval] = Field(default=None, alias="creationTimeRange")
    last_test_run_time_range: Optional[TimeInterval] = Field(default=None, alias="lastTestRunTimeRange")
    stress_test_categories: Optional[List[TestCategoryType]] = Field(default=None, description="Optional: When specified, return all projects whose ST categories are a superset of the ST categories provided here.", alias="stressTestCategories")
    continuous_test_categories: Optional[List[TestCategoryType]] = Field(default=None, description="Optional: When specified, return all projects whose CT categories are a superset of the CT categories provided here.", alias="continuousTestCategories")
    owner_email: Optional[StrictStr] = Field(default=None, description="Optional: When specified, return all projects whose owner email matches.", alias="ownerEmail")
    model_tasks: Optional[List[ModelTask]] = Field(default=None, description="Optional: When specified, return all projects whose model task is the provided model task.", alias="modelTasks")
    status: Optional[ProjectStatus] = None
    sort: Optional[SortSpec] = None
    search: Optional[SearchSpec] = None
    __properties: ClassVar[List[str]] = ["isPublished", "creationTimeRange", "lastTestRunTimeRange", "stressTestCategories", "continuousTestCategories", "ownerEmail", "modelTasks", "status", "sort", "search"]

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
        """Create an instance of ListProjectsRequestQuery from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of creation_time_range
        if self.creation_time_range:
            _dict['creationTimeRange'] = self.creation_time_range.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_test_run_time_range
        if self.last_test_run_time_range:
            _dict['lastTestRunTimeRange'] = self.last_test_run_time_range.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sort
        if self.sort:
            _dict['sort'] = self.sort.to_dict()
        # override the default output from pydantic by calling `to_dict()` of search
        if self.search:
            _dict['search'] = self.search.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListProjectsRequestQuery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "isPublished": obj.get("isPublished"),
            "creationTimeRange": TimeInterval.from_dict(obj["creationTimeRange"]) if obj.get("creationTimeRange") is not None else None,
            "lastTestRunTimeRange": TimeInterval.from_dict(obj["lastTestRunTimeRange"]) if obj.get("lastTestRunTimeRange") is not None else None,
            "stressTestCategories": obj.get("stressTestCategories"),
            "continuousTestCategories": obj.get("continuousTestCategories"),
            "ownerEmail": obj.get("ownerEmail"),
            "modelTasks": obj.get("modelTasks"),
            "status": obj.get("status"),
            "sort": SortSpec.from_dict(obj["sort"]) if obj.get("sort") is not None else None,
            "search": SearchSpec.from_dict(obj["search"]) if obj.get("search") is not None else None
        })
        return _obj


