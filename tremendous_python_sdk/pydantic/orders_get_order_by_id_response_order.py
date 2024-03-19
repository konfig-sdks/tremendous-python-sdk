# coding: utf-8

"""
    API Endpoints

    Deliver monetary rewards and incentives to employees, customers, survey participants, and more through the Tremendous API. For organizational tasks, like managing your organization and it's members within Tremendous, please see the Tremendous Organizational API.

    The version of the OpenAPI document: 2
    Contact: developers@tremendous.com
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from tremendous_python_sdk.pydantic.orders_get_order_by_id_response_order_payment import OrdersGetOrderByIdResponseOrderPayment
from tremendous_python_sdk.pydantic.orders_get_order_by_id_response_order_reward import OrdersGetOrderByIdResponseOrderReward

class OrdersGetOrderByIdResponseOrder(BaseModel):
    # Tremendous ID of the order
    id: str = Field(alias='id')

    # Date the order has been created
    created_at: datetime = Field(alias='created_at')

    # Execution status of a given order  <table>   <thead>     <tr>       <th>         Status       </th>       <th>         Description       </th>     </tr>   </thead>   <tbody>     <tr>       <td>         <code>           CANCELED         </code>       </td>       <td>         The order and all of its rewards were canceled.       </td>     </tr>     <tr>       <td>         <code>           CART         </code>       </td>       <td>         The order has been created, but hasn't yet been processed.       </td>     </tr>     <tr>       <td>         <code>           EXECUTED         </code>       </td>       <td>         The order has been executed. Payment has been handled and rewards are being delivered (if applicable).       </td>     </tr>     <tr>       <td>         <code>           FAILED         </code>       </td>       <td>         The order could not be processed due to an error. E.g. due to insufficient funds in the account.       </td>     </tr>     <tr>       <td>         <code>           PENDING APPROVAL         </code>       </td>       <td>         The order has been created but needs approval to be executed.       </td>     </tr>     <tr>       <td>         <code>           PENDING INTERNAL PAYMENT APPROVAL         </code>       </td>       <td>         The order has been created but it is under review and requires approval from our team.       </td>     </tr>    </tbody> </table> 
    status: Literal["CANCELED", "CART", "EXECUTED", "FAILED", "PENDING APPROVAL", "PENDING INTERNAL PAYMENT APPROVAL"] = Field(alias='status')

    # Reference for this order, supplied by the customer.  When set, `external_id` makes order idempotent. All requests that use the same `external_id` after the initial order creation, will result in a response that returns the data of the initially created order. The response will have a `201` response code. These responses **fail** to create any further orders.  It also allows for retrieving by `external_id` instead of `id` only. 
    external_id: typing.Optional[typing.Optional[str]] = Field(None, alias='external_id')

    # ID of the campaign in your account, that defines the available products (different gift cards, charity, etc.) that the recipient can choose from. 
    campaign_id: typing.Optional[typing.Optional[str]] = Field(None, alias='campaign_id')

    payment: typing.Optional[OrdersGetOrderByIdResponseOrderPayment] = Field(None, alias='payment')

    # The ID for the invoice associated with this order
    invoice_id: typing.Optional[str] = Field(None, alias='invoice_id')

    reward: typing.Optional[OrdersGetOrderByIdResponseOrderReward] = Field(None, alias='reward')
    class Config:
        arbitrary_types_allowed = True
