# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import urllib3
from urllib3._collections import HTTPHeaderDict

from petstore_api import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401

# body param


class SchemaForRequestBodyApplicationXWwwFormUrlencoded(
    schemas.DictSchema
):


    class MetaOapg:
        required = {
            "number",
            "pattern_without_delimiter",
            "byte",
            "double",
        }
        
        class properties:
            
            
            class integer(
                schemas.IntSchema
            ):
                pass
            
            
            class int32(
                schemas.Int32Schema
            ):
                pass
            int64 = schemas.Int64Schema
            
            
            class number(
                schemas.NumberSchema
            ):
                pass
            
            
            class _float(
                schemas.Float32Schema
            ):
                pass
            
            
            class double(
                schemas.Float64Schema
            ):
                pass
            
            
            class string(
                schemas.StrSchema
            ):
                pass
            
            
            class pattern_without_delimiter(
                schemas.StrSchema
            ):
                pass
            byte = schemas.StrSchema
            binary = schemas.BinarySchema
            date = schemas.DateSchema
            dateTime = schemas.DateTimeSchema
            
            
            class password(
                schemas.StrSchema
            ):
                pass
            callback = schemas.StrSchema
            __annotations__ = {
                "integer": integer,
                "int32": int32,
                "int64": int64,
                "number": number,
                "float": _float,
                "double": double,
                "string": string,
                "pattern_without_delimiter": pattern_without_delimiter,
                "byte": byte,
                "binary": binary,
                "date": date,
                "dateTime": dateTime,
                "password": password,
                "callback": callback,
            }
    
    number: MetaOapg.properties.number
    pattern_without_delimiter: MetaOapg.properties.pattern_without_delimiter
    byte: MetaOapg.properties.byte
    double: MetaOapg.properties.double
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["integer"]) -> MetaOapg.properties.integer: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["int32"]) -> MetaOapg.properties.int32: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["int64"]) -> MetaOapg.properties.int64: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["float"]) -> MetaOapg.properties._float: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["double"]) -> MetaOapg.properties.double: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["string"]) -> MetaOapg.properties.string: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["pattern_without_delimiter"]) -> MetaOapg.properties.pattern_without_delimiter: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["byte"]) -> MetaOapg.properties.byte: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["binary"]) -> MetaOapg.properties.binary: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["dateTime"]) -> MetaOapg.properties.dateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["callback"]) -> MetaOapg.properties.callback: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing.Literal["integer", "int32", "int64", "number", "float", "double", "string", "pattern_without_delimiter", "byte", "binary", "date", "dateTime", "password", "callback", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing.Literal["integer"]) -> typing.Union[MetaOapg.properties.integer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing.Literal["int32"]) -> typing.Union[MetaOapg.properties.int32, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing.Literal["int64"]) -> typing.Union[MetaOapg.properties.int64, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing.Literal["float"]) -> typing.Union[MetaOapg.properties._float, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing.Literal["double"]) -> MetaOapg.properties.double: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing.Literal["string"]) -> typing.Union[MetaOapg.properties.string, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing.Literal["pattern_without_delimiter"]) -> MetaOapg.properties.pattern_without_delimiter: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing.Literal["byte"]) -> MetaOapg.properties.byte: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing.Literal["binary"]) -> typing.Union[MetaOapg.properties.binary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing.Literal["date"]) -> typing.Union[MetaOapg.properties.date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing.Literal["dateTime"]) -> typing.Union[MetaOapg.properties.dateTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing.Literal["password"]) -> typing.Union[MetaOapg.properties.password, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing.Literal["callback"]) -> typing.Union[MetaOapg.properties.callback, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing.Literal["integer", "int32", "int64", "number", "float", "double", "string", "pattern_without_delimiter", "byte", "binary", "date", "dateTime", "password", "callback", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        number: typing.Union[MetaOapg.properties.number, decimal.Decimal, int, float, ],
        pattern_without_delimiter: typing.Union[MetaOapg.properties.pattern_without_delimiter, str, ],
        byte: typing.Union[MetaOapg.properties.byte, str, ],
        double: typing.Union[MetaOapg.properties.double, decimal.Decimal, int, float, ],
        integer: typing.Union[MetaOapg.properties.integer, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        int32: typing.Union[MetaOapg.properties.int32, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        int64: typing.Union[MetaOapg.properties.int64, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        string: typing.Union[MetaOapg.properties.string, str, schemas.Unset] = schemas.unset,
        binary: typing.Union[MetaOapg.properties.binary, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        date: typing.Union[MetaOapg.properties.date, str, date, schemas.Unset] = schemas.unset,
        dateTime: typing.Union[MetaOapg.properties.dateTime, str, datetime, schemas.Unset] = schemas.unset,
        password: typing.Union[MetaOapg.properties.password, str, schemas.Unset] = schemas.unset,
        callback: typing.Union[MetaOapg.properties.callback, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaForRequestBodyApplicationXWwwFormUrlencoded':
        return super().__new__(
            cls,
            *args,
            number=number,
            pattern_without_delimiter=pattern_without_delimiter,
            byte=byte,
            double=double,
            integer=integer,
            int32=int32,
            int64=int64,
            string=string,
            binary=binary,
            date=date,
            dateTime=dateTime,
            password=password,
            callback=callback,
            _configuration=_configuration,
            **kwargs,
        )


class BaseApi(api_client.Api):

    def _endpoint_parameters_oapg(
        self: api_client.Api,
        body: typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        content_type: str = 'application/x-www-form-urlencoded',
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
        Fake endpoint for testing various parameters 假端點 偽のエンドポイント 가짜 엔드 포인트 
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling

        _fields = None
        _body = None
        if body is not schemas.unset:
            serialized_data = request_body_body.serialize(body, content_type)
            _headers.add('Content-Type', content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=used_path,
            method='post'.upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response


class EndpointParameters(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def endpoint_parameters(
        self: BaseApi,
        body: typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        content_type: str = 'application/x-www-form-urlencoded',
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._endpoint_parameters_oapg(
            body=body,
            content_type=content_type,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    def post(
        self: BaseApi,
        body: typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        content_type: str = 'application/x-www-form-urlencoded',
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._endpoint_parameters_oapg(
            body=body,
            content_type=content_type,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


