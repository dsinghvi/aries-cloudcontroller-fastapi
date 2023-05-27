# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.indy_rev_reg_def_value_public_keys import IndyRevRegDefValuePublicKeys


class IndyRevRegDefValue(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyRevRegDefValue - a model defined in OpenAPI

        issuance_type: The issuance_type of this IndyRevRegDefValue [Optional].
        max_cred_num: The max_cred_num of this IndyRevRegDefValue [Optional].
        public_keys: The public_keys of this IndyRevRegDefValue [Optional].
        tails_hash: The tails_hash of this IndyRevRegDefValue [Optional].
        tails_location: The tails_location of this IndyRevRegDefValue [Optional].
    """

    issuance_type: Optional[str] = Field(alias="issuanceType", default=None)
    max_cred_num: Optional[int] = Field(alias="maxCredNum", default=None)
    public_keys: Optional[IndyRevRegDefValuePublicKeys] = Field(alias="publicKeys", default=None)
    tails_hash: Optional[str] = Field(alias="tailsHash", default=None)
    tails_location: Optional[str] = Field(alias="tailsLocation", default=None)

    @validator("max_cred_num")
    def max_cred_num_min(cls, value):
        assert value >= 1
        return value

    @validator("tails_hash")
    def tails_hash_pattern(cls, value):
        assert value is not None and re.match(r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$", value)
        return value

IndyRevRegDefValue.update_forward_refs()
