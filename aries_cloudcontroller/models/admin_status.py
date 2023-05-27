# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class AdminStatus(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AdminStatus - a model defined in OpenAPI

        conductor: The conductor of this AdminStatus [Optional].
        label: The label of this AdminStatus [Optional].
        timing: The timing of this AdminStatus [Optional].
        version: The version of this AdminStatus [Optional].
    """

    conductor: Optional[Dict[str, Any]] = Field(alias="conductor", default=None)
    label: Optional[str] = Field(alias="label", default=None)
    timing: Optional[Dict[str, Any]] = Field(alias="timing", default=None)
    version: Optional[str] = Field(alias="version", default=None)

AdminStatus.update_forward_refs()
