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

from tremendous_python_sdk.pydantic.orders_create_order202_response_order_rewards_item_custom_fields_item import OrdersCreateOrder202ResponseOrderRewardsItemCustomFieldsItem

OrdersCreateOrder202ResponseOrderRewardsItemCustomFields = typing.List[OrdersCreateOrder202ResponseOrderRewardsItemCustomFieldsItem]
