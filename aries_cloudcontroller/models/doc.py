# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.doc_options import DocOptions


class Doc(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Doc - a model defined in OpenAPI

        credential: The credential of this Doc.
        options: The options of this Doc.
    """

    credential: Dict[str, Any] = Field(alias="credential")
    options: DocOptions = Field(alias="options")

Doc.update_forward_refs()