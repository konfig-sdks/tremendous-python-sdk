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


class FundingSourcesGetByIdResponseFundingSourceMeta(BaseModel):
    # **Only available when `method` is set to `balance`.**  Available amount for this funding source (in Cents USD) 
    available_cents: typing.Optional[int] = Field(None, alias='available_cents')

    # **Only available when `method` is set to `balance`.**  Funds that are already registered on your Tremendous account but which have not yet been deposited in your account (e.g. unpaid invoices) (in Cents USD). 
    pending_cents: typing.Optional[int] = Field(None, alias='pending_cents')

    # **Only available when `method` is set to `bank_account` or `credit_card`.**  Name of the holder of the bank account or credit_card 
    accountholder_name: typing.Optional[str] = Field(None, alias='accountholder_name')

    # **Only available when `method` is set to `bank_account`.**  Is this a checking or savings account 
    account_type: typing.Optional[Literal["checking", "savings"]] = Field(None, alias='account_type')

    # **Only available when `method` is set to `bank_account`.**  Name of the bank 
    bank_name: typing.Optional[typing.Optional[str]] = Field(None, alias='bank_name')

    # **Only available when `method` is set to `bank_account`.**  Last 4 digits of the account number 
    account_number_mask: typing.Optional[str] = Field(None, alias='account_number_mask')

    # **Only available when `method` is set to `bank_account`.**  Last 4 digits of the routing number 
    account_routing_mask: typing.Optional[str] = Field(None, alias='account_routing_mask')

    # **Only available when `method` is set to `bank_account`.**  Can refunds be deposited to this bank account 
    refundable: typing.Optional[bool] = Field(None, alias='refundable')

    # **Only available when `method` is set to `credit_card`.**  Network of the credit card 
    network: typing.Optional[Literal["MasterCard", "Amex", "JCB", "Diner's Club", "visa", "discover", "laser", "elo", "maestro", "solo"]] = Field(None, alias='network')

    # **Only available when `method` is set to `credit_card`.**  Last 4 digits of the credit card number 
    last4: typing.Optional[str] = Field(None, alias='last4')

    # **Only available when `method` is set to `credit_card`.**  Is this credit card expired 
    expired: typing.Optional[bool] = Field(None, alias='expired')

    # **Only available when `method` is set to `bank_account` or `credit_card`.**  Point in time when the last order failed using this bank account or credit card as a funding source. 
    last_payment_failed_at: typing.Optional[typing.Optional[datetime]] = Field(None, alias='last_payment_failed_at')
    class Config:
        arbitrary_types_allowed = True
