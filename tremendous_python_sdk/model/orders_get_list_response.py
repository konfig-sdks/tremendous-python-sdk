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


class OrdersGetListResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "total_count",
            "orders",
        }
        
        class properties:
        
            @staticmethod
            def orders() -> typing.Type['OrdersGetListResponseOrders']:
                return OrdersGetListResponseOrders
            total_count = schemas.IntSchema
            __annotations__ = {
                "orders": orders,
                "total_count": total_count,
            }
    
    total_count: MetaOapg.properties.total_count
    orders: 'OrdersGetListResponseOrders'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orders"]) -> 'OrdersGetListResponseOrders': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_count"]) -> MetaOapg.properties.total_count: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["orders", "total_count", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orders"]) -> 'OrdersGetListResponseOrders': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_count"]) -> MetaOapg.properties.total_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["orders", "total_count", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        total_count: typing.Union[MetaOapg.properties.total_count, decimal.Decimal, int, ],
        orders: 'OrdersGetListResponseOrders',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OrdersGetListResponse':
        return super().__new__(
            cls,
            *args,
            total_count=total_count,
            orders=orders,
            _configuration=_configuration,
            **kwargs,
        )

from tremendous_python_sdk.model.orders_get_list_response_orders import OrdersGetListResponseOrders
