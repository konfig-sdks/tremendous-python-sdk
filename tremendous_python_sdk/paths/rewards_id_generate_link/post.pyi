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

from tremendous_python_sdk.model.rewards_generate_link500_response import RewardsGenerateLink500Response as RewardsGenerateLink500ResponseSchema
from tremendous_python_sdk.model.rewards_generate_link_response import RewardsGenerateLinkResponse as RewardsGenerateLinkResponseSchema
from tremendous_python_sdk.model.rewards_generate_link429_response import RewardsGenerateLink429Response as RewardsGenerateLink429ResponseSchema
from tremendous_python_sdk.model.rewards_generate_link403_response import RewardsGenerateLink403Response as RewardsGenerateLink403ResponseSchema
from tremendous_python_sdk.model.rewards_generate_link401_response import RewardsGenerateLink401Response as RewardsGenerateLink401ResponseSchema
from tremendous_python_sdk.model.rewards_generate_link404_response import RewardsGenerateLink404Response as RewardsGenerateLink404ResponseSchema

from tremendous_python_sdk.type.rewards_generate_link_response import RewardsGenerateLinkResponse
from tremendous_python_sdk.type.rewards_generate_link404_response import RewardsGenerateLink404Response
from tremendous_python_sdk.type.rewards_generate_link403_response import RewardsGenerateLink403Response
from tremendous_python_sdk.type.rewards_generate_link429_response import RewardsGenerateLink429Response
from tremendous_python_sdk.type.rewards_generate_link500_response import RewardsGenerateLink500Response
from tremendous_python_sdk.type.rewards_generate_link401_response import RewardsGenerateLink401Response

from ...api_client import Dictionary
from tremendous_python_sdk.pydantic.rewards_generate_link_response import RewardsGenerateLinkResponse as RewardsGenerateLinkResponsePydantic
from tremendous_python_sdk.pydantic.rewards_generate_link401_response import RewardsGenerateLink401Response as RewardsGenerateLink401ResponsePydantic
from tremendous_python_sdk.pydantic.rewards_generate_link429_response import RewardsGenerateLink429Response as RewardsGenerateLink429ResponsePydantic
from tremendous_python_sdk.pydantic.rewards_generate_link403_response import RewardsGenerateLink403Response as RewardsGenerateLink403ResponsePydantic
from tremendous_python_sdk.pydantic.rewards_generate_link404_response import RewardsGenerateLink404Response as RewardsGenerateLink404ResponsePydantic
from tremendous_python_sdk.pydantic.rewards_generate_link500_response import RewardsGenerateLink500Response as RewardsGenerateLink500ResponsePydantic

# Path params


class IdSchema(
    schemas.StrSchema
):
    pass
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'id': typing.Union[IdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_id = api_client.PathParameter(
    name="id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = RewardsGenerateLinkResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: RewardsGenerateLinkResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: RewardsGenerateLinkResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = RewardsGenerateLink401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: RewardsGenerateLink401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: RewardsGenerateLink401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = RewardsGenerateLink403ResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: RewardsGenerateLink403Response


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: RewardsGenerateLink403Response


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = RewardsGenerateLink404ResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: RewardsGenerateLink404Response


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: RewardsGenerateLink404Response


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor429ResponseBodyApplicationJson = RewardsGenerateLink429ResponseSchema


@dataclass
class ApiResponseFor429(api_client.ApiResponse):
    body: RewardsGenerateLink429Response


@dataclass
class ApiResponseFor429Async(api_client.AsyncApiResponse):
    body: RewardsGenerateLink429Response


_response_for_429 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor429,
    response_cls_async=ApiResponseFor429Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor429ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = RewardsGenerateLink500ResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: RewardsGenerateLink500Response


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: RewardsGenerateLink500Response


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

    def _generate_link_mapped_args(
        self,
        id: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if id is not None:
            _path_params["id"] = id
        args.path = _path_params
        return args

    async def _agenerate_link_oapg(
        self,
            path_params: typing.Optional[dict] = {},
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
        Generate a reward URL
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/rewards/{id}/generate_link',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
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


    def _generate_link_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Generate a reward URL
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/rewards/{id}/generate_link',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
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


class GenerateLinkRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def agenerate_link(
        self,
        id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._generate_link_mapped_args(
            id=id,
        )
        return await self._agenerate_link_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def generate_link(
        self,
        id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._generate_link_mapped_args(
            id=id,
        )
        return self._generate_link_oapg(
            path_params=args.path,
        )

class GenerateLink(BaseApi):

    async def agenerate_link(
        self,
        id: str,
        validate: bool = False,
        **kwargs,
    ) -> RewardsGenerateLinkResponsePydantic:
        raw_response = await self.raw.agenerate_link(
            id=id,
            **kwargs,
        )
        if validate:
            return RewardsGenerateLinkResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(RewardsGenerateLinkResponsePydantic, raw_response.body)
    
    
    def generate_link(
        self,
        id: str,
        validate: bool = False,
    ) -> RewardsGenerateLinkResponsePydantic:
        raw_response = self.raw.generate_link(
            id=id,
        )
        if validate:
            return RewardsGenerateLinkResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(RewardsGenerateLinkResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._generate_link_mapped_args(
            id=id,
        )
        return await self._agenerate_link_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._generate_link_mapped_args(
            id=id,
        )
        return self._generate_link_oapg(
            path_params=args.path,
        )

