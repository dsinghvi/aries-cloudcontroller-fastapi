# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class LinkedDataProof(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    LinkedDataProof - a model defined in OpenAPI

        challenge: The challenge of this LinkedDataProof [Optional].
        created: The created of this LinkedDataProof.
        domain: The domain of this LinkedDataProof [Optional].
        jws: The jws of this LinkedDataProof [Optional].
        nonce: The nonce of this LinkedDataProof [Optional].
        proof_purpose: The proof_purpose of this LinkedDataProof.
        proof_value: The proof_value of this LinkedDataProof [Optional].
        type: The type of this LinkedDataProof.
        verification_method: The verification_method of this LinkedDataProof.
    """

    challenge: Optional[str] = Field(alias="challenge", default=None)
    created: str = Field(alias="created")
    domain: Optional[str] = Field(alias="domain", default=None)
    jws: Optional[str] = Field(alias="jws", default=None)
    nonce: Optional[str] = Field(alias="nonce", default=None)
    proof_purpose: str = Field(alias="proofPurpose")
    proof_value: Optional[str] = Field(alias="proofValue", default=None)
    type: str = Field(alias="type")
    verification_method: str = Field(alias="verificationMethod")

    @validator("created")
    def created_pattern(cls, value):
        assert value is not None and re.match(r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$", value)
        return value

    @validator("domain")
    def domain_pattern(cls, value):
        assert value is not None and re.match(r"\w+:(\\/?\\/?)[^\s]+", value)
        return value

    @validator("verification_method")
    def verification_method_pattern(cls, value):
        assert value is not None and re.match(r"\w+:(\\/?\\/?)[^\s]+", value)
        return value

LinkedDataProof.update_forward_refs()