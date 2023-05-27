# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.schema_send_result_schema import SchemaSendResultSchema


class SchemaSendResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SchemaSendResult - a model defined in OpenAPI

        schema: The schema of this SchemaSendResult [Optional].
        schema_id: The schema_id of this SchemaSendResult.
    """

    schema: Optional[SchemaSendResultSchema] = Field(alias="schema", default=None)
    schema_id: str = Field(alias="schema_id")

    @validator("schema_id")
    def schema_id_pattern(cls, value):
        assert value is not None and re.match(r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$", value)
        return value

SchemaSendResult.update_forward_refs()