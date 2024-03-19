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


class RequiredRewardsListAllRewards500ResponseErrors(TypedDict):
    pass

class OptionalRewardsListAllRewards500ResponseErrors(TypedDict, total=False):
    # Error message
    message: str

    # Mirrors the request parameters structure, filled only with the (nested) properties that caused an error.
    payload: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class RewardsListAllRewards500ResponseErrors(RequiredRewardsListAllRewards500ResponseErrors, OptionalRewardsListAllRewards500ResponseErrors):
    pass
