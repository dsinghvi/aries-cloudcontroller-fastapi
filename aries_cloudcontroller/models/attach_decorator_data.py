# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.attach_decorator_data_jws import AttachDecoratorDataJws


class AttachDecoratorData(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AttachDecoratorData - a model defined in OpenAPI

        base64: The base64 of this AttachDecoratorData [Optional].
        json: The json of this AttachDecoratorData [Optional].
        jws: The jws of this AttachDecoratorData [Optional].
        links: The links of this AttachDecoratorData [Optional].
        sha256: The sha256 of this AttachDecoratorData [Optional].
    """

    base64: Optional[str] = Field(alias="base64", default=None)
    json: Optional[Dict[str, Any]] = Field(alias="json", default=None)
    jws: Optional[AttachDecoratorDataJws] = Field(alias="jws", default=None)
    links: Optional[List[str]] = Field(alias="links", default=None)
    sha256: Optional[str] = Field(alias="sha256", default=None)

    @validator("base64")
    def base64_pattern(cls, value):
        assert value is not None and re.match(r"^[a-zA-Z0-9+\/]*&#x3D;{0,2}$", value)
        return value

    @validator("sha256")
    def sha256_pattern(cls, value):
        assert value is not None and re.match(r"^[a-fA-F0-9+\/]{64}$", value)
        return value

AttachDecoratorData.update_forward_refs()
