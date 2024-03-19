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


class RequiredOrderRewardRecipient(TypedDict):
    pass

class OptionalOrderRewardRecipient(TypedDict, total=False):
    # Name of the recipient
    name: str

    # Email address of the recipient
    email: str

    # Phone number of the recipient. For non-US phone numbers, specify the country code (prefixed with +).
    phone: str

class OrderRewardRecipient(RequiredOrderRewardRecipient, OptionalOrderRewardRecipient):
    pass
