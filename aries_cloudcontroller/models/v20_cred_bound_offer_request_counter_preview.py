# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.v20_cred_attr_spec import V20CredAttrSpec


class V20CredBoundOfferRequestCounterPreview(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20CredBoundOfferRequestCounterPreview - a model defined in OpenAPI

        type: The type of this V20CredBoundOfferRequestCounterPreview [Optional].
        attributes: The attributes of this V20CredBoundOfferRequestCounterPreview.
    """

    type: Optional[str] = Field(alias="@type", default=None)
    attributes: List[V20CredAttrSpec] = Field(alias="attributes")

V20CredBoundOfferRequestCounterPreview.update_forward_refs()