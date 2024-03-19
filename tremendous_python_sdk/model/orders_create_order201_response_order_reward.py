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


class OrdersCreateOrder201ResponseOrderReward(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A single reward, sent to a recipient. A reward is always part of an order.

Either `products` or `campaign_id` must be specified.

    """


    class MetaOapg:
        
        class properties:
            
            
            class id(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'[A-Z0-9]{4,20}',
                    }]
            
            
            class order_id(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'[A-Z0-9]{4,20}',
                    }]
            created_at = schemas.DateTimeSchema
        
            @staticmethod
            def value() -> typing.Type['OrdersCreateOrder201ResponseOrderRewardValue']:
                return OrdersCreateOrder201ResponseOrderRewardValue
        
            @staticmethod
            def recipient() -> typing.Type['OrdersCreateOrder201ResponseOrderRewardRecipient']:
                return OrdersCreateOrder201ResponseOrderRewardRecipient
            
            
            class deliver_at(
                schemas.DateSchema
            ):
            
            
                class MetaOapg:
                    format = 'date'
                    regex=[{
                        'pattern': r'YYYY-MM-DD',
                    }]
        
            @staticmethod
            def custom_fields() -> typing.Type['OrdersCreateOrder201ResponseOrderRewardCustomFields']:
                return OrdersCreateOrder201ResponseOrderRewardCustomFields
        
            @staticmethod
            def delivery() -> typing.Type['OrdersCreateOrder201ResponseOrderRewardDelivery']:
                return OrdersCreateOrder201ResponseOrderRewardDelivery
            __annotations__ = {
                "id": id,
                "order_id": order_id,
                "created_at": created_at,
                "value": value,
                "recipient": recipient,
                "deliver_at": deliver_at,
                "custom_fields": custom_fields,
                "delivery": delivery,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order_id"]) -> MetaOapg.properties.order_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> 'OrdersCreateOrder201ResponseOrderRewardValue': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recipient"]) -> 'OrdersCreateOrder201ResponseOrderRewardRecipient': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deliver_at"]) -> MetaOapg.properties.deliver_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_fields"]) -> 'OrdersCreateOrder201ResponseOrderRewardCustomFields': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["delivery"]) -> 'OrdersCreateOrder201ResponseOrderRewardDelivery': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "order_id", "created_at", "value", "recipient", "deliver_at", "custom_fields", "delivery", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order_id"]) -> typing.Union[MetaOapg.properties.order_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union['OrdersCreateOrder201ResponseOrderRewardValue', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recipient"]) -> typing.Union['OrdersCreateOrder201ResponseOrderRewardRecipient', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deliver_at"]) -> typing.Union[MetaOapg.properties.deliver_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_fields"]) -> typing.Union['OrdersCreateOrder201ResponseOrderRewardCustomFields', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["delivery"]) -> typing.Union['OrdersCreateOrder201ResponseOrderRewardDelivery', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "order_id", "created_at", "value", "recipient", "deliver_at", "custom_fields", "delivery", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        order_id: typing.Union[MetaOapg.properties.order_id, str, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        value: typing.Union['OrdersCreateOrder201ResponseOrderRewardValue', schemas.Unset] = schemas.unset,
        recipient: typing.Union['OrdersCreateOrder201ResponseOrderRewardRecipient', schemas.Unset] = schemas.unset,
        deliver_at: typing.Union[MetaOapg.properties.deliver_at, str, date, schemas.Unset] = schemas.unset,
        custom_fields: typing.Union['OrdersCreateOrder201ResponseOrderRewardCustomFields', schemas.Unset] = schemas.unset,
        delivery: typing.Union['OrdersCreateOrder201ResponseOrderRewardDelivery', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OrdersCreateOrder201ResponseOrderReward':
        return super().__new__(
            cls,
            *args,
            id=id,
            order_id=order_id,
            created_at=created_at,
            value=value,
            recipient=recipient,
            deliver_at=deliver_at,
            custom_fields=custom_fields,
            delivery=delivery,
            _configuration=_configuration,
            **kwargs,
        )

from tremendous_python_sdk.model.orders_create_order201_response_order_reward_custom_fields import OrdersCreateOrder201ResponseOrderRewardCustomFields
from tremendous_python_sdk.model.orders_create_order201_response_order_reward_delivery import OrdersCreateOrder201ResponseOrderRewardDelivery
from tremendous_python_sdk.model.orders_create_order201_response_order_reward_recipient import OrdersCreateOrder201ResponseOrderRewardRecipient
from tremendous_python_sdk.model.orders_create_order201_response_order_reward_value import OrdersCreateOrder201ResponseOrderRewardValue
