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

from tremendous_python_sdk.type.invoices_get_by_id404_response_errors import InvoicesGetById404ResponseErrors

class RequiredInvoicesGetById404Response(TypedDict):
    errors: InvoicesGetById404ResponseErrors

class OptionalInvoicesGetById404Response(TypedDict, total=False):
    pass

class InvoicesGetById404Response(RequiredInvoicesGetById404Response, OptionalInvoicesGetById404Response):
    pass
