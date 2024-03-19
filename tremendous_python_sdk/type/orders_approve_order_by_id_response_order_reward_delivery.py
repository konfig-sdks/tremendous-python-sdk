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


class RequiredOrdersApproveOrderByIdResponseOrderRewardDelivery(TypedDict):
    # How to deliver the reward to the recipient.  <table>   <thead>     <tr>       <th>Delivery Method</th>       <th>Description</th>     </tr>   </thead>   <tbody>     <tr>       <td><code>EMAIL</code></td>       <td>Deliver the reward to the recipient by email</td>     </tr>     <tr>       <td><code>LINK</code></td>       <td>         <p>Deliver the reward to the recipient via a link.</p>         <p>The link can be retrieved on a successfully ordered reward via the <code>/rewards</code> or <code>/rewards/{id}</code> endpoint. That link must then be  delivered to the recipient out-of-band.</p>       </td>     </tr>     <tr>       <td><code>PHONE</code></td>       <td>Deliver the reward to the recipient by SMS</td>     </tr>   </tbody> </table> 
    method: str

    # Current status of the delivery of the reward:  * `SCHEDULED` - Reward is scheduled for delivery and will be delivered soon. * `FAILED` - Delivery of reward failed (e.g. email bounced). * `SUCCEEDED` - Reward was successfully delivered (email or text message delivered or reward link opened). * `PENDING` - Delivery is pending but not yet scheduled. 
    status: str

class OptionalOrdersApproveOrderByIdResponseOrderRewardDelivery(TypedDict, total=False):
    pass

class OrdersApproveOrderByIdResponseOrderRewardDelivery(RequiredOrdersApproveOrderByIdResponseOrderRewardDelivery, OptionalOrdersApproveOrderByIdResponseOrderRewardDelivery):
    pass
