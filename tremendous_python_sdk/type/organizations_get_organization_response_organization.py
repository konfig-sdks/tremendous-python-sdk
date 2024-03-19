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


class RequiredOrganizationsGetOrganizationResponseOrganization(TypedDict):
    # Name of the organization
    name: str

    # URL of the website of that organization
    website: str

class OptionalOrganizationsGetOrganizationResponseOrganization(TypedDict, total=False):
    id: str

    # Status of the organization. Organizations need to be approved to be able to use them to send out rewards.
    status: str

    # Timestamp of when the organization has been created.  *This field is only returned when creating an organization.* It is not returned anymore when retrieving or listing organizations. 
    created_at: date

class OrganizationsGetOrganizationResponseOrganization(RequiredOrganizationsGetOrganizationResponseOrganization, OptionalOrganizationsGetOrganizationResponseOrganization):
    pass
