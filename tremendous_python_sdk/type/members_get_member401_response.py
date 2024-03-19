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

from tremendous_python_sdk.type.members_get_member401_response_errors import MembersGetMember401ResponseErrors

class RequiredMembersGetMember401Response(TypedDict):
    errors: MembersGetMember401ResponseErrors

class OptionalMembersGetMember401Response(TypedDict, total=False):
    pass

class MembersGetMember401Response(RequiredMembersGetMember401Response, OptionalMembersGetMember401Response):
    pass