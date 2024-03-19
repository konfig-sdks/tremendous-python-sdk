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

from tremendous_python_sdk.type.orders_create_order_response_order_payment import OrdersCreateOrderResponseOrderPayment
from tremendous_python_sdk.type.orders_create_order_response_order_rewards import OrdersCreateOrderResponseOrderRewards

class RequiredOrdersCreateOrderResponseOrder(TypedDict):
    # Tremendous ID of the order
    id: str

    # Date the order has been created
    created_at: datetime

    # Execution status of a given order  <table>   <thead>     <tr>       <th>         Status       </th>       <th>         Description       </th>     </tr>   </thead>   <tbody>     <tr>       <td>         <code>           CANCELED         </code>       </td>       <td>         The order and all of its rewards were canceled.       </td>     </tr>     <tr>       <td>         <code>           CART         </code>       </td>       <td>         The order has been created, but hasn't yet been processed.       </td>     </tr>     <tr>       <td>         <code>           EXECUTED         </code>       </td>       <td>         The order has been executed. Payment has been handled and rewards are being delivered (if applicable).       </td>     </tr>     <tr>       <td>         <code>           FAILED         </code>       </td>       <td>         The order could not be processed due to an error. E.g. due to insufficient funds in the account.       </td>     </tr>     <tr>       <td>         <code>           PENDING APPROVAL         </code>       </td>       <td>         The order has been created but needs approval to be executed.       </td>     </tr>     <tr>       <td>         <code>           PENDING INTERNAL PAYMENT APPROVAL         </code>       </td>       <td>         The order has been created but it is under review and requires approval from our team.       </td>     </tr>    </tbody> </table> 
    status: str

class OptionalOrdersCreateOrderResponseOrder(TypedDict, total=False):
    # Reference for this order, supplied by the customer.  When set, `external_id` makes order idempotent. All requests that use the same `external_id` after the initial order creation, will result in a response that returns the data of the initially created order. The response will have a `201` response code. These responses **fail** to create any further orders.  It also allows for retrieving by `external_id` instead of `id` only. 
    external_id: typing.Optional[str]

    # ID of the campaign in your account, that defines the available products (different gift cards, charity, etc.) that the recipient can choose from. 
    campaign_id: typing.Optional[str]

    payment: OrdersCreateOrderResponseOrderPayment

    # The ID for the invoice associated with this order
    invoice_id: str

    rewards: OrdersCreateOrderResponseOrderRewards

class OrdersCreateOrderResponseOrder(RequiredOrdersCreateOrderResponseOrder, OptionalOrdersCreateOrderResponseOrder):
    pass
