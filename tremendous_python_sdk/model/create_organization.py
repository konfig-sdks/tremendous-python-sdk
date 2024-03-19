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


class CreateOrganization(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "website",
            "name",
        }
        
        class properties:
            name = schemas.StrSchema
            website = schemas.StrSchema
            with_api_key = schemas.BoolSchema
        
            @staticmethod
            def copy_settings() -> typing.Type['CreateOrganizationCopySettings']:
                return CreateOrganizationCopySettings
            phone = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "website": website,
                "with_api_key": with_api_key,
                "copy_settings": copy_settings,
                "phone": phone,
            }
    
    website: MetaOapg.properties.website
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["website"]) -> MetaOapg.properties.website: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["with_api_key"]) -> MetaOapg.properties.with_api_key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["copy_settings"]) -> 'CreateOrganizationCopySettings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.properties.phone: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "website", "with_api_key", "copy_settings", "phone", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["website"]) -> MetaOapg.properties.website: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["with_api_key"]) -> typing.Union[MetaOapg.properties.with_api_key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["copy_settings"]) -> typing.Union['CreateOrganizationCopySettings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone"]) -> typing.Union[MetaOapg.properties.phone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "website", "with_api_key", "copy_settings", "phone", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        website: typing.Union[MetaOapg.properties.website, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        with_api_key: typing.Union[MetaOapg.properties.with_api_key, bool, schemas.Unset] = schemas.unset,
        copy_settings: typing.Union['CreateOrganizationCopySettings', schemas.Unset] = schemas.unset,
        phone: typing.Union[MetaOapg.properties.phone, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateOrganization':
        return super().__new__(
            cls,
            *args,
            website=website,
            name=name,
            with_api_key=with_api_key,
            copy_settings=copy_settings,
            phone=phone,
            _configuration=_configuration,
            **kwargs,
        )

from tremendous_python_sdk.model.create_organization_copy_settings import CreateOrganizationCopySettings
