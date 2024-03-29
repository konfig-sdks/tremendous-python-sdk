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


class OrderBasePayment(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Cost breakdown of the order (cost of rewards + fees). Cost and fees are always denominated in USD, independent from the currency of the ordered rewards.
Note that this property will only appear for processed orders (`status` is `EXECUTED`).
    """


    class MetaOapg:
        
        class properties:
            
            
            class subtotal(
                schemas.Float64Schema
            ):
            
            
                class MetaOapg:
                    format = 'double'
                    inclusive_minimum = 0
            
            
            class total(
                schemas.Float64Schema
            ):
            
            
                class MetaOapg:
                    format = 'double'
                    inclusive_minimum = 0
            
            
            class fees(
                schemas.Float64Schema
            ):
            
            
                class MetaOapg:
                    format = 'double'
                    inclusive_minimum = 0
        
            @staticmethod
            def refund() -> typing.Type['OrderBasePaymentRefund']:
                return OrderBasePaymentRefund
            
            
            class channel(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "UI": "UI",
                        "API": "API",
                        "EMBED": "EMBED",
                        "DECIPHER": "DECIPHER",
                        "QUALTRICS": "QUALTRICS",
                        "TYPEFORM": "TYPEFORM",
                        "SURVEY MONKEY": "SURVEY_MONKEY",
                    }
                
                @schemas.classproperty
                def UI(cls):
                    return cls("UI")
                
                @schemas.classproperty
                def API(cls):
                    return cls("API")
                
                @schemas.classproperty
                def EMBED(cls):
                    return cls("EMBED")
                
                @schemas.classproperty
                def DECIPHER(cls):
                    return cls("DECIPHER")
                
                @schemas.classproperty
                def QUALTRICS(cls):
                    return cls("QUALTRICS")
                
                @schemas.classproperty
                def TYPEFORM(cls):
                    return cls("TYPEFORM")
                
                @schemas.classproperty
                def SURVEY_MONKEY(cls):
                    return cls("SURVEY MONKEY")
            __annotations__ = {
                "subtotal": subtotal,
                "total": total,
                "fees": fees,
                "refund": refund,
                "channel": channel,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subtotal"]) -> MetaOapg.properties.subtotal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fees"]) -> MetaOapg.properties.fees: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refund"]) -> 'OrderBasePaymentRefund': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channel"]) -> MetaOapg.properties.channel: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["subtotal", "total", "fees", "refund", "channel", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subtotal"]) -> typing.Union[MetaOapg.properties.subtotal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> typing.Union[MetaOapg.properties.total, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fees"]) -> typing.Union[MetaOapg.properties.fees, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refund"]) -> typing.Union['OrderBasePaymentRefund', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channel"]) -> typing.Union[MetaOapg.properties.channel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["subtotal", "total", "fees", "refund", "channel", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        subtotal: typing.Union[MetaOapg.properties.subtotal, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        total: typing.Union[MetaOapg.properties.total, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        fees: typing.Union[MetaOapg.properties.fees, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        refund: typing.Union['OrderBasePaymentRefund', schemas.Unset] = schemas.unset,
        channel: typing.Union[MetaOapg.properties.channel, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OrderBasePayment':
        return super().__new__(
            cls,
            *args,
            subtotal=subtotal,
            total=total,
            fees=fees,
            refund=refund,
            channel=channel,
            _configuration=_configuration,
            **kwargs,
        )

from tremendous_python_sdk.model.order_base_payment_refund import OrderBasePaymentRefund
