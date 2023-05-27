# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.attach_decorator import AttachDecorator
from aries_cloudcontroller.models.v20_cred_format import V20CredFormat


class V20CredExRecordCredRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20CredExRecordCredRequest - a model defined in OpenAPI

        id: The id of this V20CredExRecordCredRequest [Optional].
        type: The type of this V20CredExRecordCredRequest [Optional].
        comment: The comment of this V20CredExRecordCredRequest [Optional].
        formats: The formats of this V20CredExRecordCredRequest.
        requestsattach: The requestsattach of this V20CredExRecordCredRequest.
    """

    id: Optional[str] = Field(alias="@id", default=None)
    type: Optional[str] = Field(alias="@type", default=None)
    comment: Optional[str] = Field(alias="comment", default=None)
    formats: List[V20CredFormat] = Field(alias="formats")
    requestsattach: List[AttachDecorator] = Field(alias="requests~attach")

V20CredExRecordCredRequest.update_forward_refs()
