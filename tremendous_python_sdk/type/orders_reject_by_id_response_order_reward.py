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

from tremendous_python_sdk.type.orders_reject_by_id_response_order_reward_custom_fields import OrdersRejectByIdResponseOrderRewardCustomFields
from tremendous_python_sdk.type.orders_reject_by_id_response_order_reward_delivery import OrdersRejectByIdResponseOrderRewardDelivery
from tremendous_python_sdk.type.orders_reject_by_id_response_order_reward_recipient import OrdersRejectByIdResponseOrderRewardRecipient
from tremendous_python_sdk.type.orders_reject_by_id_response_order_reward_value import OrdersRejectByIdResponseOrderRewardValue

class RequiredOrdersRejectByIdResponseOrderReward(TypedDict):
    pass

class OptionalOrdersRejectByIdResponseOrderReward(TypedDict, total=False):
    # Tremendous ID of the reward
    id: str

    # Tremendous ID of the order this reward is part of.
    order_id: str

    # Date the reward was created
    created_at: datetime

    value: OrdersRejectByIdResponseOrderRewardValue

    recipient: OrdersRejectByIdResponseOrderRewardRecipient

    # Timestamp of reward delivery within the next year. Note that if date-time is provided, the time values will be ignored.
    deliver_at: date

    custom_fields: OrdersRejectByIdResponseOrderRewardCustomFields

    delivery: OrdersRejectByIdResponseOrderRewardDelivery

class OrdersRejectByIdResponseOrderReward(RequiredOrdersRejectByIdResponseOrderReward, OptionalOrdersRejectByIdResponseOrderReward):
    pass