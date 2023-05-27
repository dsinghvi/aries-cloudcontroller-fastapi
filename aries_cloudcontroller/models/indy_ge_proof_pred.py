# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class IndyGEProofPred(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyGEProofPred - a model defined in OpenAPI

        attr_name: The attr_name of this IndyGEProofPred [Optional].
        p_type: The p_type of this IndyGEProofPred [Optional].
        value: The value of this IndyGEProofPred [Optional].
    """

    attr_name: Optional[str] = Field(alias="attr_name", default=None)
    p_type: Optional[str] = Field(alias="p_type", default=None)
    value: Optional[int] = Field(alias="value", default=None)

IndyGEProofPred.update_forward_refs()
