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

from tremendous_python_sdk.type.orders_reject_by_id429_response_errors import OrdersRejectById429ResponseErrors

class RequiredOrdersRejectById429Response(TypedDict):
    errors: OrdersRejectById429ResponseErrors

class OptionalOrdersRejectById429Response(TypedDict, total=False):
    pass

class OrdersRejectById429Response(RequiredOrdersRejectById429Response, OptionalOrdersRejectById429Response):
    pass
