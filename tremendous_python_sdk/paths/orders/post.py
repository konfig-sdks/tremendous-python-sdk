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

from tremendous_python_sdk.model.orders_create_order_request_reward import OrdersCreateOrderRequestReward as OrdersCreateOrderRequestRewardSchema
from tremendous_python_sdk.model.orders_create_order_request_payment import OrdersCreateOrderRequestPayment as OrdersCreateOrderRequestPaymentSchema
from tremendous_python_sdk.model.orders_create_order500_response import OrdersCreateOrder500Response as OrdersCreateOrder500ResponseSchema
from tremendous_python_sdk.model.orders_create_order401_response import OrdersCreateOrder401Response as OrdersCreateOrder401ResponseSchema
from tremendous_python_sdk.model.orders_create_order_request import OrdersCreateOrderRequest as OrdersCreateOrderRequestSchema
from tremendous_python_sdk.model.orders_create_order201_response import OrdersCreateOrder201Response as OrdersCreateOrder201ResponseSchema
from tremendous_python_sdk.model.orders_create_order402_response import OrdersCreateOrder402Response as OrdersCreateOrder402ResponseSchema
from tremendous_python_sdk.model.orders_create_order422_response import OrdersCreateOrder422Response as OrdersCreateOrder422ResponseSchema
from tremendous_python_sdk.model.orders_create_order429_response import OrdersCreateOrder429Response as OrdersCreateOrder429ResponseSchema
from tremendous_python_sdk.model.orders_create_order_response import OrdersCreateOrderResponse as OrdersCreateOrderResponseSchema
from tremendous_python_sdk.model.orders_create_order400_response import OrdersCreateOrder400Response as OrdersCreateOrder400ResponseSchema
from tremendous_python_sdk.model.orders_create_order202_response import OrdersCreateOrder202Response as OrdersCreateOrder202ResponseSchema

from tremendous_python_sdk.type.orders_create_order402_response import OrdersCreateOrder402Response
from tremendous_python_sdk.type.orders_create_order_request import OrdersCreateOrderRequest
from tremendous_python_sdk.type.orders_create_order429_response import OrdersCreateOrder429Response
from tremendous_python_sdk.type.orders_create_order500_response import OrdersCreateOrder500Response
from tremendous_python_sdk.type.orders_create_order400_response import OrdersCreateOrder400Response
from tremendous_python_sdk.type.orders_create_order_response import OrdersCreateOrderResponse
from tremendous_python_sdk.type.orders_create_order_request_reward import OrdersCreateOrderRequestReward
from tremendous_python_sdk.type.orders_create_order201_response import OrdersCreateOrder201Response
from tremendous_python_sdk.type.orders_create_order_request_payment import OrdersCreateOrderRequestPayment
from tremendous_python_sdk.type.orders_create_order422_response import OrdersCreateOrder422Response
from tremendous_python_sdk.type.orders_create_order401_response import OrdersCreateOrder401Response
from tremendous_python_sdk.type.orders_create_order202_response import OrdersCreateOrder202Response

from ...api_client import Dictionary
from tremendous_python_sdk.pydantic.orders_create_order429_response import OrdersCreateOrder429Response as OrdersCreateOrder429ResponsePydantic
from tremendous_python_sdk.pydantic.orders_create_order202_response import OrdersCreateOrder202Response as OrdersCreateOrder202ResponsePydantic
from tremendous_python_sdk.pydantic.orders_create_order_request import OrdersCreateOrderRequest as OrdersCreateOrderRequestPydantic
from tremendous_python_sdk.pydantic.orders_create_order_request_reward import OrdersCreateOrderRequestReward as OrdersCreateOrderRequestRewardPydantic
from tremendous_python_sdk.pydantic.orders_create_order201_response import OrdersCreateOrder201Response as OrdersCreateOrder201ResponsePydantic
from tremendous_python_sdk.pydantic.orders_create_order401_response import OrdersCreateOrder401Response as OrdersCreateOrder401ResponsePydantic
from tremendous_python_sdk.pydantic.orders_create_order500_response import OrdersCreateOrder500Response as OrdersCreateOrder500ResponsePydantic
from tremendous_python_sdk.pydantic.orders_create_order422_response import OrdersCreateOrder422Response as OrdersCreateOrder422ResponsePydantic
from tremendous_python_sdk.pydantic.orders_create_order_response import OrdersCreateOrderResponse as OrdersCreateOrderResponsePydantic
from tremendous_python_sdk.pydantic.orders_create_order400_response import OrdersCreateOrder400Response as OrdersCreateOrder400ResponsePydantic
from tremendous_python_sdk.pydantic.orders_create_order_request_payment import OrdersCreateOrderRequestPayment as OrdersCreateOrderRequestPaymentPydantic
from tremendous_python_sdk.pydantic.orders_create_order402_response import OrdersCreateOrder402Response as OrdersCreateOrder402ResponsePydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = OrdersCreateOrderRequestSchema


