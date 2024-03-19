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


class RequiredRewardToken(TypedDict):
    pass

class OptionalRewardToken(TypedDict, total=False):
    # Tremendous ID of the reward
    id: str

    # The token to redeem the reward. 
    token: str

    # Date the token expires
    expires_at: datetime

class RewardToken(RequiredRewardToken, OptionalRewardToken):
    pass
