# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class IndyProofRequestedProofPredicate(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyProofRequestedProofPredicate - a model defined in OpenAPI

        sub_proof_index: The sub_proof_index of this IndyProofRequestedProofPredicate [Optional].
    """

    sub_proof_index: Optional[int] = Field(alias="sub_proof_index", default=None)

IndyProofRequestedProofPredicate.update_forward_refs()