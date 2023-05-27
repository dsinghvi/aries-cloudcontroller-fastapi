# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.indy_proof_proof_aggregated_proof import IndyProofProofAggregatedProof
from aries_cloudcontroller.models.indy_proof_proof_proofs_proof import IndyProofProofProofsProof


class IndyProofProof(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyProofProof - a model defined in OpenAPI

        aggregated_proof: The aggregated_proof of this IndyProofProof [Optional].
        proofs: The proofs of this IndyProofProof [Optional].
    """

    aggregated_proof: Optional[IndyProofProofAggregatedProof] = Field(alias="aggregated_proof", default=None)
    proofs: Optional[List[IndyProofProofProofsProof]] = Field(alias="proofs", default=None)

IndyProofProof.update_forward_refs()