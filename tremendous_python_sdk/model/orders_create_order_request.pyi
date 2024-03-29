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


class OrdersCreateOrderRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "reward",
            "payment",
        }
        
        class properties:
        
            @staticmethod
            def payment() -> typing.Type['OrdersCreateOrderRequestPayment']:
                return OrdersCreateOrderRequestPayment
        
            @staticmethod
            def reward() -> typing.Type['OrdersCreateOrderRequestReward']:
                return OrdersCreateOrderRequestReward
            
            
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
            __annotations__ = {
                "payment": payment,
                "reward": reward,
                "external_id": external_id,
            }
    
    reward: 'OrdersCreateOrderRequestReward'
    payment: 'OrdersCreateOrderRequestPayment'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment"]) -> 'OrdersCreateOrderRequestPayment': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reward"]) -> 'OrdersCreateOrderRequestReward': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["external_id"]) -> MetaOapg.properties.external_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["payment", "reward", "external_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment"]) -> 'OrdersCreateOrderRequestPayment': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reward"]) -> 'OrdersCreateOrderRequestReward': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["external_id"]) -> typing.Union[MetaOapg.properties.external_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["payment", "reward", "external_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        reward: 'OrdersCreateOrderRequestReward',
        payment: 'OrdersCreateOrderRequestPayment',
        external_id: typing.Union[MetaOapg.properties.external_id, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OrdersCreateOrderRequest':
        return super().__new__(
            cls,
            *args,
            reward=reward,
            payment=payment,
            external_id=external_id,
            _configuration=_configuration,
            **kwargs,
        )

from tremendous_python_sdk.model.orders_create_order_request_payment import OrdersCreateOrderRequestPayment
from tremendous_python_sdk.model.orders_create_order_request_reward import OrdersCreateOrderRequestReward
