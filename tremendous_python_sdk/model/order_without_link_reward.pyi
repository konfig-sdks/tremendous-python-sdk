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


class OrderWithoutLinkReward(
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
                pass
            
            
            class order_id(
                schemas.StrSchema
            ):
                pass
            created_at = schemas.DateTimeSchema
            
            
            class campaign_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
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
            def products() -> typing.Type['OrderWithoutLinkRewardProducts']:
                return OrderWithoutLinkRewardProducts
        
            @staticmethod
            def value() -> typing.Type['OrderWithoutLinkRewardValue']:
                return OrderWithoutLinkRewardValue
        
            @staticmethod
            def recipient() -> typing.Type['OrderWithoutLinkRewardRecipient']:
                return OrderWithoutLinkRewardRecipient
            
            
            class deliver_at(
                schemas.DateSchema
            ):
                pass
        
            @staticmethod
            def custom_fields() -> typing.Type['OrderWithoutLinkRewardCustomFields']:
                return OrderWithoutLinkRewardCustomFields
        
            @staticmethod
            def delivery() -> typing.Type['OrderWithoutLinkRewardDelivery']:
                return OrderWithoutLinkRewardDelivery
            __annotations__ = {
                "id": id,
                "order_id": order_id,
                "created_at": created_at,
                "campaign_id": campaign_id,
                "products": products,
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
    def __getitem__(self, name: typing_extensions.Literal["campaign_id"]) -> MetaOapg.properties.campaign_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["products"]) -> 'OrderWithoutLinkRewardProducts': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> 'OrderWithoutLinkRewardValue': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recipient"]) -> 'OrderWithoutLinkRewardRecipient': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deliver_at"]) -> MetaOapg.properties.deliver_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_fields"]) -> 'OrderWithoutLinkRewardCustomFields': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["delivery"]) -> 'OrderWithoutLinkRewardDelivery': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "order_id", "created_at", "campaign_id", "products", "value", "recipient", "deliver_at", "custom_fields", "delivery", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order_id"]) -> typing.Union[MetaOapg.properties.order_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["campaign_id"]) -> typing.Union[MetaOapg.properties.campaign_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["products"]) -> typing.Union['OrderWithoutLinkRewardProducts', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union['OrderWithoutLinkRewardValue', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recipient"]) -> typing.Union['OrderWithoutLinkRewardRecipient', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deliver_at"]) -> typing.Union[MetaOapg.properties.deliver_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_fields"]) -> typing.Union['OrderWithoutLinkRewardCustomFields', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["delivery"]) -> typing.Union['OrderWithoutLinkRewardDelivery', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "order_id", "created_at", "campaign_id", "products", "value", "recipient", "deliver_at", "custom_fields", "delivery", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        order_id: typing.Union[MetaOapg.properties.order_id, str, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        campaign_id: typing.Union[MetaOapg.properties.campaign_id, None, str, schemas.Unset] = schemas.unset,
        products: typing.Union['OrderWithoutLinkRewardProducts', schemas.Unset] = schemas.unset,
        value: typing.Union['OrderWithoutLinkRewardValue', schemas.Unset] = schemas.unset,
        recipient: typing.Union['OrderWithoutLinkRewardRecipient', schemas.Unset] = schemas.unset,
        deliver_at: typing.Union[MetaOapg.properties.deliver_at, str, date, schemas.Unset] = schemas.unset,
        custom_fields: typing.Union['OrderWithoutLinkRewardCustomFields', schemas.Unset] = schemas.unset,
        delivery: typing.Union['OrderWithoutLinkRewardDelivery', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OrderWithoutLinkReward':
        return super().__new__(
            cls,
            *args,
            id=id,
            order_id=order_id,
            created_at=created_at,
            campaign_id=campaign_id,
            products=products,
            value=value,
            recipient=recipient,
            deliver_at=deliver_at,
            custom_fields=custom_fields,
            delivery=delivery,
            _configuration=_configuration,
            **kwargs,
        )

from tremendous_python_sdk.model.order_without_link_reward_custom_fields import OrderWithoutLinkRewardCustomFields
from tremendous_python_sdk.model.order_without_link_reward_delivery import OrderWithoutLinkRewardDelivery
from tremendous_python_sdk.model.order_without_link_reward_products import OrderWithoutLinkRewardProducts
from tremendous_python_sdk.model.order_without_link_reward_recipient import OrderWithoutLinkRewardRecipient
from tremendous_python_sdk.model.order_without_link_reward_value import OrderWithoutLinkRewardValue
