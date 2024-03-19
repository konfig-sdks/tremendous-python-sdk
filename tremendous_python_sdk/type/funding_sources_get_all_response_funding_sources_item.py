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

from tremendous_python_sdk.type.funding_sources_get_all_response_funding_sources_item_meta import FundingSourcesGetAllResponseFundingSourcesItemMeta

class RequiredFundingSourcesGetAllResponseFundingSourcesItem(TypedDict):
    id: str

    # You can pay for rewards using different payment methods on Tremendous:  <table>   <thead>     <tr>       <th>Payment Method</th>       <th>Description</th>       </tr>   </thead>   <tbody>     <tr>       <td><code>balance</code></td>       <td>Pre-funded balance in your Tremendous account to draw funds from to send rewards to recipients.</td>     </tr>     <tr>       <td><code>bank_account</code></td>       <td>Bank account to draw funds from to send rewards to recipients.</td>     </tr>     <tr>       <td><code>credit_card</code></td>       <td>Credit card to draw funds from to send rewards to recipients.</td>     </tr>     <tr>       <td><code>invoice</code></td>       <td>Send rewards to recipients and pay by invoice.</td>     </tr>    </tbody> </table> 
    method: str

    meta: FundingSourcesGetAllResponseFundingSourcesItemMeta

class OptionalFundingSourcesGetAllResponseFundingSourcesItem(TypedDict, total=False):
    # **Only available when `method` is set to `invoice`.** 
    type: str

class FundingSourcesGetAllResponseFundingSourcesItem(RequiredFundingSourcesGetAllResponseFundingSourcesItem, OptionalFundingSourcesGetAllResponseFundingSourcesItem):
    pass