request_body_orders_create_order_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'BearerApiKey',
]
SchemaFor200ResponseBodyApplicationJson = OrdersCreateOrderResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: OrdersCreateOrderResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: OrdersCreateOrderResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor201ResponseBodyApplicationJson = OrdersCreateOrder201ResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: OrdersCreateOrder201Response


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: OrdersCreateOrder201Response


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
SchemaFor202ResponseBodyApplicationJson = OrdersCreateOrder202ResponseSchema


@dataclass
class ApiResponseFor202(api_client.ApiResponse):
    body: OrdersCreateOrder202Response


@dataclass
class ApiResponseFor202Async(api_client.AsyncApiResponse):
    body: OrdersCreateOrder202Response


_response_for_202 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor202,
    response_cls_async=ApiResponseFor202Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor202ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = OrdersCreateOrder400ResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: OrdersCreateOrder400Response


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: OrdersCreateOrder400Response


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = OrdersCreateOrder401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: OrdersCreateOrder401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: OrdersCreateOrder401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor402ResponseBodyApplicationJson = OrdersCreateOrder402ResponseSchema


@dataclass
class ApiResponseFor402(api_client.ApiResponse):
    body: OrdersCreateOrder402Response


@dataclass
class ApiResponseFor402Async(api_client.AsyncApiResponse):
    body: OrdersCreateOrder402Response


_response_for_402 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor402,
    response_cls_async=ApiResponseFor402Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor402ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = OrdersCreateOrder422ResponseSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: OrdersCreateOrder422Response


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: OrdersCreateOrder422Response


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
SchemaFor429ResponseBodyApplicationJson = OrdersCreateOrder429ResponseSchema


@dataclass
class ApiResponseFor429(api_client.ApiResponse):
    body: OrdersCreateOrder429Response


@dataclass
class ApiResponseFor429Async(api_client.AsyncApiResponse):
    body: OrdersCreateOrder429Response


_response_for_429 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor429,
    response_cls_async=ApiResponseFor429Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor429ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = OrdersCreateOrder500ResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: OrdersCreateOrder500Response


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: OrdersCreateOrder500Response


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '201': _response_for_201,
    '202': _response_for_202,
    '400': _response_for_400,
    '401': _response_for_401,
    '402': _response_for_402,
    '422': _response_for_422,
    '429': _response_for_429,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_order_mapped_args(
        self,
        payment: OrdersCreateOrderRequestPayment,
        reward: OrdersCreateOrderRequestReward,
        external_id: typing.Optional[typing.Optional[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if external_id is not None:
            _body["external_id"] = external_id
        if payment is not None:
            _body["payment"] = payment
        if reward is not None:
            _body["reward"] = reward
        args.body = _body
        return args

    async def _acreate_order_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor201Async,
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create order
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/orders',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_orders_create_order_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


    def _create_order_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create order
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/orders',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_orders_create_order_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


class CreateOrderRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_order(
        self,
        payment: OrdersCreateOrderRequestPayment,
        reward: OrdersCreateOrderRequestReward,
        external_id: typing.Optional[typing.Optional[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor201Async,
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_order_mapped_args(
            payment=payment,
            reward=reward,
            external_id=external_id,
        )
        return await self._acreate_order_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_order(
        self,
        payment: OrdersCreateOrderRequestPayment,
        reward: OrdersCreateOrderRequestReward,
        external_id: typing.Optional[typing.Optional[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_order_mapped_args(
            payment=payment,
            reward=reward,
            external_id=external_id,
        )
        return self._create_order_oapg(
            body=args.body,
        )

class CreateOrder(BaseApi):

    async def acreate_order(
        self,
        payment: OrdersCreateOrderRequestPayment,
        reward: OrdersCreateOrderRequestReward,
        external_id: typing.Optional[typing.Optional[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> OrdersCreateOrderResponsePydantic:
        raw_response = await self.raw.acreate_order(
            payment=payment,
            reward=reward,
            external_id=external_id,
            **kwargs,
        )
        if validate:
            return OrdersCreateOrderResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(OrdersCreateOrderResponsePydantic, raw_response.body)
    
    
    def create_order(
        self,
        payment: OrdersCreateOrderRequestPayment,
        reward: OrdersCreateOrderRequestReward,
        external_id: typing.Optional[typing.Optional[str]] = None,
        validate: bool = False,
    ) -> OrdersCreateOrderResponsePydantic:
        raw_response = self.raw.create_order(
            payment=payment,
            reward=reward,
            external_id=external_id,
        )
        if validate:
            return OrdersCreateOrderResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(OrdersCreateOrderResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        payment: OrdersCreateOrderRequestPayment,
        reward: OrdersCreateOrderRequestReward,
        external_id: typing.Optional[typing.Optional[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor201Async,
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_order_mapped_args(
            payment=payment,
            reward=reward,
            external_id=external_id,
        )
        return await self._acreate_order_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        payment: OrdersCreateOrderRequestPayment,
        reward: OrdersCreateOrderRequestReward,
        external_id: typing.Optional[typing.Optional[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_order_mapped_args(
            payment=payment,
            reward=reward,
            external_id=external_id,
        )
        return self._create_order_oapg(
            body=args.body,
        )

