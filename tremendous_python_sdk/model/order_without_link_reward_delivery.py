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


class OrderWithoutLinkRewardDelivery(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details on how the reward is delivered to the recipient.

    """


    class MetaOapg:
        required = {
            "method",
            "status",
        }
        
        class properties:
            
            
            class method(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "EMAIL": "EMAIL",
                        "LINK": "LINK",
                        "PHONE": "PHONE",
                    }
                
                @schemas.classproperty
                def EMAIL(cls):
                    return cls("EMAIL")
                
                @schemas.classproperty
                def LINK(cls):
                    return cls("LINK")
                
                @schemas.classproperty
                def PHONE(cls):
                    return cls("PHONE")
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "SCHEDULED": "SCHEDULED",
                        "FAILED": "FAILED",
                        "SUCCEEDED": "SUCCEEDED",
                        "PENDING": "PENDING",
                    }
                
                @schemas.classproperty
                def SCHEDULED(cls):
                    return cls("SCHEDULED")
                
                @schemas.classproperty
                def FAILED(cls):
                    return cls("FAILED")
                
                @schemas.classproperty
                def SUCCEEDED(cls):
                    return cls("SUCCEEDED")
                
                @schemas.classproperty
                def PENDING(cls):
                    return cls("PENDING")
            __annotations__ = {
                "method": method,
                "status": status,
            }
    
    method: MetaOapg.properties.method
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["method"]) -> MetaOapg.properties.method: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["method", "status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["method"]) -> MetaOapg.properties.method: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["method", "status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        method: typing.Union[MetaOapg.properties.method, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OrderWithoutLinkRewardDelivery':
        return super().__new__(
            cls,
            *args,
            method=method,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )
