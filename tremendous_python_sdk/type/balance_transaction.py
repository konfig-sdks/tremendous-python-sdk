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


class RequiredBalanceTransaction(TypedDict):
    pass

class OptionalBalanceTransaction(TypedDict, total=False):
    # A brief description of the transaction
    description: str

    # Date that the transaction was created
    created_at: date

    # Amount of the transaction in USD
    amount: typing.Union[int, float]

    # The updated total after the transaction. Note that this running balance may be delayed and contain `null`.
    balance: typing.Union[int, float]

    # The action that was performed
    action: str

class BalanceTransaction(RequiredBalanceTransaction, OptionalBalanceTransaction):
    pass