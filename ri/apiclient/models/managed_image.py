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
from ri.apiclient.models.image_reference import ImageReference
from ri.apiclient.models.managed_image_status import ManagedImageStatus
from ri.apiclient.models.package_requirement import PackageRequirement
from ri.apiclient.models.pip_library import PipLibrary
from ri.apiclient.models.pip_requirement import PipRequirement
from ri.apiclient.models.role_type import RoleType
from typing import Optional, Set
from typing_extensions import Self

class ManagedImage(BaseModel):
    """
    A representation of a custom Image whose tag or version is managed by the ImageRegistry.
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The external name of the image. This name must match the /^[a-z][a-z0-9]*(?:[_-][a-z0-9]+)*$/ regular expression. See the naming rules in https://docs.docker.com/engine/reference/commandline/tag/#extended-description https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html from which the naming convention derives. The above names are valid ECR or Docker image names.")
    base_image: Optional[ImageReference] = Field(default=None, alias="baseImage")
    role_type: Optional[RoleType] = None
    child_images: Optional[List[ImageReference]] = Field(default=None, description="The set of images that use this image as a source.", alias="childImages")
    rime_tag: Optional[StrictStr] = Field(default=None, description="The tag of the RIME wheel used to build the managed image.", alias="rimeTag")
    repo_uri: Optional[StrictStr] = Field(default=None, description="The URI of the repository.", alias="repoUri")
    status: Optional[ManagedImageStatus] = None
    package_requirements: Optional[List[PackageRequirement]] = Field(default=None, description="A list of all system package requirements used to build this image.", alias="packageRequirements")
    pip_requirements: Optional[List[PipRequirement]] = Field(default=None, description="A list of all pip requirements used to build this image.", alias="pipRequirements")
    pip_libraries: Optional[List[PipLibrary]] = Field(default=None, description="A list of all pip libraries installed on this image as obtained by running `pip list`.", alias="pipLibraries")
    python_version: Optional[StrictStr] = Field(default=None, description="The version of Python used to build the Robust Intelligence image.", alias="pythonVersion")
    __properties: ClassVar[List[str]] = ["name", "baseImage", "roleType", "childImages", "rimeTag", "repoUri", "status", "packageRequirements", "pipRequirements", "pipLibraries", "pythonVersion"]

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
        """Create an instance of ManagedImage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of base_image
        if self.base_image:
            _dict['baseImage'] = self.base_image.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in child_images (list)
        _items = []
        if self.child_images:
            for _item in self.child_images:
                if _item:
                    _items.append(_item.to_dict())
            _dict['childImages'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in package_requirements (list)
        _items = []
        if self.package_requirements:
            for _item in self.package_requirements:
                if _item:
                    _items.append(_item.to_dict())
            _dict['packageRequirements'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in pip_requirements (list)
        _items = []
        if self.pip_requirements:
            for _item in self.pip_requirements:
                if _item:
                    _items.append(_item.to_dict())
            _dict['pipRequirements'] = _items
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
        """Create an instance of ManagedImage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "baseImage": ImageReference.from_dict(obj["baseImage"]) if obj.get("baseImage") is not None else None,
            "roleType": obj.get("roleType"),
            "childImages": [ImageReference.from_dict(_item) for _item in obj["childImages"]] if obj.get("childImages") is not None else None,
            "rimeTag": obj.get("rimeTag"),
            "repoUri": obj.get("repoUri"),
            "status": obj.get("status"),
            "packageRequirements": [PackageRequirement.from_dict(_item) for _item in obj["packageRequirements"]] if obj.get("packageRequirements") is not None else None,
            "pipRequirements": [PipRequirement.from_dict(_item) for _item in obj["pipRequirements"]] if obj.get("pipRequirements") is not None else None,
            "pipLibraries": [PipLibrary.from_dict(_item) for _item in obj["pipLibraries"]] if obj.get("pipLibraries") is not None else None,
            "pythonVersion": obj.get("pythonVersion")
        })
        return _obj


