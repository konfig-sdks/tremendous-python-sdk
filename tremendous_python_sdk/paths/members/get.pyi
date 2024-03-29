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

from tremendous_python_sdk.model.members_list_members_response import MembersListMembersResponse as MembersListMembersResponseSchema
from tremendous_python_sdk.model.members_list_members429_response import MembersListMembers429Response as MembersListMembers429ResponseSchema
from tremendous_python_sdk.model.members_list_members401_response import MembersListMembers401Response as MembersListMembers401ResponseSchema
from tremendous_python_sdk.model.members_list_members500_response import MembersListMembers500Response as MembersListMembers500ResponseSchema

from tremendous_python_sdk.type.members_list_members429_response import MembersListMembers429Response
from tremendous_python_sdk.type.members_list_members500_response import MembersListMembers500Response
from tremendous_python_sdk.type.members_list_members401_response import MembersListMembers401Response
from tremendous_python_sdk.type.members_list_members_response import MembersListMembersResponse

from ...api_client import Dictionary
from tremendous_python_sdk.pydantic.members_list_members500_response import MembersListMembers500Response as MembersListMembers500ResponsePydantic
from tremendous_python_sdk.pydantic.members_list_members401_response import MembersListMembers401Response as MembersListMembers401ResponsePydantic
from tremendous_python_sdk.pydantic.members_list_members_response import MembersListMembersResponse as MembersListMembersResponsePydantic
from tremendous_python_sdk.pydantic.members_list_members429_response import MembersListMembers429Response as MembersListMembers429ResponsePydantic

SchemaFor200ResponseBodyApplicationJson = MembersListMembersResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: MembersListMembersResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: MembersListMembersResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = MembersListMembers401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: MembersListMembers401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: MembersListMembers401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor429ResponseBodyApplicationJson = MembersListMembers429ResponseSchema


@dataclass
class ApiResponseFor429(api_client.ApiResponse):
    body: MembersListMembers429Response


@dataclass
class ApiResponseFor429Async(api_client.AsyncApiResponse):
    body: MembersListMembers429Response


_response_for_429 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor429,
    response_cls_async=ApiResponseFor429Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor429ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = MembersListMembers500ResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: MembersListMembers500Response


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: MembersListMembers500Response


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

    def _list_members_mapped_args(
        self,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        return args

    async def _alist_members_oapg(
        self,
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
        List members
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
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
            path_template='/members',
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


    def _list_members_oapg(
        self,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        List members
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
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
            path_template='/members',
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


class ListMembersRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_members(
        self,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_members_mapped_args(
        )
        return await self._alist_members_oapg(
            **kwargs,
        )
    
    def list_members(
        self,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_members_mapped_args(
        )
        return self._list_members_oapg(
        )

class ListMembers(BaseApi):

    async def alist_members(
        self,
        validate: bool = False,
        **kwargs,
    ) -> MembersListMembersResponsePydantic:
        raw_response = await self.raw.alist_members(
            **kwargs,
        )
        if validate:
            return MembersListMembersResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(MembersListMembersResponsePydantic, raw_response.body)
    
    
    def list_members(
        self,
        validate: bool = False,
    ) -> MembersListMembersResponsePydantic:
        raw_response = self.raw.list_members(
        )
        if validate:
            return MembersListMembersResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(MembersListMembersResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_members_mapped_args(
        )
        return await self._alist_members_oapg(
            **kwargs,
        )
    
    def get(
        self,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_members_mapped_args(
        )
        return self._list_members_oapg(
        )

