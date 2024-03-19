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

from tremendous_python_sdk.pydantic.order_for_create_reward_custom_fields import OrderForCreateRewardCustomFields
from tremendous_python_sdk.pydantic.order_for_create_reward_delivery import OrderForCreateRewardDelivery
from tremendous_python_sdk.pydantic.order_for_create_reward_products import OrderForCreateRewardProducts
from tremendous_python_sdk.pydantic.order_for_create_reward_recipient import OrderForCreateRewardRecipient
from tremendous_python_sdk.pydantic.order_for_create_reward_value import OrderForCreateRewardValue

class OrderForCreateReward(BaseModel):
    # Tremendous ID of the reward
    id: typing.Optional[str] = Field(None, alias='id')

    # Tremendous ID of the order this reward is part of.
    order_id: typing.Optional[str] = Field(None, alias='order_id')

    # Date the reward was created
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    # ID of the campaign in your account, that defines the available products (different gift cards, charity, etc.) that the recipient can choose from. 
    campaign_id: typing.Optional[typing.Optional[str]] = Field(None, alias='campaign_id')

    products: typing.Optional[OrderForCreateRewardProducts] = Field(None, alias='products')

    value: typing.Optional[OrderForCreateRewardValue] = Field(None, alias='value')

    recipient: typing.Optional[OrderForCreateRewardRecipient] = Field(None, alias='recipient')

    # Timestamp of reward delivery within the next year. Note that if date-time is provided, the time values will be ignored.
    deliver_at: typing.Optional[date] = Field(None, alias='deliver_at')

    custom_fields: typing.Optional[OrderForCreateRewardCustomFields] = Field(None, alias='custom_fields')

    # Set this to translate the redemption experience for this reward. Pass a 2-letter [ISO-639-1 code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for the desired language. Defaults to `en`. 
    language: typing.Optional[str] = Field(None, alias='language')

    delivery: typing.Optional[OrderForCreateRewardDelivery] = Field(None, alias='delivery')
    class Config:
        arbitrary_types_allowed = True
