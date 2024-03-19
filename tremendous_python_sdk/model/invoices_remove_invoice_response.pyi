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


class InvoicesRemoveInvoiceResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "invoice",
        }
        
        class properties:
        
            @staticmethod
            def invoice() -> typing.Type['InvoicesRemoveInvoiceResponseInvoice']:
                return InvoicesRemoveInvoiceResponseInvoice
            __annotations__ = {
                "invoice": invoice,
            }
    
    invoice: 'InvoicesRemoveInvoiceResponseInvoice'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invoice"]) -> 'InvoicesRemoveInvoiceResponseInvoice': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["invoice", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invoice"]) -> 'InvoicesRemoveInvoiceResponseInvoice': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["invoice", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        invoice: 'InvoicesRemoveInvoiceResponseInvoice',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InvoicesRemoveInvoiceResponse':
        return super().__new__(
            cls,
            *args,
            invoice=invoice,
            _configuration=_configuration,
            **kwargs,
        )

from tremendous_python_sdk.model.invoices_remove_invoice_response_invoice import InvoicesRemoveInvoiceResponseInvoice