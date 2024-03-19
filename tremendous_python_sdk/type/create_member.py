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


class RequiredCreateMember(TypedDict):
    # Email address of the member
    email: str

    # Full name of the member
    name: str

    # Role of the member within the organization.  <table>   <thead>     <tr>       <th>Role</th>       <th>Description</th>     </tr>   </thead>     <tr>       <td><code>MEMBER</code></td>       <td>Limited permissions. Can view their own reward and order histories only.</td>     </tr>     <tr>       <td><code>ADMIN</code></td>       <td>Update organization settings, invite other members to the organization, and view all member order and reward histories within their organization.</td>     </tr>   <tbody> </table> 
    role: str

class OptionalCreateMember(TypedDict, total=False):
    pass

class CreateMember(RequiredCreateMember, OptionalCreateMember):
    pass
