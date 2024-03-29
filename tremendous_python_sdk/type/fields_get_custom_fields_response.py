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

from tremendous_python_sdk.type.fields_get_custom_fields_response_fields import FieldsGetCustomFieldsResponseFields

class RequiredFieldsGetCustomFieldsResponse(TypedDict):
    pass

class OptionalFieldsGetCustomFieldsResponse(TypedDict, total=False):
    fields: FieldsGetCustomFieldsResponseFields

class FieldsGetCustomFieldsResponse(RequiredFieldsGetCustomFieldsResponse, OptionalFieldsGetCustomFieldsResponse):
    pass
