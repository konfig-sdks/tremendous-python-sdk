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

from tremendous_python_sdk.type.products_get_by_id_response_product_countries import ProductsGetByIdResponseProductCountries
from tremendous_python_sdk.type.products_get_by_id_response_product_currency_codes import ProductsGetByIdResponseProductCurrencyCodes
from tremendous_python_sdk.type.products_get_by_id_response_product_images import ProductsGetByIdResponseProductImages
from tremendous_python_sdk.type.products_get_by_id_response_product_skus import ProductsGetByIdResponseProductSkus

class RequiredProductsGetByIdResponseProduct(TypedDict):
    # Detailed description of the product. Mostly used for products with a `category` of `charities`.
    description: str

    id: str

    # Name of the product
    name: str

    # The category of this product  <table>   <thead>     <tr>       <th>Category</th>       <th>Description</th>     </tr>   </thead>   <tbody>     <tr>       <td><code>ach</code></td>       <td>Bank transfer to the recipient</td>     </tr>     <tr>       <td><code>charity</code></td>       <td>Donations to a charity</td>     </tr>     <tr>       <td><code>merchant_card</code></td>       <td>A gift card for a certain merchant (e.g. Amazon)</td>     </tr>     <tr>       <td><code>paypal</code></td>       <td>Payout via PayPal</td>     </tr>     <tr>       <td><code>venmo</code></td>       <td>Payout via Venmo</td>     </tr>     <tr>       <td><code>visa_card</code></td>       <td>Payout in form of a Visa debit card</td>     </tr>   </tbody> </table> 
    category: str

    # Legal disclosures for this product. Can be in HTML format.
    disclosure: str

    currency_codes: ProductsGetByIdResponseProductCurrencyCodes

    countries: ProductsGetByIdResponseProductCountries

    images: ProductsGetByIdResponseProductImages

class OptionalProductsGetByIdResponseProduct(TypedDict, total=False):
    skus: ProductsGetByIdResponseProductSkus

class ProductsGetByIdResponseProduct(RequiredProductsGetByIdResponseProduct, OptionalProductsGetByIdResponseProduct):
    pass
