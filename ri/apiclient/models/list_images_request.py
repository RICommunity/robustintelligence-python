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
from ri.apiclient.models.pip_library_filter import PipLibraryFilter
from typing import Optional, Set
from typing_extensions import Self

class ListImagesRequest(BaseModel):
    """
    Request and response for a ListImages RPC.
    """ # noqa: E501
    page_token: Optional[StrictStr] = Field(default=None, description="Specifies a page of the list returned by a ListImages query. The ListImages query returns a pageToken when there is more than one page of results.", alias="pageToken")
    page_size: Optional[StrictStr] = Field(default=None, description="The maximum number of Image objects to return in a single page.", alias="pageSize")
    pip_libraries: Optional[List[PipLibraryFilter]] = Field(default=None, description="Optional. Filters the list for libraries that are installed on the Managed Image. The filter is only active when the list is not empty. When this filter is specified, do not include a pageToken field in the request.", alias="pipLibraries")
    __properties: ClassVar[List[str]] = ["pageToken", "pageSize", "pipLibraries"]

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
        """Create an instance of ListImagesRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in pip_libraries (list)
        _items = []
        if self.pip_libraries:
            for _item in self.pip_libraries:
                if _item:
                    _items.append(_item.to_dict())
            _dict['pipLibraries'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListImagesRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pageToken": obj.get("pageToken"),
            "pageSize": obj.get("pageSize"),
            "pipLibraries": [PipLibraryFilter.from_dict(_item) for _item in obj["pipLibraries"]] if obj.get("pipLibraries") is not None else None
        })
        return _obj


