# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.credential_definition import CredentialDefinition


class CredentialDefinitionGetResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CredentialDefinitionGetResult - a model defined in OpenAPI

        credential_definition: The credential_definition of this CredentialDefinitionGetResult [Optional].
    """

    credential_definition: Optional[CredentialDefinition] = Field(alias="credential_definition", default=None)

CredentialDefinitionGetResult.update_forward_refs()