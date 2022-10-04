# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
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

from petstore_api import schemas  # noqa: F401


class Capitalization(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            smallCamel = schemas.StrSchema
            CapitalCamel = schemas.StrSchema
            small_Snake = schemas.StrSchema
            Capital_Snake = schemas.StrSchema
            SCA_ETH_Flow_Points = schemas.StrSchema
            ATT_NAME = schemas.StrSchema
            __annotations__ = {
                "smallCamel": smallCamel,
                "CapitalCamel": CapitalCamel,
                "small_Snake": small_Snake,
                "Capital_Snake": Capital_Snake,
                "SCA_ETH_Flow_Points": SCA_ETH_Flow_Points,
                "ATT_NAME": ATT_NAME,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["smallCamel"]) -> MetaOapg.properties.smallCamel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CapitalCamel"]) -> MetaOapg.properties.CapitalCamel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["small_Snake"]) -> MetaOapg.properties.small_Snake: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Capital_Snake"]) -> MetaOapg.properties.Capital_Snake: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SCA_ETH_Flow_Points"]) -> MetaOapg.properties.SCA_ETH_Flow_Points: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ATT_NAME"]) -> MetaOapg.properties.ATT_NAME: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["smallCamel", "CapitalCamel", "small_Snake", "Capital_Snake", "SCA_ETH_Flow_Points", "ATT_NAME", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["smallCamel"]) -> typing.Union[MetaOapg.properties.smallCamel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CapitalCamel"]) -> typing.Union[MetaOapg.properties.CapitalCamel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["small_Snake"]) -> typing.Union[MetaOapg.properties.small_Snake, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Capital_Snake"]) -> typing.Union[MetaOapg.properties.Capital_Snake, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SCA_ETH_Flow_Points"]) -> typing.Union[MetaOapg.properties.SCA_ETH_Flow_Points, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ATT_NAME"]) -> typing.Union[MetaOapg.properties.ATT_NAME, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["smallCamel", "CapitalCamel", "small_Snake", "Capital_Snake", "SCA_ETH_Flow_Points", "ATT_NAME", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        smallCamel: typing.Union[MetaOapg.properties.smallCamel, str, schemas.Unset] = schemas.unset,
        CapitalCamel: typing.Union[MetaOapg.properties.CapitalCamel, str, schemas.Unset] = schemas.unset,
        small_Snake: typing.Union[MetaOapg.properties.small_Snake, str, schemas.Unset] = schemas.unset,
        Capital_Snake: typing.Union[MetaOapg.properties.Capital_Snake, str, schemas.Unset] = schemas.unset,
        SCA_ETH_Flow_Points: typing.Union[MetaOapg.properties.SCA_ETH_Flow_Points, str, schemas.Unset] = schemas.unset,
        ATT_NAME: typing.Union[MetaOapg.properties.ATT_NAME, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Capitalization':
        return super().__new__(
            cls,
            *args,
            smallCamel=smallCamel,
            CapitalCamel=CapitalCamel,
            small_Snake=small_Snake,
            Capital_Snake=Capital_Snake,
            SCA_ETH_Flow_Points=SCA_ETH_Flow_Points,
            ATT_NAME=ATT_NAME,
            _configuration=_configuration,
            **kwargs,
        )
