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
from pydantic import BaseModel, Field, RootModel

from tremendous_python_sdk.pydantic.orders_create_order202_response_order_rewards_item_custom_fields import OrdersCreateOrder202ResponseOrderRewardsItemCustomFields
from tremendous_python_sdk.pydantic.orders_create_order202_response_order_rewards_item_delivery import OrdersCreateOrder202ResponseOrderRewardsItemDelivery
from tremendous_python_sdk.pydantic.orders_create_order202_response_order_rewards_item_recipient import OrdersCreateOrder202ResponseOrderRewardsItemRecipient
from tremendous_python_sdk.pydantic.orders_create_order202_response_order_rewards_item_value import OrdersCreateOrder202ResponseOrderRewardsItemValue

class OrdersCreateOrder202ResponseOrderRewardsItem(BaseModel):
    # Tremendous ID of the reward
    id: typing.Optional[str] = Field(None, alias='id')

    # Tremendous ID of the order this reward is part of.
    order_id: typing.Optional[str] = Field(None, alias='order_id')

    # Date the reward was created
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    value: typing.Optional[OrdersCreateOrder202ResponseOrderRewardsItemValue] = Field(None, alias='value')

    recipient: typing.Optional[OrdersCreateOrder202ResponseOrderRewardsItemRecipient] = Field(None, alias='recipient')

    # Timestamp of reward delivery within the next year. Note that if date-time is provided, the time values will be ignored.
    deliver_at: typing.Optional[date] = Field(None, alias='deliver_at')

    custom_fields: typing.Optional[OrdersCreateOrder202ResponseOrderRewardsItemCustomFields] = Field(None, alias='custom_fields')

    delivery: typing.Optional[OrdersCreateOrder202ResponseOrderRewardsItemDelivery] = Field(None, alias='delivery')
    class Config:
        arbitrary_types_allowed = True
