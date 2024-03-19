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

from tremendous_python_sdk.type.funding_sources_get_by_id401_response_errors import FundingSourcesGetById401ResponseErrors

class RequiredFundingSourcesGetById401Response(TypedDict):
    errors: FundingSourcesGetById401ResponseErrors

class OptionalFundingSourcesGetById401Response(TypedDict, total=False):
    pass

class FundingSourcesGetById401Response(RequiredFundingSourcesGetById401Response, OptionalFundingSourcesGetById401Response):
    pass
