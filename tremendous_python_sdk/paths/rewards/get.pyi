# coding: utf-8

"""
    API Endpoints

    Deliver monetary rewards and incentives to employees, customers, survey participants, and more through the Tremendous API. For organizational tasks, like managing your organization and it's members within Tremendous, please see the Tremendous Organizational API.

    The version of the OpenAPI document: 2
    Contact: developers@tremendous.com
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from tremendous_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from tremendous_python_sdk.api_response import AsyncGeneratorResponse
from tremendous_python_sdk import api_client, exceptions
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

from tremendous_python_sdk.model.rewards_list_all_rewards500_response import RewardsListAllRewards500Response as RewardsListAllRewards500ResponseSchema
from tremendous_python_sdk.model.rewards_list_all_rewards_response import RewardsListAllRewardsResponse as RewardsListAllRewardsResponseSchema
from tremendous_python_sdk.model.rewards_list_all_rewards429_response import RewardsListAllRewards429Response as RewardsListAllRewards429ResponseSchema
from tremendous_python_sdk.model.rewards_list_all_rewards401_response import RewardsListAllRewards401Response as RewardsListAllRewards401ResponseSchema

from tremendous_python_sdk.type.rewards_list_all_rewards429_response import RewardsListAllRewards429Response
from tremendous_python_sdk.type.rewards_list_all_rewards401_response import RewardsListAllRewards401Response
from tremendous_python_sdk.type.rewards_list_all_rewards_response import RewardsListAllRewardsResponse
from tremendous_python_sdk.type.rewards_list_all_rewards500_response import RewardsListAllRewards500Response

from ...api_client import Dictionary
from tremendous_python_sdk.pydantic.rewards_list_all_rewards429_response import RewardsListAllRewards429Response as RewardsListAllRewards429ResponsePydantic
from tremendous_python_sdk.pydantic.rewards_list_all_rewards_response import RewardsListAllRewardsResponse as RewardsListAllRewardsResponsePydantic
from tremendous_python_sdk.pydantic.rewards_list_all_rewards401_response import RewardsListAllRewards401Response as RewardsListAllRewards401ResponsePydantic
from tremendous_python_sdk.pydantic.rewards_list_all_rewards500_response import RewardsListAllRewards500Response as RewardsListAllRewards500ResponsePydantic

# Query params
OffsetSchema = schemas.IntSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'offset': typing.Union[OffsetSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_offset = api_client.QueryParameter(
    name="offset",
    style=api_client.ParameterStyle.FORM,
    schema=OffsetSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = RewardsListAllRewardsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: RewardsListAllRewardsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: RewardsListAllRewardsResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = RewardsListAllRewards401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: RewardsListAllRewards401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: RewardsListAllRewards401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor429ResponseBodyApplicationJson = RewardsListAllRewards429ResponseSchema


@dataclass
class ApiResponseFor429(api_client.ApiResponse):
    body: RewardsListAllRewards429Response


@dataclass
class ApiResponseFor429Async(api_client.AsyncApiResponse):
    body: RewardsListAllRewards429Response


_response_for_429 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor429,
    response_cls_async=ApiResponseFor429Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor429ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = RewardsListAllRewards500ResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: RewardsListAllRewards500Response


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: RewardsListAllRewards500Response


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_all_rewards_mapped_args(
        self,
        offset: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if offset is not None:
            _query_params["offset"] = offset
        args.query = _query_params
        return args

    async def _alist_all_rewards_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        List rewards
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_offset,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/rewards',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _list_all_rewards_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        List rewards
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_offset,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/rewards',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class ListAllRewardsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_all_rewards(
        self,
        offset: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_all_rewards_mapped_args(
            offset=offset,
        )
        return await self._alist_all_rewards_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list_all_rewards(
        self,
        offset: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_all_rewards_mapped_args(
            offset=offset,
        )
        return self._list_all_rewards_oapg(
            query_params=args.query,
        )

class ListAllRewards(BaseApi):

    async def alist_all_rewards(
        self,
        offset: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> RewardsListAllRewardsResponsePydantic:
        raw_response = await self.raw.alist_all_rewards(
            offset=offset,
            **kwargs,
        )
        if validate:
            return RewardsListAllRewardsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(RewardsListAllRewardsResponsePydantic, raw_response.body)
    
    
    def list_all_rewards(
        self,
        offset: typing.Optional[int] = None,
        validate: bool = False,
    ) -> RewardsListAllRewardsResponsePydantic:
        raw_response = self.raw.list_all_rewards(
            offset=offset,
        )
        if validate:
            return RewardsListAllRewardsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(RewardsListAllRewardsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        offset: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_all_rewards_mapped_args(
            offset=offset,
        )
        return await self._alist_all_rewards_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        offset: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_all_rewards_mapped_args(
            offset=offset,
        )
        return self._list_all_rewards_oapg(
            query_params=args.query,
        )
