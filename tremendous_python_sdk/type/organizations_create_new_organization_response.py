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

from tremendous_python_sdk.type.organizations_create_new_organization_response_organization import OrganizationsCreateNewOrganizationResponseOrganization

class RequiredOrganizationsCreateNewOrganizationResponse(TypedDict):
    pass

class OptionalOrganizationsCreateNewOrganizationResponse(TypedDict, total=False):
    organization: OrganizationsCreateNewOrganizationResponseOrganization

class OrganizationsCreateNewOrganizationResponse(RequiredOrganizationsCreateNewOrganizationResponse, OptionalOrganizationsCreateNewOrganizationResponse):
    pass
