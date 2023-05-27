# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.query_item import QueryItem


class V20DiscoveryRecordQueriesMsg(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20DiscoveryRecordQueriesMsg - a model defined in OpenAPI

        id: The id of this V20DiscoveryRecordQueriesMsg [Optional].
        type: The type of this V20DiscoveryRecordQueriesMsg [Optional].
        queries: The queries of this V20DiscoveryRecordQueriesMsg [Optional].
    """

    id: Optional[str] = Field(alias="@id", default=None)
    type: Optional[str] = Field(alias="@type", default=None)
    queries: Optional[List[QueryItem]] = Field(alias="queries", default=None)

V20DiscoveryRecordQueriesMsg.update_forward_refs()