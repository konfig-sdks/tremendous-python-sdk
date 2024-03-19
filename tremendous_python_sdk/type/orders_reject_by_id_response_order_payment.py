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

from tremendous_python_sdk.type.orders_reject_by_id_response_order_payment_refund import OrdersRejectByIdResponseOrderPaymentRefund

class RequiredOrdersRejectByIdResponseOrderPayment(TypedDict):
    pass

class OptionalOrdersRejectByIdResponseOrderPayment(TypedDict, total=False):
    # Total price of the order before fees (in USD)
    subtotal: typing.Union[int, float]

    # Total price of the order including fees (in USD)
    total: typing.Union[int, float]

    # Fees for the order (in USD)
    fees: typing.Union[int, float]

    refund: OrdersRejectByIdResponseOrderPaymentRefund

    # Name of the channel in which the order was created
    channel: str

class OrdersRejectByIdResponseOrderPayment(RequiredOrdersRejectByIdResponseOrderPayment, OptionalOrdersRejectByIdResponseOrderPayment):
    pass
