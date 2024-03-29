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


class RequiredMemberWithoutEvents(TypedDict):
    id: str

    # Email address of the member
    email: str

    # Full name of the member
    name: typing.Optional[str]

    # Role of the member within the organization.  <table>   <thead>     <tr>       <th>Role</th>       <th>Description</th>     </tr>   </thead>     <tr>       <td><code>MEMBER</code></td>       <td>Limited permissions. Can view their own reward and order histories only.</td>     </tr>     <tr>       <td><code>ADMIN</code></td>       <td>Update organization settings, invite other members to the organization, and view all member order and reward histories within their organization.</td>     </tr>     <tr>       <td><code>DELETED</code></td>       <td>No longer a member of this organization.</td>     </tr>   <tbody>   </tbody> </table> 
    role: str

    # Current status of the member's account.  When creating a member it starts out in the status `INVITED`. As soon as that member open the invitation link and registers an account, the status switches to `REGISTERED`. 
    status: str

class OptionalMemberWithoutEvents(TypedDict, total=False):
    # Timestamp when this member was created.  The `created_at` timestamp is **NOT** returned when retrieving a member (but is part of the response when listing or creating members). 
    created_at: datetime

    # Timestamp when this member most recently logged into the dashboard of the organization associated with this API key. 
    last_login_at: typing.Optional[datetime]

class MemberWithoutEvents(RequiredMemberWithoutEvents, OptionalMemberWithoutEvents):
    pass
