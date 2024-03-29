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

from tremendous_python_sdk.type.orders_get_list_response_orders import OrdersGetListResponseOrders

class RequiredOrdersGetListResponse(TypedDict):
    orders: OrdersGetListResponseOrders

    # The total number of orders across all pages
    total_count: int

class OptionalOrdersGetListResponse(TypedDict, total=False):
    pass

class OrdersGetListResponse(RequiredOrdersGetListResponse, OptionalOrdersGetListResponse):
    pass
