# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class TransactionJobs(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    TransactionJobs - a model defined in OpenAPI

        transaction_my_job: The transaction_my_job of this TransactionJobs [Optional].
        transaction_their_job: The transaction_their_job of this TransactionJobs [Optional].
    """

    transaction_my_job: Optional[str] = Field(alias="transaction_my_job", default=None)
    transaction_their_job: Optional[str] = Field(alias="transaction_their_job", default=None)

TransactionJobs.update_forward_refs()
