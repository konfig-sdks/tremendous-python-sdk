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

from tremendous_python_sdk.type.orders_get_order_by_id401_response_errors import OrdersGetOrderById401ResponseErrors

class RequiredOrdersGetOrderById401Response(TypedDict):
    errors: OrdersGetOrderById401ResponseErrors

class OptionalOrdersGetOrderById401Response(TypedDict, total=False):
    pass

class OrdersGetOrderById401Response(RequiredOrdersGetOrderById401Response, OptionalOrdersGetOrderById401Response):
    pass
