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

from tremendous_python_sdk.type.orders_create_order_request_payment import OrdersCreateOrderRequestPayment
from tremendous_python_sdk.type.orders_create_order_request_reward import OrdersCreateOrderRequestReward

class RequiredOrdersCreateOrderRequest(TypedDict):
    payment: OrdersCreateOrderRequestPayment

    reward: OrdersCreateOrderRequestReward

class OptionalOrdersCreateOrderRequest(TypedDict, total=False):
    # Reference for this order, supplied by the customer.  When set, `external_id` makes order idempotent. All requests that use the same `external_id` after the initial order creation, will result in a response that returns the data of the initially created order. The response will have a `201` response code. These responses **fail** to create any further orders.  It also allows for retrieving by `external_id` instead of `id` only. 
    external_id: typing.Optional[str]

class OrdersCreateOrderRequest(RequiredOrdersCreateOrderRequest, OptionalOrdersCreateOrderRequest):
    pass
