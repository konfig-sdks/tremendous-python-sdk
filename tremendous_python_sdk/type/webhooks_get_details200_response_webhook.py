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


class RequiredWebhooksGetDetails200ResponseWebhook(TypedDict):
    # URL the webhook will make requests to
    url: typing.Optional[str]

class OptionalWebhooksGetDetails200ResponseWebhook(TypedDict, total=False):
    id: str

    # Private key for the webhook
    private_key: str

class WebhooksGetDetails200ResponseWebhook(RequiredWebhooksGetDetails200ResponseWebhook, OptionalWebhooksGetDetails200ResponseWebhook):
    pass
