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


class ProductCurrencyCodes(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Available currencies for this product
    """


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
            
            @schemas.classproperty
            def USD(cls):
                return cls("USD")
            
            @schemas.classproperty
            def CAD(cls):
                return cls("CAD")
            
            @schemas.classproperty
            def EUR(cls):
                return cls("EUR")
            
            @schemas.classproperty
            def AED(cls):
                return cls("AED")
            
            @schemas.classproperty
            def AFN(cls):
                return cls("AFN")
            
            @schemas.classproperty
            def ALL(cls):
                return cls("ALL")
            
            @schemas.classproperty
            def AMD(cls):
                return cls("AMD")
            
            @schemas.classproperty
            def ARS(cls):
                return cls("ARS")
            
            @schemas.classproperty
            def AUD(cls):
                return cls("AUD")
            
            @schemas.classproperty
            def AZN(cls):
                return cls("AZN")
            
            @schemas.classproperty
            def BAM(cls):
                return cls("BAM")
            
            @schemas.classproperty
            def BDT(cls):
                return cls("BDT")
            
            @schemas.classproperty
            def BGN(cls):
                return cls("BGN")
            
            @schemas.classproperty
            def BHD(cls):
                return cls("BHD")
            
            @schemas.classproperty
            def BIF(cls):
                return cls("BIF")
            
            @schemas.classproperty
            def BND(cls):
                return cls("BND")
            
            @schemas.classproperty
            def BOB(cls):
                return cls("BOB")
            
            @schemas.classproperty
            def BRL(cls):
                return cls("BRL")
            
            @schemas.classproperty
            def BWP(cls):
                return cls("BWP")
            
            @schemas.classproperty
            def BYR(cls):
                return cls("BYR")
            
            @schemas.classproperty
            def BZD(cls):
                return cls("BZD")
            
            @schemas.classproperty
            def CDF(cls):
                return cls("CDF")
            
            @schemas.classproperty
            def CHF(cls):
                return cls("CHF")
            
            @schemas.classproperty
            def CLP(cls):
                return cls("CLP")
            
            @schemas.classproperty
            def CNY(cls):
                return cls("CNY")
            
            @schemas.classproperty
            def COP(cls):
                return cls("COP")
            
            @schemas.classproperty
            def CRC(cls):
                return cls("CRC")
            
            @schemas.classproperty
            def CVE(cls):
                return cls("CVE")
            
            @schemas.classproperty
            def CZK(cls):
                return cls("CZK")
            
            @schemas.classproperty
            def DJF(cls):
                return cls("DJF")
            
            @schemas.classproperty
            def DKK(cls):
                return cls("DKK")
            
            @schemas.classproperty
            def DOP(cls):
                return cls("DOP")
            
            @schemas.classproperty
            def DZD(cls):
                return cls("DZD")
            
            @schemas.classproperty
            def EEK(cls):
                return cls("EEK")
            
            @schemas.classproperty
            def EGP(cls):
                return cls("EGP")
            
            @schemas.classproperty
            def ERN(cls):
                return cls("ERN")
            
            @schemas.classproperty
            def ETB(cls):
                return cls("ETB")
            
            @schemas.classproperty
            def GBP(cls):
                return cls("GBP")
            
            @schemas.classproperty
            def GEL(cls):
                return cls("GEL")
            
            @schemas.classproperty
            def GHS(cls):
                return cls("GHS")
            
            @schemas.classproperty
            def GNF(cls):
                return cls("GNF")
            
            @schemas.classproperty
            def GTQ(cls):
                return cls("GTQ")
            
            @schemas.classproperty
            def HKD(cls):
                return cls("HKD")
            
            @schemas.classproperty
            def HNL(cls):
                return cls("HNL")
            
            @schemas.classproperty
            def HRK(cls):
                return cls("HRK")
            
            @schemas.classproperty
            def HUF(cls):
                return cls("HUF")
            
            @schemas.classproperty
            def IDR(cls):
                return cls("IDR")
            
            @schemas.classproperty
            def ILS(cls):
                return cls("ILS")
            
            @schemas.classproperty
            def INR(cls):
                return cls("INR")
            
            @schemas.classproperty
            def IQD(cls):
                return cls("IQD")
            
            @schemas.classproperty
            def IRR(cls):
                return cls("IRR")
            
            @schemas.classproperty
            def ISK(cls):
                return cls("ISK")
            
            @schemas.classproperty
            def JMD(cls):
                return cls("JMD")
            
            @schemas.classproperty
            def JOD(cls):
                return cls("JOD")
            
            @schemas.classproperty
            def JPY(cls):
                return cls("JPY")
            
            @schemas.classproperty
            def KES(cls):
                return cls("KES")
            
            @schemas.classproperty
            def KHR(cls):
                return cls("KHR")
            
            @schemas.classproperty
            def KRW(cls):
                return cls("KRW")
            
            @schemas.classproperty
            def KWD(cls):
                return cls("KWD")
            
            @schemas.classproperty
            def KZT(cls):
                return cls("KZT")
            
            @schemas.classproperty
            def LBP(cls):
                return cls("LBP")
            
            @schemas.classproperty
            def LKR(cls):
                return cls("LKR")
            
            @schemas.classproperty
            def LTL(cls):
                return cls("LTL")
            
            @schemas.classproperty
            def LVL(cls):
                return cls("LVL")
            
            @schemas.classproperty
            def MAD(cls):
                return cls("MAD")
            
            @schemas.classproperty
            def MDL(cls):
                return cls("MDL")
            
            @schemas.classproperty
            def MGA(cls):
                return cls("MGA")
            
            @schemas.classproperty
            def MKD(cls):
                return cls("MKD")
            
            @schemas.classproperty
            def MMK(cls):
                return cls("MMK")
            
            @schemas.classproperty
            def MOP(cls):
                return cls("MOP")
            
            @schemas.classproperty
            def MUR(cls):
                return cls("MUR")
            
            @schemas.classproperty
            def MXN(cls):
                return cls("MXN")
            
            @schemas.classproperty
            def MYR(cls):
                return cls("MYR")
            
            @schemas.classproperty
            def MZN(cls):
                return cls("MZN")
            
            @schemas.classproperty
            def NAD(cls):
                return cls("NAD")
            
            @schemas.classproperty
            def NGN(cls):
                return cls("NGN")
            
            @schemas.classproperty
            def NIO(cls):
                return cls("NIO")
            
            @schemas.classproperty
            def NOK(cls):
                return cls("NOK")
            
            @schemas.classproperty
            def NPR(cls):
                return cls("NPR")
            
            @schemas.classproperty
            def NZD(cls):
                return cls("NZD")
            
            @schemas.classproperty
            def OMR(cls):
                return cls("OMR")
            
            @schemas.classproperty
            def PAB(cls):
                return cls("PAB")
            
            @schemas.classproperty
            def PEN(cls):
                return cls("PEN")
            
            @schemas.classproperty
            def PHP(cls):
                return cls("PHP")
            
            @schemas.classproperty
            def PKR(cls):
                return cls("PKR")
            
            @schemas.classproperty
            def PLN(cls):
                return cls("PLN")
            
            @schemas.classproperty
            def PYG(cls):
                return cls("PYG")
            
            @schemas.classproperty
            def QAR(cls):
                return cls("QAR")
            
            @schemas.classproperty
            def RON(cls):
                return cls("RON")
            
            @schemas.classproperty
            def RSD(cls):
                return cls("RSD")
            
            @schemas.classproperty
            def RUB(cls):
                return cls("RUB")
            
            @schemas.classproperty
            def RWF(cls):
                return cls("RWF")
            
            @schemas.classproperty
            def SAR(cls):
                return cls("SAR")
            
            @schemas.classproperty
            def SDG(cls):
                return cls("SDG")
            
            @schemas.classproperty
            def SEK(cls):
                return cls("SEK")
            
            @schemas.classproperty
            def SGD(cls):
                return cls("SGD")
            
            @schemas.classproperty
            def SOS(cls):
                return cls("SOS")
            
            @schemas.classproperty
            def SYP(cls):
                return cls("SYP")
            
            @schemas.classproperty
            def THB(cls):
                return cls("THB")
            
            @schemas.classproperty
            def TND(cls):
                return cls("TND")
            
            @schemas.classproperty
            def TOP(cls):
                return cls("TOP")
            
            @schemas.classproperty
            def TRY(cls):
                return cls("TRY")
            
            @schemas.classproperty
            def TTD(cls):
                return cls("TTD")
            
            @schemas.classproperty
            def TWD(cls):
                return cls("TWD")
            
            @schemas.classproperty
            def TZS(cls):
                return cls("TZS")
            
            @schemas.classproperty
            def UAH(cls):
                return cls("UAH")
            
            @schemas.classproperty
            def UGX(cls):
                return cls("UGX")
            
            @schemas.classproperty
            def UYU(cls):
                return cls("UYU")
            
            @schemas.classproperty
            def UZS(cls):
                return cls("UZS")
            
            @schemas.classproperty
            def VEF(cls):
                return cls("VEF")
            
            @schemas.classproperty
            def VND(cls):
                return cls("VND")
            
            @schemas.classproperty
            def XAF(cls):
                return cls("XAF")
            
            @schemas.classproperty
            def XOF(cls):
                return cls("XOF")
            
            @schemas.classproperty
            def YER(cls):
                return cls("YER")
            
            @schemas.classproperty
            def ZAR(cls):
                return cls("ZAR")
            
            @schemas.classproperty
            def ZMK(cls):
                return cls("ZMK")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ProductCurrencyCodes':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
