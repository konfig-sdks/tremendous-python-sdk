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

from tremendous_python_sdk.pydantic.orders_reject_by_id_response_order_reward_custom_fields import OrdersRejectByIdResponseOrderRewardCustomFields
from tremendous_python_sdk.pydantic.orders_reject_by_id_response_order_reward_delivery import OrdersRejectByIdResponseOrderRewardDelivery
from tremendous_python_sdk.pydantic.orders_reject_by_id_response_order_reward_recipient import OrdersRejectByIdResponseOrderRewardRecipient
from tremendous_python_sdk.pydantic.orders_reject_by_id_response_order_reward_value import OrdersRejectByIdResponseOrderRewardValue

class OrdersRejectByIdResponseOrderReward(BaseModel):
    # Tremendous ID of the reward
    id: typing.Optional[str] = Field(None, alias='id')

    # Tremendous ID of the order this reward is part of.
    order_id: typing.Optional[str] = Field(None, alias='order_id')

    # Date the reward was created
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    value: typing.Optional[OrdersRejectByIdResponseOrderRewardValue] = Field(None, alias='value')

    recipient: typing.Optional[OrdersRejectByIdResponseOrderRewardRecipient] = Field(None, alias='recipient')

    # Timestamp of reward delivery within the next year. Note that if date-time is provided, the time values will be ignored.
    deliver_at: typing.Optional[date] = Field(None, alias='deliver_at')

    custom_fields: typing.Optional[OrdersRejectByIdResponseOrderRewardCustomFields] = Field(None, alias='custom_fields')

    delivery: typing.Optional[OrdersRejectByIdResponseOrderRewardDelivery] = Field(None, alias='delivery')
    class Config:
        arbitrary_types_allowed = True
