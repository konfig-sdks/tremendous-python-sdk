# coding: utf-8

"""
    API Endpoints

    Deliver monetary rewards and incentives to employees, customers, survey participants, and more through the Tremendous API. For organizational tasks, like managing your organization and it's members within Tremendous, please see the Tremendous Organizational API.

    The version of the OpenAPI document: 2
    Contact: developers@tremendous.com
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from tremendous_python_sdk import schemas  # noqa: F401


class BalanceTransactionsListAllResponseInvoices(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['BalanceTransactionsListAllResponseInvoicesItem']:
            return BalanceTransactionsListAllResponseInvoicesItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['BalanceTransactionsListAllResponseInvoicesItem'], typing.List['BalanceTransactionsListAllResponseInvoicesItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'BalanceTransactionsListAllResponseInvoices':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'BalanceTransactionsListAllResponseInvoicesItem':
        return super().__getitem__(i)

from tremendous_python_sdk.model.balance_transactions_list_all_response_invoices_item import BalanceTransactionsListAllResponseInvoicesItem
