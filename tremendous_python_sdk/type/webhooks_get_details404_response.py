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

from tremendous_python_sdk.type.webhooks_get_details404_response_errors import WebhooksGetDetails404ResponseErrors

class RequiredWebhooksGetDetails404Response(TypedDict):
    errors: WebhooksGetDetails404ResponseErrors

class OptionalWebhooksGetDetails404Response(TypedDict, total=False):
    pass

class WebhooksGetDetails404Response(RequiredWebhooksGetDetails404Response, OptionalWebhooksGetDetails404Response):
    pass
