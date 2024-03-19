# coding: utf-8

"""
    API Endpoints

    Deliver monetary rewards and incentives to employees, customers, survey participants, and more through the Tremendous API. For organizational tasks, like managing your organization and it's members within Tremendous, please see the Tremendous Organizational API.

    The version of the OpenAPI document: 2
    Contact: developers@tremendous.com
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import tremendous_python_sdk
from tremendous_python_sdk.paths.webhooks_id import get
from tremendous_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestWebhooksId(ApiTestMixin, unittest.TestCase):
    """
    WebhooksId unit test stubs
        Retrieve webhook
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
