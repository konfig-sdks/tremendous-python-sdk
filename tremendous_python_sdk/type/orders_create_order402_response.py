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

from tremendous_python_sdk.type.orders_create_order402_response_errors import OrdersCreateOrder402ResponseErrors

class RequiredOrdersCreateOrder402Response(TypedDict):
    errors: OrdersCreateOrder402ResponseErrors

class OptionalOrdersCreateOrder402Response(TypedDict, total=False):
    pass

class OrdersCreateOrder402Response(RequiredOrdersCreateOrder402Response, OptionalOrdersCreateOrder402Response):
    pass
