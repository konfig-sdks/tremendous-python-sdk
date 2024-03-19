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


class RequiredFundingSourcesGetByIdResponseFundingSourceMeta(TypedDict):
    pass

class OptionalFundingSourcesGetByIdResponseFundingSourceMeta(TypedDict, total=False):
    # **Only available when `method` is set to `balance`.**  Available amount for this funding source (in Cents USD) 
    available_cents: int

    # **Only available when `method` is set to `balance`.**  Funds that are already registered on your Tremendous account but which have not yet been deposited in your account (e.g. unpaid invoices) (in Cents USD). 
    pending_cents: int

    # **Only available when `method` is set to `bank_account` or `credit_card`.**  Name of the holder of the bank account or credit_card 
    accountholder_name: str

    # **Only available when `method` is set to `bank_account`.**  Is this a checking or savings account 
    account_type: str

    # **Only available when `method` is set to `bank_account`.**  Name of the bank 
    bank_name: typing.Optional[str]

    # **Only available when `method` is set to `bank_account`.**  Last 4 digits of the account number 
    account_number_mask: str

    # **Only available when `method` is set to `bank_account`.**  Last 4 digits of the routing number 
    account_routing_mask: str

    # **Only available when `method` is set to `bank_account`.**  Can refunds be deposited to this bank account 
    refundable: bool

    # **Only available when `method` is set to `credit_card`.**  Network of the credit card 
    network: str

    # **Only available when `method` is set to `credit_card`.**  Last 4 digits of the credit card number 
    last4: str

    # **Only available when `method` is set to `credit_card`.**  Is this credit card expired 
    expired: bool

    # **Only available when `method` is set to `bank_account` or `credit_card`.**  Point in time when the last order failed using this bank account or credit card as a funding source. 
    last_payment_failed_at: typing.Optional[datetime]

class FundingSourcesGetByIdResponseFundingSourceMeta(RequiredFundingSourcesGetByIdResponseFundingSourceMeta, OptionalFundingSourcesGetByIdResponseFundingSourceMeta):
    pass