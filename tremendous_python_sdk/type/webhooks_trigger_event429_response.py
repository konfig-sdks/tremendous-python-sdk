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

from tremendous_python_sdk.type.webhooks_trigger_event429_response_errors import WebhooksTriggerEvent429ResponseErrors

class RequiredWebhooksTriggerEvent429Response(TypedDict):
    errors: WebhooksTriggerEvent429ResponseErrors

class OptionalWebhooksTriggerEvent429Response(TypedDict, total=False):
    pass

class WebhooksTriggerEvent429Response(RequiredWebhooksTriggerEvent429Response, OptionalWebhooksTriggerEvent429Response):
    pass