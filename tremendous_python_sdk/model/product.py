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


class Product(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A product represents one way to payout a reward to it's recipient. Think:

* Amazon.com gift card (ID: `OKMHM2X2OHYV`)
* Donations to Save the Children (ID: `ESRNAD533W5A`)
* Virtual Visa debit card (ID: `Q24BD9EZ332JT`)

each of which is one specific product on Tremendous.

> 📘 All available products
>
> See this [list](https://www.tremendous.com/catalog)

Products can be limited in their availability to recipients by

* geography (field `countries`)
* currency (field `currencies`)
* amount of the reward (field `skus`)
  * e.g. adidas gift cards accept any amount between 5 and 200 USD.

See the description of each respective parameter for further details.

    """


    class MetaOapg:
        required = {
            "disclosure",
            "images",
            "name",
            "description",
            "countries",
            "id",
            "category",
            "currency_codes",
        }
        
        class properties:
            description = schemas.StrSchema
            
            
            class id(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'[A-Z0-9]{4,20}',
                    }]
            name = schemas.StrSchema
            
            
            class category(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ach": "ACH",
                        "charity": "CHARITY",
                        "merchant_card": "MERCHANT_CARD",
                        "paypal": "PAYPAL",
                        "venmo": "VENMO",
                        "visa_card": "VISA_CARD",
                    }
                
                @schemas.classproperty
                def ACH(cls):
                    return cls("ach")
                
                @schemas.classproperty
                def CHARITY(cls):
                    return cls("charity")
                
                @schemas.classproperty
                def MERCHANT_CARD(cls):
                    return cls("merchant_card")
                
                @schemas.classproperty
                def PAYPAL(cls):
                    return cls("paypal")
                
                @schemas.classproperty
                def VENMO(cls):
                    return cls("venmo")
                
                @schemas.classproperty
                def VISA_CARD(cls):
                    return cls("visa_card")
            disclosure = schemas.StrSchema
        
            @staticmethod
            def currency_codes() -> typing.Type['ProductCurrencyCodes']:
                return ProductCurrencyCodes
        
            @staticmethod
            def countries() -> typing.Type['ProductCountries']:
                return ProductCountries
        
            @staticmethod
            def images() -> typing.Type['ProductImages']:
                return ProductImages
        
            @staticmethod
            def skus() -> typing.Type['ProductSkus']:
                return ProductSkus
            __annotations__ = {
                "description": description,
                "id": id,
                "name": name,
                "category": category,
                "disclosure": disclosure,
                "currency_codes": currency_codes,
                "countries": countries,
                "images": images,
                "skus": skus,
            }
    
    disclosure: MetaOapg.properties.disclosure
    images: 'ProductImages'
    name: MetaOapg.properties.name
    description: MetaOapg.properties.description
    countries: 'ProductCountries'
    id: MetaOapg.properties.id
    category: MetaOapg.properties.category
    currency_codes: 'ProductCurrencyCodes'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["disclosure"]) -> MetaOapg.properties.disclosure: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency_codes"]) -> 'ProductCurrencyCodes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countries"]) -> 'ProductCountries': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["images"]) -> 'ProductImages': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["skus"]) -> 'ProductSkus': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "id", "name", "category", "disclosure", "currency_codes", "countries", "images", "skus", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["disclosure"]) -> MetaOapg.properties.disclosure: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency_codes"]) -> 'ProductCurrencyCodes': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countries"]) -> 'ProductCountries': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["images"]) -> 'ProductImages': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["skus"]) -> typing.Union['ProductSkus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "id", "name", "category", "disclosure", "currency_codes", "countries", "images", "skus", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        disclosure: typing.Union[MetaOapg.properties.disclosure, str, ],
        images: 'ProductImages',
        name: typing.Union[MetaOapg.properties.name, str, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        countries: 'ProductCountries',
        id: typing.Union[MetaOapg.properties.id, str, ],
        category: typing.Union[MetaOapg.properties.category, str, ],
        currency_codes: 'ProductCurrencyCodes',
        skus: typing.Union['ProductSkus', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Product':
        return super().__new__(
            cls,
            *args,
            disclosure=disclosure,
            images=images,
            name=name,
            description=description,
            countries=countries,
            id=id,
            category=category,
            currency_codes=currency_codes,
            skus=skus,
            _configuration=_configuration,
            **kwargs,
        )

from tremendous_python_sdk.model.product_countries import ProductCountries
from tremendous_python_sdk.model.product_currency_codes import ProductCurrencyCodes
from tremendous_python_sdk.model.product_images import ProductImages
from tremendous_python_sdk.model.product_skus import ProductSkus