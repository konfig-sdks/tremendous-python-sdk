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


class OrdersGetOrderByIdResponseOrder(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    An order wraps around the fulfilment of one or more rewards.
    """


    class MetaOapg:
        required = {
            "created_at",
            "id",
            "status",
        }
        
        class properties:
            
            
            class id(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'[A-Z0-9]{4,20}',
                    }]
            created_at = schemas.DateTimeSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "CANCELED": "CANCELED",
                        "CART": "CART",
                        "EXECUTED": "EXECUTED",
                        "FAILED": "FAILED",
                        "PENDING APPROVAL": "PENDING_APPROVAL",
                        "PENDING INTERNAL PAYMENT APPROVAL": "PENDING_INTERNAL_PAYMENT_APPROVAL",
                    }
                
                @schemas.classproperty
                def CANCELED(cls):
                    return cls("CANCELED")
                
                @schemas.classproperty
                def CART(cls):
                    return cls("CART")
                
                @schemas.classproperty
                def EXECUTED(cls):
                    return cls("EXECUTED")
                
                @schemas.classproperty
                def FAILED(cls):
                    return cls("FAILED")
                
                @schemas.classproperty
                def PENDING_APPROVAL(cls):
                    return cls("PENDING APPROVAL")
                
                @schemas.classproperty
                def PENDING_INTERNAL_PAYMENT_APPROVAL(cls):
                    return cls("PENDING INTERNAL PAYMENT APPROVAL")
            
            
            class external_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'external_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class campaign_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'[A-Z0-9]{4,20}',
                    }]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'campaign_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def payment() -> typing.Type['OrdersGetOrderByIdResponseOrderPayment']:
                return OrdersGetOrderByIdResponseOrderPayment
            invoice_id = schemas.StrSchema
        
            @staticmethod
            def reward() -> typing.Type['OrdersGetOrderByIdResponseOrderReward']:
                return OrdersGetOrderByIdResponseOrderReward
            __annotations__ = {
                "id": id,
                "created_at": created_at,
                "status": status,
                "external_id": external_id,
                "campaign_id": campaign_id,
                "payment": payment,
                "invoice_id": invoice_id,
                "reward": reward,
            }
    
    created_at: MetaOapg.properties.created_at
    id: MetaOapg.properties.id
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["external_id"]) -> MetaOapg.properties.external_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["campaign_id"]) -> MetaOapg.properties.campaign_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment"]) -> 'OrdersGetOrderByIdResponseOrderPayment': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invoice_id"]) -> MetaOapg.properties.invoice_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reward"]) -> 'OrdersGetOrderByIdResponseOrderReward': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "created_at", "status", "external_id", "campaign_id", "payment", "invoice_id", "reward", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["external_id"]) -> typing.Union[MetaOapg.properties.external_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["campaign_id"]) -> typing.Union[MetaOapg.properties.campaign_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment"]) -> typing.Union['OrdersGetOrderByIdResponseOrderPayment', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invoice_id"]) -> typing.Union[MetaOapg.properties.invoice_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reward"]) -> typing.Union['OrdersGetOrderByIdResponseOrderReward', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "created_at", "status", "external_id", "campaign_id", "payment", "invoice_id", "reward", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        external_id: typing.Union[MetaOapg.properties.external_id, None, str, schemas.Unset] = schemas.unset,
        campaign_id: typing.Union[MetaOapg.properties.campaign_id, None, str, schemas.Unset] = schemas.unset,
        payment: typing.Union['OrdersGetOrderByIdResponseOrderPayment', schemas.Unset] = schemas.unset,
        invoice_id: typing.Union[MetaOapg.properties.invoice_id, str, schemas.Unset] = schemas.unset,
        reward: typing.Union['OrdersGetOrderByIdResponseOrderReward', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OrdersGetOrderByIdResponseOrder':
        return super().__new__(
            cls,
            *args,
            created_at=created_at,
            id=id,
            status=status,
            external_id=external_id,
            campaign_id=campaign_id,
            payment=payment,
            invoice_id=invoice_id,
            reward=reward,
            _configuration=_configuration,
            **kwargs,
        )

from tremendous_python_sdk.model.orders_get_order_by_id_response_order_payment import OrdersGetOrderByIdResponseOrderPayment
from tremendous_python_sdk.model.orders_get_order_by_id_response_order_reward import OrdersGetOrderByIdResponseOrderReward
