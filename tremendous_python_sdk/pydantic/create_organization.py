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

from tremendous_python_sdk.pydantic.create_organization_copy_settings import CreateOrganizationCopySettings

class CreateOrganization(BaseModel):
    # Name of the organization
    name: str = Field(alias='name')

    # URL of the website of that organization
    website: str = Field(alias='website')

    # Default value is `false`. Set to true to also generate an API key associated to the new organization.
    with_api_key: typing.Optional[bool] = Field(None, alias='with_api_key')

    copy_settings: typing.Optional[CreateOrganizationCopySettings] = Field(None, alias='copy_settings')

    # Phone number of the organization. For non-US phone numbers, specify the country code (prefixed with +).
    phone: typing.Optional[str] = Field(None, alias='phone')
    class Config:
        arbitrary_types_allowed = True
