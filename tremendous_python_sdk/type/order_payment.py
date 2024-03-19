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

from tremendous_python_sdk.type.order_payment_refund import OrderPaymentRefund

class RequiredOrderPayment(TypedDict):
    pass

class OptionalOrderPayment(TypedDict, total=False):
    # Total price of the order before fees (in USD)
    subtotal: typing.Union[int, float]

    # Total price of the order including fees (in USD)
    total: typing.Union[int, float]

    # Fees for the order (in USD)
    fees: typing.Union[int, float]

    refund: OrderPaymentRefund

    # Name of the channel in which the order was created
    channel: str

class OrderPayment(RequiredOrderPayment, OptionalOrderPayment):
    pass
