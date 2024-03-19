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

from tremendous_python_sdk.pydantic.orders_create_order_request_reward_custom_fields import OrdersCreateOrderRequestRewardCustomFields
from tremendous_python_sdk.pydantic.orders_create_order_request_reward_delivery import OrdersCreateOrderRequestRewardDelivery
from tremendous_python_sdk.pydantic.orders_create_order_request_reward_products import OrdersCreateOrderRequestRewardProducts
from tremendous_python_sdk.pydantic.orders_create_order_request_reward_recipient import OrdersCreateOrderRequestRewardRecipient
from tremendous_python_sdk.pydantic.orders_create_order_request_reward_value import OrdersCreateOrderRequestRewardValue

class OrdersCreateOrderRequestReward(BaseModel):
    # ID of the campaign in your account, that defines the available products (different gift cards, charity, etc.) that the recipient can choose from. 
    campaign_id: typing.Optional[typing.Optional[str]] = Field(None, alias='campaign_id')

    products: typing.Optional[OrdersCreateOrderRequestRewardProducts] = Field(None, alias='products')

    value: typing.Optional[OrdersCreateOrderRequestRewardValue] = Field(None, alias='value')

    recipient: typing.Optional[OrdersCreateOrderRequestRewardRecipient] = Field(None, alias='recipient')

    # Timestamp of reward delivery within the next year. Note that if date-time is provided, the time values will be ignored.
    deliver_at: typing.Optional[date] = Field(None, alias='deliver_at')

    custom_fields: typing.Optional[OrdersCreateOrderRequestRewardCustomFields] = Field(None, alias='custom_fields')

    # Set this to translate the redemption experience for this reward. Pass a 2-letter [ISO-639-1 code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for the desired language. Defaults to `en`. 
    language: typing.Optional[str] = Field(None, alias='language')

    delivery: typing.Optional[OrdersCreateOrderRequestRewardDelivery] = Field(None, alias='delivery')
    class Config:
        arbitrary_types_allowed = True
