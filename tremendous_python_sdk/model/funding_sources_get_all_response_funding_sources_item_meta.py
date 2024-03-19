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


class FundingSourcesGetAllResponseFundingSourcesItemMeta(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            available_cents = schemas.IntSchema
            pending_cents = schemas.IntSchema
            accountholder_name = schemas.StrSchema
            
            
            class account_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "checking": "CHECKING",
                        "savings": "SAVINGS",
                    }
                
                @schemas.classproperty
                def CHECKING(cls):
                    return cls("checking")
                
                @schemas.classproperty
                def SAVINGS(cls):
                    return cls("savings")
            
            
            class bank_name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'bank_name':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class account_number_mask(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'[0-9]{4}',
                    }]
            
            
            class account_routing_mask(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'[0-9]{4}',
                    }]
            refundable = schemas.BoolSchema
            
            
            class network(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "MasterCard": "MASTER_CARD",
                        "Amex": "AMEX",
                        "JCB": "JCB",
                        "Diner's Club": "DINERS_CLUB",
                        "visa": "VISA",
                        "discover": "DISCOVER",
                        "laser": "LASER",
                        "elo": "ELO",
                        "maestro": "MAESTRO",
                        "solo": "SOLO",
                    }
                
                @schemas.classproperty
                def MASTER_CARD(cls):
                    return cls("MasterCard")
                
                @schemas.classproperty
                def AMEX(cls):
                    return cls("Amex")
                
                @schemas.classproperty
                def JCB(cls):
                    return cls("JCB")
                
                @schemas.classproperty
                def DINERS_CLUB(cls):
                    return cls("Diner's Club")
                
                @schemas.classproperty
                def VISA(cls):
                    return cls("visa")
                
                @schemas.classproperty
                def DISCOVER(cls):
                    return cls("discover")
                
                @schemas.classproperty
                def LASER(cls):
                    return cls("laser")
                
                @schemas.classproperty
                def ELO(cls):
                    return cls("elo")
                
                @schemas.classproperty
                def MAESTRO(cls):
                    return cls("maestro")
                
                @schemas.classproperty
                def SOLO(cls):
                    return cls("solo")
            
            
            class last4(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'[0-9]{4}',
                    }]
            expired = schemas.BoolSchema
            
            
            class last_payment_failed_at(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'last_payment_failed_at':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "available_cents": available_cents,
                "pending_cents": pending_cents,
                "accountholder_name": accountholder_name,
                "account_type": account_type,
                "bank_name": bank_name,
                "account_number_mask": account_number_mask,
                "account_routing_mask": account_routing_mask,
                "refundable": refundable,
                "network": network,
                "last4": last4,
                "expired": expired,
                "last_payment_failed_at": last_payment_failed_at,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["available_cents"]) -> MetaOapg.properties.available_cents: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pending_cents"]) -> MetaOapg.properties.pending_cents: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountholder_name"]) -> MetaOapg.properties.accountholder_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_type"]) -> MetaOapg.properties.account_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bank_name"]) -> MetaOapg.properties.bank_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_number_mask"]) -> MetaOapg.properties.account_number_mask: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_routing_mask"]) -> MetaOapg.properties.account_routing_mask: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refundable"]) -> MetaOapg.properties.refundable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["network"]) -> MetaOapg.properties.network: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last4"]) -> MetaOapg.properties.last4: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expired"]) -> MetaOapg.properties.expired: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_payment_failed_at"]) -> MetaOapg.properties.last_payment_failed_at: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["available_cents", "pending_cents", "accountholder_name", "account_type", "bank_name", "account_number_mask", "account_routing_mask", "refundable", "network", "last4", "expired", "last_payment_failed_at", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["available_cents"]) -> typing.Union[MetaOapg.properties.available_cents, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pending_cents"]) -> typing.Union[MetaOapg.properties.pending_cents, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountholder_name"]) -> typing.Union[MetaOapg.properties.accountholder_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_type"]) -> typing.Union[MetaOapg.properties.account_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bank_name"]) -> typing.Union[MetaOapg.properties.bank_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_number_mask"]) -> typing.Union[MetaOapg.properties.account_number_mask, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_routing_mask"]) -> typing.Union[MetaOapg.properties.account_routing_mask, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refundable"]) -> typing.Union[MetaOapg.properties.refundable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["network"]) -> typing.Union[MetaOapg.properties.network, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last4"]) -> typing.Union[MetaOapg.properties.last4, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expired"]) -> typing.Union[MetaOapg.properties.expired, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_payment_failed_at"]) -> typing.Union[MetaOapg.properties.last_payment_failed_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["available_cents", "pending_cents", "accountholder_name", "account_type", "bank_name", "account_number_mask", "account_routing_mask", "refundable", "network", "last4", "expired", "last_payment_failed_at", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        available_cents: typing.Union[MetaOapg.properties.available_cents, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        pending_cents: typing.Union[MetaOapg.properties.pending_cents, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        accountholder_name: typing.Union[MetaOapg.properties.accountholder_name, str, schemas.Unset] = schemas.unset,
        account_type: typing.Union[MetaOapg.properties.account_type, str, schemas.Unset] = schemas.unset,
        bank_name: typing.Union[MetaOapg.properties.bank_name, None, str, schemas.Unset] = schemas.unset,
        account_number_mask: typing.Union[MetaOapg.properties.account_number_mask, str, schemas.Unset] = schemas.unset,
        account_routing_mask: typing.Union[MetaOapg.properties.account_routing_mask, str, schemas.Unset] = schemas.unset,
        refundable: typing.Union[MetaOapg.properties.refundable, bool, schemas.Unset] = schemas.unset,
        network: typing.Union[MetaOapg.properties.network, str, schemas.Unset] = schemas.unset,
        last4: typing.Union[MetaOapg.properties.last4, str, schemas.Unset] = schemas.unset,
        expired: typing.Union[MetaOapg.properties.expired, bool, schemas.Unset] = schemas.unset,
        last_payment_failed_at: typing.Union[MetaOapg.properties.last_payment_failed_at, None, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FundingSourcesGetAllResponseFundingSourcesItemMeta':
        return super().__new__(
            cls,
            *args,
            available_cents=available_cents,
            pending_cents=pending_cents,
            accountholder_name=accountholder_name,
            account_type=account_type,
            bank_name=bank_name,
            account_number_mask=account_number_mask,
            account_routing_mask=account_routing_mask,
            refundable=refundable,
            network=network,
            last4=last4,
            expired=expired,
            last_payment_failed_at=last_payment_failed_at,
            _configuration=_configuration,
            **kwargs,
        )
