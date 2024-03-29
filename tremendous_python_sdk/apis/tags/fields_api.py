# coding: utf-8

"""
    API Endpoints

    Deliver monetary rewards and incentives to employees, customers, survey participants, and more through the Tremendous API. For organizational tasks, like managing your organization and it's members within Tremendous, please see the Tremendous Organizational API.

    The version of the OpenAPI document: 2
    Contact: developers@tremendous.com
    Generated by: https://konfigthis.com
"""

from tremendous_python_sdk.paths.fields.get import GetCustomFields
from tremendous_python_sdk.apis.tags.fields_api_raw import FieldsApiRaw


class FieldsApi(
    GetCustomFields,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: FieldsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = FieldsApiRaw(api_client)
