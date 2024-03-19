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


class RequiredCreateOrganizationCopySettings(TypedDict):
    pass

class OptionalCreateOrganizationCopySettings(TypedDict, total=False):
    # Copy over the campaigns from the current organization to the new organization. Defaults to `false`.
    campaigns: bool

    # Copy over the custom fields from the current organization to the new organization. Defaults to `false`.
    custom_fields: bool

    # Copy over the order approvals settings from the current organization to the new organization. Defaults to `false`.
    order_approvals: bool

    # Copy over the payment methods from the current organization to the new organization. Defaults to `false`.
    payment_methods: bool

    # Copy over the security settings from the current organization to the new organization. Defaults to `true`.
    security_settings: bool

    # Copy over the users from the current organization to the new organization. Defaults to `false`.
    users: bool

class CreateOrganizationCopySettings(RequiredCreateOrganizationCopySettings, OptionalCreateOrganizationCopySettings):
    pass
