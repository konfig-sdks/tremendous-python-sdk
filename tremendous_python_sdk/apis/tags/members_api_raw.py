# coding: utf-8

"""
    API Endpoints

    Deliver monetary rewards and incentives to employees, customers, survey participants, and more through the Tremendous API. For organizational tasks, like managing your organization and it's members within Tremendous, please see the Tremendous Organizational API.

    The version of the OpenAPI document: 2
    Contact: developers@tremendous.com
    Generated by: https://konfigthis.com
"""

from tremendous_python_sdk.paths.members.post import CreateNewMemberRaw
from tremendous_python_sdk.paths.members_id.get import GetMemberRaw
from tremendous_python_sdk.paths.members.get import ListMembersRaw


class MembersApiRaw(
    CreateNewMemberRaw,
    GetMemberRaw,
    ListMembersRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass