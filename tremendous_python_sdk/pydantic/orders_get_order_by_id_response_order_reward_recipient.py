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


class OrdersGetOrderByIdResponseOrderRewardRecipient(BaseModel):
    # Name of the recipient
    name: typing.Optional[str] = Field(None, alias='name')

    # Email address of the recipient
    email: typing.Optional[str] = Field(None, alias='email')

    # Phone number of the recipient. For non-US phone numbers, specify the country code (prefixed with +).
    phone: typing.Optional[str] = Field(None, alias='phone')
    class Config:
        arbitrary_types_allowed = True
