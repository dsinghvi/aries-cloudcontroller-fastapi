# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.v10_discovery_exchange_list_result_results_inner import V10DiscoveryExchangeListResultResultsInner


class V10DiscoveryExchangeListResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V10DiscoveryExchangeListResult - a model defined in OpenAPI

        results: The results of this V10DiscoveryExchangeListResult [Optional].
    """

    results: Optional[List[V10DiscoveryExchangeListResultResultsInner]] = Field(alias="results", default=None)

V10DiscoveryExchangeListResult.update_forward_refs()