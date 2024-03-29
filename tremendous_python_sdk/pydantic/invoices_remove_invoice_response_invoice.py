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

from tremendous_python_sdk.pydantic.invoices_remove_invoice_response_invoice_orders import InvoicesRemoveInvoiceResponseInvoiceOrders
from tremendous_python_sdk.pydantic.invoices_remove_invoice_response_invoice_rewards import InvoicesRemoveInvoiceResponseInvoiceRewards

class InvoicesRemoveInvoiceResponseInvoice(BaseModel):
    # The invoice number
    id: str = Field(alias='id')

    # Amount of the invoice in USD
    amount: typing.Union[int, float] = Field(alias='amount')

    # Status of this invoice  <table>   <thead>     <tr>       <th>Status</th>       <th>Description</th>     </tr>   </thead>   <tbody>     <tr>       <td><code>DELETED</code></td>       <td>Invoice has been deleted by your organization</td>     </tr>     <tr>       <td><code>PAID</code></td>       <td>Invoice has been paid by your organization</td>     </tr>     <tr>       <td><code>OPEN</code></td>       <td>Invoice has been created by your organization but has not been paid, yet</td>     </tr>   </tbody> </table> 
    status: Literal["DELETED", "PAID", "OPEN", "MARKED_AS_PAID"] = Field(alias='status')

    # Timestamp of when the invoice has been created. 
    created_at: date = Field(alias='created_at')

    # Timestamp of when the invoice has been paid. 
    paid_at: typing.Optional[date] = Field(alias='paid_at')

    # Reference to the purchase order number within your organization
    po_number: typing.Optional[typing.Optional[str]] = Field(None, alias='po_number')

    orders: typing.Optional[InvoicesRemoveInvoiceResponseInvoiceOrders] = Field(None, alias='orders')

    rewards: typing.Optional[InvoicesRemoveInvoiceResponseInvoiceRewards] = Field(None, alias='rewards')
    class Config:
        arbitrary_types_allowed = True
