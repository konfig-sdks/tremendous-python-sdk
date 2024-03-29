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

from tremendous_python_sdk.type.orders_create_order_response_order_rewards_item_custom_fields import OrdersCreateOrderResponseOrderRewardsItemCustomFields
from tremendous_python_sdk.type.orders_create_order_response_order_rewards_item_delivery import OrdersCreateOrderResponseOrderRewardsItemDelivery
from tremendous_python_sdk.type.orders_create_order_response_order_rewards_item_recipient import OrdersCreateOrderResponseOrderRewardsItemRecipient
from tremendous_python_sdk.type.orders_create_order_response_order_rewards_item_value import OrdersCreateOrderResponseOrderRewardsItemValue

class RequiredOrdersCreateOrderResponseOrderRewardsItem(TypedDict):
    pass

class OptionalOrdersCreateOrderResponseOrderRewardsItem(TypedDict, total=False):
    # Tremendous ID of the reward
    id: str

    # Tremendous ID of the order this reward is part of.
    order_id: str

    # Date the reward was created
    created_at: datetime

    value: OrdersCreateOrderResponseOrderRewardsItemValue

    recipient: OrdersCreateOrderResponseOrderRewardsItemRecipient

    # Timestamp of reward delivery within the next year. Note that if date-time is provided, the time values will be ignored.
    deliver_at: date

    custom_fields: OrdersCreateOrderResponseOrderRewardsItemCustomFields

    delivery: OrdersCreateOrderResponseOrderRewardsItemDelivery

class OrdersCreateOrderResponseOrderRewardsItem(RequiredOrdersCreateOrderResponseOrderRewardsItem, OptionalOrdersCreateOrderResponseOrderRewardsItem):
    pass
