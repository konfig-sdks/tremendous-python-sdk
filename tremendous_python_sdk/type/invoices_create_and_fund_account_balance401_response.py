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

from tremendous_python_sdk.type.invoices_create_and_fund_account_balance401_response_errors import InvoicesCreateAndFundAccountBalance401ResponseErrors

class RequiredInvoicesCreateAndFundAccountBalance401Response(TypedDict):
    errors: InvoicesCreateAndFundAccountBalance401ResponseErrors

class OptionalInvoicesCreateAndFundAccountBalance401Response(TypedDict, total=False):
    pass

class InvoicesCreateAndFundAccountBalance401Response(RequiredInvoicesCreateAndFundAccountBalance401Response, OptionalInvoicesCreateAndFundAccountBalance401Response):
    pass
