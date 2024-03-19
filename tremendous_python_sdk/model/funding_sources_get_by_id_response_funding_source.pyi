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


class FundingSourcesGetByIdResponseFundingSource(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "method",
            "meta",
            "id",
        }
        
        class properties:
            
            
            class id(
                schemas.StrSchema
            ):
                pass
            
            
            class method(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def BALANCE(cls):
                    return cls("balance")
                
                @schemas.classproperty
                def BANK_ACCOUNT(cls):
                    return cls("bank_account")
                
                @schemas.classproperty
                def CREDIT_CARD(cls):
                    return cls("credit_card")
                
                @schemas.classproperty
                def INVOICE(cls):
                    return cls("invoice")
        
            @staticmethod
            def meta() -> typing.Type['FundingSourcesGetByIdResponseFundingSourceMeta']:
                return FundingSourcesGetByIdResponseFundingSourceMeta
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def COMMERCIAL(cls):
                    return cls("COMMERCIAL")
                
                @schemas.classproperty
                def PRO_FORMA(cls):
                    return cls("PRO_FORMA")
                
                @schemas.classproperty
                def PREFUNDING_ONLY(cls):
                    return cls("PREFUNDING_ONLY")
            __annotations__ = {
                "id": id,
                "method": method,
                "meta": meta,
                "type": type,
            }
    
    method: MetaOapg.properties.method
    meta: 'FundingSourcesGetByIdResponseFundingSourceMeta'
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["method"]) -> MetaOapg.properties.method: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> 'FundingSourcesGetByIdResponseFundingSourceMeta': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "method", "meta", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["method"]) -> MetaOapg.properties.method: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> 'FundingSourcesGetByIdResponseFundingSourceMeta': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "method", "meta", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        method: typing.Union[MetaOapg.properties.method, str, ],
        meta: 'FundingSourcesGetByIdResponseFundingSourceMeta',
        id: typing.Union[MetaOapg.properties.id, str, ],
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FundingSourcesGetByIdResponseFundingSource':
        return super().__new__(
            cls,
            *args,
            method=method,
            meta=meta,
            id=id,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from tremendous_python_sdk.model.funding_sources_get_by_id_response_funding_source_meta import FundingSourcesGetByIdResponseFundingSourceMeta
