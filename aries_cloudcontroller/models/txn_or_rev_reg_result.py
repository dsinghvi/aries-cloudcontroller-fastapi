# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.rev_reg_result import RevRegResult
from aries_cloudcontroller.models.txn_or_rev_reg_result_txn import TxnOrRevRegResultTxn


class TxnOrRevRegResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    TxnOrRevRegResult - a model defined in OpenAPI

        sent: The sent of this TxnOrRevRegResult [Optional].
        txn: The txn of this TxnOrRevRegResult [Optional].
    """

    sent: Optional[RevRegResult] = Field(alias="sent", default=None)
    txn: Optional[TxnOrRevRegResultTxn] = Field(alias="txn", default=None)

TxnOrRevRegResult.update_forward_refs()
