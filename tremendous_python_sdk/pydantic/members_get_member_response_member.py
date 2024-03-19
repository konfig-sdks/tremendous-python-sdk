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

from tremendous_python_sdk.pydantic.members_get_member_response_member_events import MembersGetMemberResponseMemberEvents

class MembersGetMemberResponseMember(BaseModel):
    id: str = Field(alias='id')

    # Email address of the member
    email: str = Field(alias='email')

    # Full name of the member
    name: typing.Optional[str] = Field(alias='name')

    # Role of the member within the organization.  <table>   <thead>     <tr>       <th>Role</th>       <th>Description</th>     </tr>   </thead>     <tr>       <td><code>MEMBER</code></td>       <td>Limited permissions. Can view their own reward and order histories only.</td>     </tr>     <tr>       <td><code>ADMIN</code></td>       <td>Update organization settings, invite other members to the organization, and view all member order and reward histories within their organization.</td>     </tr>     <tr>       <td><code>DELETED</code></td>       <td>No longer a member of this organization.</td>     </tr>   <tbody>   </tbody> </table> 
    role: Literal["MEMBER", "ADMIN", "DELETED"] = Field(alias='role')

    # Current status of the member's account.  When creating a member it starts out in the status `INVITED`. As soon as that member open the invitation link and registers an account, the status switches to `REGISTERED`. 
    status: Literal["REGISTERED", "INVITED"] = Field(alias='status')

    events: typing.Optional[MembersGetMemberResponseMemberEvents] = Field(None, alias='events')
    class Config:
        arbitrary_types_allowed = True