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


class OrderStatus(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Execution status of a given order

<table>
  <thead>
    <tr>
      <th>
        Status
      </th>
      <th>
        Description
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <code>
          CANCELED
        </code>
      </td>
      <td>
        The order and all of its rewards were canceled.
      </td>
    </tr>
    <tr>
      <td>
        <code>
          CART
        </code>
      </td>
      <td>
        The order has been created, but hasn't yet been processed.
      </td>
    </tr>
    <tr>
      <td>
        <code>
          EXECUTED
        </code>
      </td>
      <td>
        The order has been executed. Payment has been handled and rewards are being delivered (if applicable).
      </td>
    </tr>
    <tr>
      <td>
        <code>
          FAILED
        </code>
      </td>
      <td>
        The order could not be processed due to an error. E.g. due to insufficient funds in the account.
      </td>
    </tr>
    <tr>
      <td>
        <code>
          PENDING APPROVAL
        </code>
      </td>
      <td>
        The order has been created but needs approval to be executed.
      </td>
    </tr>
    <tr>
      <td>
        <code>
          PENDING INTERNAL PAYMENT APPROVAL
        </code>
      </td>
      <td>
        The order has been created but it is under review and requires approval from our team.
      </td>
    </tr>

  </tbody>
</table>

    """


    class MetaOapg:
        enum_value_to_name = {
            "CANCELED": "CANCELED",
            "CART": "CART",
            "EXECUTED": "EXECUTED",
            "FAILED": "FAILED",
            "PENDING APPROVAL": "PENDING_APPROVAL",
            "PENDING INTERNAL PAYMENT APPROVAL": "PENDING_INTERNAL_PAYMENT_APPROVAL",
        }
    
    @schemas.classproperty
    def CANCELED(cls):
        return cls("CANCELED")
    
    @schemas.classproperty
    def CART(cls):
        return cls("CART")
    
    @schemas.classproperty
    def EXECUTED(cls):
        return cls("EXECUTED")
    
    @schemas.classproperty
    def FAILED(cls):
        return cls("FAILED")
    
    @schemas.classproperty
    def PENDING_APPROVAL(cls):
        return cls("PENDING APPROVAL")
    
    @schemas.classproperty
    def PENDING_INTERNAL_PAYMENT_APPROVAL(cls):
        return cls("PENDING INTERNAL PAYMENT APPROVAL")
