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

from tremendous_python_sdk.type.orders_get_list500_response_errors import OrdersGetList500ResponseErrors

class RequiredOrdersGetList500Response(TypedDict):
    errors: OrdersGetList500ResponseErrors

class OptionalOrdersGetList500Response(TypedDict, total=False):
    pass

class OrdersGetList500Response(RequiredOrdersGetList500Response, OptionalOrdersGetList500Response):
    pass
