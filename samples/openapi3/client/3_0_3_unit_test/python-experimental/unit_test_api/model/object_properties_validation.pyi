# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from unit_test_api import schemas  # noqa: F401


class ObjectPropertiesValidation(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            foo = schemas.IntSchema
            bar = schemas.StrSchema
            __annotations__ = {
                "foo": foo,
                "bar": bar,
            }

    
    @typing.overload
    def __getitem__(self, name: typing.Literal["foo"]) -> MetaOapg.properties.foo: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["bar"]) -> MetaOapg.properties.bar: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing.Literal["foo", "bar", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing.Literal["foo"]) -> typing.Union[MetaOapg.properties.foo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing.Literal["bar"]) -> typing.Union[MetaOapg.properties.bar, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing.Literal["foo", "bar", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, ],
        foo: typing.Union[MetaOapg.properties.foo, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        bar: typing.Union[MetaOapg.properties.bar, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ObjectPropertiesValidation':
        return super().__new__(
            cls,
            *args,
            foo=foo,
            bar=bar,
            _configuration=_configuration,
            **kwargs,
        )
