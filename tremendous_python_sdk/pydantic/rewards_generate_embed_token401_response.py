# coding: utf-8

"""
    API Endpoints

    Deliver monetary rewards and incentives to employees, customers, survey participants, and more through the Tremendous API. For organizational tasks, like managing your organization and it's members within Tremendous, please see the Tremendous Organizational API.

    The version of the OpenAPI document: 2
    Contact: developers@tremendous.com
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from tremendous_python_sdk.pydantic.rewards_generate_embed_token401_response_errors import RewardsGenerateEmbedToken401ResponseErrors

class RewardsGenerateEmbedToken401Response(BaseModel):
    errors: RewardsGenerateEmbedToken401ResponseErrors = Field(alias='errors')
    class Config:
        arbitrary_types_allowed = True
