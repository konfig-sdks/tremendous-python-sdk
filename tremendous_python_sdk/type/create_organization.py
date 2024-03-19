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

from tremendous_python_sdk.type.create_organization_copy_settings import CreateOrganizationCopySettings

class RequiredCreateOrganization(TypedDict):
    # Name of the organization
    name: str

    # URL of the website of that organization
    website: str

class OptionalCreateOrganization(TypedDict, total=False):
    # Default value is `false`. Set to true to also generate an API key associated to the new organization.
    with_api_key: bool

    copy_settings: CreateOrganizationCopySettings

    # Phone number of the organization. For non-US phone numbers, specify the country code (prefixed with +).
    phone: str

class CreateOrganization(RequiredCreateOrganization, OptionalCreateOrganization):
    pass