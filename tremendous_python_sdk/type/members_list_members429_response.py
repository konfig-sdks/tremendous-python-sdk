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

from tremendous_python_sdk.type.members_list_members429_response_errors import MembersListMembers429ResponseErrors

class RequiredMembersListMembers429Response(TypedDict):
    errors: MembersListMembers429ResponseErrors

class OptionalMembersListMembers429Response(TypedDict, total=False):
    pass

class MembersListMembers429Response(RequiredMembersListMembers429Response, OptionalMembersListMembers429Response):
    pass
