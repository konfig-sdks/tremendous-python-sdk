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

from tremendous_python_sdk.type.field_data import FieldData

class RequiredField(TypedDict):
    pass

class OptionalField(TypedDict, total=False):
    id: str

    # Label of the field
    label: str

    # Type of the values of the field
    data_type: str

    data: FieldData

    # Is this field required (true) or optional (false)
    required: bool

    # Type of objects this field gets associated with
    scope: str

class Field(RequiredField, OptionalField):
    pass