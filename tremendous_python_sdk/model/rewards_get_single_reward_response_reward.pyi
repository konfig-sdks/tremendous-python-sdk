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


class RewardsGetSingleRewardResponseReward(
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
        
            @staticmethod
            def value() -> typing.Type['RewardsGetSingleRewardResponseRewardValue']:
                return RewardsGetSingleRewardResponseRewardValue
        
            @staticmethod
            def recipient() -> typing.Type['RewardsGetSingleRewardResponseRewardRecipient']:
                return RewardsGetSingleRewardResponseRewardRecipient
            
            
            class deliver_at(
                schemas.DateSchema
            ):
                pass
        
            @staticmethod
            def custom_fields() -> typing.Type['RewardsGetSingleRewardResponseRewardCustomFields']:
                return RewardsGetSingleRewardResponseRewardCustomFields
        
            @staticmethod
            def delivery() -> typing.Type['RewardsGetSingleRewardResponseRewardDelivery']:
                return RewardsGetSingleRewardResponseRewardDelivery
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
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> 'RewardsGetSingleRewardResponseRewardValue': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recipient"]) -> 'RewardsGetSingleRewardResponseRewardRecipient': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deliver_at"]) -> MetaOapg.properties.deliver_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_fields"]) -> 'RewardsGetSingleRewardResponseRewardCustomFields': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["delivery"]) -> 'RewardsGetSingleRewardResponseRewardDelivery': ...
    
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
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union['RewardsGetSingleRewardResponseRewardValue', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recipient"]) -> typing.Union['RewardsGetSingleRewardResponseRewardRecipient', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deliver_at"]) -> typing.Union[MetaOapg.properties.deliver_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_fields"]) -> typing.Union['RewardsGetSingleRewardResponseRewardCustomFields', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["delivery"]) -> typing.Union['RewardsGetSingleRewardResponseRewardDelivery', schemas.Unset]: ...
    
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
        value: typing.Union['RewardsGetSingleRewardResponseRewardValue', schemas.Unset] = schemas.unset,
        recipient: typing.Union['RewardsGetSingleRewardResponseRewardRecipient', schemas.Unset] = schemas.unset,
        deliver_at: typing.Union[MetaOapg.properties.deliver_at, str, date, schemas.Unset] = schemas.unset,
        custom_fields: typing.Union['RewardsGetSingleRewardResponseRewardCustomFields', schemas.Unset] = schemas.unset,
        delivery: typing.Union['RewardsGetSingleRewardResponseRewardDelivery', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RewardsGetSingleRewardResponseReward':
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

from tremendous_python_sdk.model.rewards_get_single_reward_response_reward_custom_fields import RewardsGetSingleRewardResponseRewardCustomFields
from tremendous_python_sdk.model.rewards_get_single_reward_response_reward_delivery import RewardsGetSingleRewardResponseRewardDelivery
from tremendous_python_sdk.model.rewards_get_single_reward_response_reward_recipient import RewardsGetSingleRewardResponseRewardRecipient
from tremendous_python_sdk.model.rewards_get_single_reward_response_reward_value import RewardsGetSingleRewardResponseRewardValue
