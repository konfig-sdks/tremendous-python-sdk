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


class InvoicesCreateAndFundAccountBalanceRequest(BaseModel):
    # Amount of the invoice in USD
    amount: typing.Union[int, float] = Field(alias='amount')

    # Reference to the purchase order number within your organization
    po_number: typing.Optional[typing.Optional[str]] = Field(None, alias='po_number')

    # A note to be included in the invoice. This is for your internal use and will not be visible to the recipient. 
    memo: typing.Optional[typing.Optional[str]] = Field(None, alias='memo')
    class Config:
        arbitrary_types_allowed = True
