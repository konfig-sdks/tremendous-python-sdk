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


class OrganizationsCreateNewOrganizationResponseOrganization(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Organizations are a way to separate different parts of your business within the same Tremendous account.
Your root Tremendous account is an organization itself and can have multiple sub-organizations.

You can assign users in your Tremendous team as members to any organization. Users can be members of multiple
organizations at once.

Each organizations can have it's own API key.

    """


    class MetaOapg:
        required = {
            "website",
            "name",
        }
        
        class properties:
            name = schemas.StrSchema
            website = schemas.StrSchema
            
            
            class id(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'[A-Z0-9]{4,20}',
                    }]
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "PENDING": "PENDING",
                        "APPROVED": "APPROVED",
                        "REJECTED": "REJECTED",
                    }
                
                @schemas.classproperty
                def PENDING(cls):
                    return cls("PENDING")
                
                @schemas.classproperty
                def APPROVED(cls):
                    return cls("APPROVED")
                
                @schemas.classproperty
                def REJECTED(cls):
                    return cls("REJECTED")
            created_at = schemas.DateSchema
            api_key = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "website": website,
                "id": id,
                "status": status,
                "created_at": created_at,
                "api_key": api_key,
            }
    
    website: MetaOapg.properties.website
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["website"]) -> MetaOapg.properties.website: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["api_key"]) -> MetaOapg.properties.api_key: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "website", "id", "status", "created_at", "api_key", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["website"]) -> MetaOapg.properties.website: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["api_key"]) -> typing.Union[MetaOapg.properties.api_key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "website", "id", "status", "created_at", "api_key", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        website: typing.Union[MetaOapg.properties.website, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, date, schemas.Unset] = schemas.unset,
        api_key: typing.Union[MetaOapg.properties.api_key, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OrganizationsCreateNewOrganizationResponseOrganization':
        return super().__new__(
            cls,
            *args,
            website=website,
            name=name,
            id=id,
            status=status,
            created_at=created_at,
            api_key=api_key,
            _configuration=_configuration,
            **kwargs,
        )
