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

from tremendous_python_sdk.pydantic.webhooks_create_webhook_response_webhook import WebhooksCreateWebhookResponseWebhook

class WebhooksCreateWebhookResponse(BaseModel):
    webhook: typing.Optional[WebhooksCreateWebhookResponseWebhook] = Field(None, alias='webhook')
    class Config:
        arbitrary_types_allowed = True