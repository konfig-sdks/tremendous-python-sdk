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

from tremendous_python_sdk.type.invoices_create_and_fund_account_balance429_response_errors import InvoicesCreateAndFundAccountBalance429ResponseErrors

class RequiredInvoicesCreateAndFundAccountBalance429Response(TypedDict):
    errors: InvoicesCreateAndFundAccountBalance429ResponseErrors

class OptionalInvoicesCreateAndFundAccountBalance429Response(TypedDict, total=False):
    pass

class InvoicesCreateAndFundAccountBalance429Response(RequiredInvoicesCreateAndFundAccountBalance429Response, OptionalInvoicesCreateAndFundAccountBalance429Response):
    pass
