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


class FundingSourcesGetByIdResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "funding_source",
        }
        
        class properties:
        
            @staticmethod
            def funding_source() -> typing.Type['FundingSourcesGetByIdResponseFundingSource']:
                return FundingSourcesGetByIdResponseFundingSource
            __annotations__ = {
                "funding_source": funding_source,
            }
    
    funding_source: 'FundingSourcesGetByIdResponseFundingSource'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["funding_source"]) -> 'FundingSourcesGetByIdResponseFundingSource': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["funding_source", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["funding_source"]) -> 'FundingSourcesGetByIdResponseFundingSource': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["funding_source", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        funding_source: 'FundingSourcesGetByIdResponseFundingSource',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FundingSourcesGetByIdResponse':
        return super().__new__(
            cls,
            *args,
            funding_source=funding_source,
            _configuration=_configuration,
            **kwargs,
        )

from tremendous_python_sdk.model.funding_sources_get_by_id_response_funding_source import FundingSourcesGetByIdResponseFundingSource
