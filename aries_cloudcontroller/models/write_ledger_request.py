# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class WriteLedgerRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    WriteLedgerRequest - a model defined in OpenAPI

        ledger_id: The ledger_id of this WriteLedgerRequest [Optional].
    """

    ledger_id: Optional[str] = Field(alias="ledger_id", default=None)

WriteLedgerRequest.update_forward_refs()
