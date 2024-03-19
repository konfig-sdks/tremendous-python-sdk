<div align="left">

[![Visit Tremendous](./header.png)](https://www.tremendous.com&#x2F;)

# Tremendous<a id="tremendous"></a>

Deliver monetary rewards and incentives to employees, customers, survey participants, and more through the Tremendous API. For organizational tasks, like managing your organization and it's members within Tremendous, please see the Tremendous Organizational API.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`tremendous.balance_transactions.list_all`](#tremendousbalance_transactionslist_all)
  * [`tremendous.campaigns.get_all`](#tremendouscampaignsget_all)
  * [`tremendous.campaigns.get_by_id`](#tremendouscampaignsget_by_id)
  * [`tremendous.fields.get_custom_fields`](#tremendousfieldsget_custom_fields)
  * [`tremendous.funding_sources.get_all`](#tremendousfunding_sourcesget_all)
  * [`tremendous.funding_sources.get_by_id`](#tremendousfunding_sourcesget_by_id)
  * [`tremendous.invoices.create_and_fund_account_balance`](#tremendousinvoicescreate_and_fund_account_balance)
- [Request body](#request-body)
  * [`tremendous.invoices.get_all`](#tremendousinvoicesget_all)
  * [`tremendous.invoices.get_by_id`](#tremendousinvoicesget_by_id)
  * [`tremendous.invoices.get_csv`](#tremendousinvoicesget_csv)
  * [`tremendous.invoices.get_pdf`](#tremendousinvoicesget_pdf)
  * [`tremendous.invoices.remove_invoice`](#tremendousinvoicesremove_invoice)
  * [`tremendous.members.create_new_member`](#tremendousmemberscreate_new_member)
  * [Permissions](#permissions)
  * [Inviting new members](#inviting-new-members)
  * [`tremendous.members.get_member`](#tremendousmembersget_member)
  * [`tremendous.members.list_members`](#tremendousmemberslist_members)
  * [`tremendous.orders.approve_order_by_id`](#tremendousordersapprove_order_by_id)
  * [`tremendous.orders.create_order`](#tremendousorderscreate_order)
- [Request body](#request-body-1)
  * [Funding sources](#funding-sources)
  * [Idempotence](#idempotence)
  * [`tremendous.orders.get_list`](#tremendousordersget_list)
  * [`tremendous.orders.get_order_by_id`](#tremendousordersget_order_by_id)
  * [`tremendous.orders.reject_by_id`](#tremendousordersreject_by_id)
  * [`tremendous.organizations.create_api_key`](#tremendousorganizationscreate_api_key)
  * [`tremendous.organizations.create_new_organization`](#tremendousorganizationscreate_new_organization)
  * [`tremendous.organizations.get_list`](#tremendousorganizationsget_list)
  * [`tremendous.organizations.get_organization`](#tremendousorganizationsget_organization)
  * [`tremendous.products.get_by_id`](#tremendousproductsget_by_id)
  * [`tremendous.products.get_list`](#tremendousproductsget_list)
  * [`tremendous.rewards.generate_embed_token`](#tremendousrewardsgenerate_embed_token)
  * [`tremendous.rewards.generate_link`](#tremendousrewardsgenerate_link)
  * [`tremendous.rewards.get_single_reward`](#tremendousrewardsget_single_reward)
  * [`tremendous.rewards.list_all_rewards`](#tremendousrewardslist_all_rewards)
  * [`tremendous.rewards.resend_reward_by_id`](#tremendousrewardsresend_reward_by_id)
  * [`tremendous.webhooks.create_webhook`](#tremendouswebhookscreate_webhook)
- [Request body](#request-body-2)
  * [`tremendous.webhooks.get_details`](#tremendouswebhooksget_details)
  * [`tremendous.webhooks.get_details_0`](#tremendouswebhooksget_details_0)
  * [`tremendous.webhooks.list_events`](#tremendouswebhookslist_events)
  * [`tremendous.webhooks.trigger_event`](#tremendouswebhookstrigger_event)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Tremendous&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from tremendous_python_sdk import Tremendous, ApiException

tremendous = Tremendous(access_token="YOUR_BEARER_TOKEN")

try:
    # List balance transactions
    list_all_response = tremendous.balance_transactions.list_all(
        offset=10,
        limit=10,
        created_at_gte="2023-07-15T18:00:00Z",
        created_at_lte="2023-08-01T18:00:00Z",
    )
    print(list_all_response)
except ApiException as e:
    print("Exception when calling BalanceTransactionsApi.list_all: %s\n" % e)
    pprint(e.body)
    if e.status == 422:
        pprint(e.body["errors"])
    if e.status == 401:
        pprint(e.body["errors"])
    if e.status == 500:
        pprint(e.body["errors"])
    if e.status == 429:
        pprint(e.body["errors"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from tremendous_python_sdk import Tremendous, ApiException

tremendous = Tremendous(access_token="YOUR_BEARER_TOKEN")


async def main():
    try:
        # List balance transactions
        list_all_response = await tremendous.balance_transactions.alist_all(
            offset=10,
            limit=10,
            created_at_gte="2023-07-15T18:00:00Z",
            created_at_lte="2023-08-01T18:00:00Z",
        )
        print(list_all_response)
    except ApiException as e:
        print("Exception when calling BalanceTransactionsApi.list_all: %s\n" % e)
        pprint(e.body)
        if e.status == 422:
            pprint(e.body["errors"])
        if e.status == 401:
            pprint(e.body["errors"])
        if e.status == 500:
            pprint(e.body["errors"])
        if e.status == 429:
            pprint(e.body["errors"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from tremendous_python_sdk import Tremendous, ApiException

tremendous = Tremendous(access_token="YOUR_BEARER_TOKEN")

try:
    # List balance transactions
    list_all_response = tremendous.balance_transactions.raw.list_all(
        offset=10,
        limit=10,
        created_at_gte="2023-07-15T18:00:00Z",
        created_at_lte="2023-08-01T18:00:00Z",
    )
    pprint(list_all_response.body)
    pprint(list_all_response.body["invoices"])
    pprint(list_all_response.headers)
    pprint(list_all_response.status)
    pprint(list_all_response.round_trip_time)
except ApiException as e:
    print("Exception when calling BalanceTransactionsApi.list_all: %s\n" % e)
    pprint(e.body)
    if e.status == 422:
        pprint(e.body["errors"])
    if e.status == 401:
        pprint(e.body["errors"])
    if e.status == 500:
        pprint(e.body["errors"])
    if e.status == 429:
        pprint(e.body["errors"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `tremendous.balance_transactions.list_all`<a id="tremendousbalance_transactionslist_all"></a>

Fetch a list of all balance transactions on your account.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = tremendous.balance_transactions.list_all(
    offset=10,
    limit=10,
    created_at_gte="2023-07-15T18:00:00Z",
    created_at_lte="2023-08-01T18:00:00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### offset: `int`<a id="offset-int"></a>

Offsets the returned list by the given number of transactions. The returned transactions are ordered (and offsetted) by their creation date (DESC).

##### limit: `int`<a id="limit-int"></a>

Limits the number of transactions listed. The default value is 10.

##### created_at_gte: `str`<a id="created_at_gte-str"></a>

Only return results where the created_at field is greater than or equal to the supplied value. The string needs to be an ISO 8601 datetime.

##### created_at_lte: `str`<a id="created_at_lte-str"></a>

Only return results where the created_at field is less than or equal to the supplied value. The string needs to be an ISO 8601 datetime.

#### 🔄 Return<a id="🔄-return"></a>

[`BalanceTransactionsListAllResponse`](./tremendous_python_sdk/pydantic/balance_transactions_list_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/balance_transactions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.campaigns.get_all`<a id="tremendouscampaignsget_all"></a>

Retrieve a list of all campaigns created in your account


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = tremendous.campaigns.get_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CampaignsGetAllResponse`](./tremendous_python_sdk/pydantic/campaigns_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/campaigns` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.campaigns.get_by_id`<a id="tremendouscampaignsget_by_id"></a>

Retrieve a campaign, identified by the given `id` in the URL


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = tremendous.campaigns.get_by_id(
    id="SOMEIDSOMEID",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

ID of the campaign that should be retrieved

#### 🔄 Return<a id="🔄-return"></a>

[`CampaignsGetByIdResponse`](./tremendous_python_sdk/pydantic/campaigns_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/campaigns/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.fields.get_custom_fields`<a id="tremendousfieldsget_custom_fields"></a>

For reporting and analytics purposes, custom fields can be associated with rewards generated through the API. Custom fields must be first added by members of your admin team through the Tremendous Dashboard.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_custom_fields_response = tremendous.fields.get_custom_fields()
```

#### 🔄 Return<a id="🔄-return"></a>

[`FieldsGetCustomFieldsResponse`](./tremendous_python_sdk/pydantic/fields_get_custom_fields_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/fields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.funding_sources.get_all`<a id="tremendousfunding_sourcesget_all"></a>

Retrieve a list of all funding sources available for ordering through the API in your organization's account.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = tremendous.funding_sources.get_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`FundingSourcesGetAllResponse`](./tremendous_python_sdk/pydantic/funding_sources_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/funding_sources` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.funding_sources.get_by_id`<a id="tremendousfunding_sourcesget_by_id"></a>

Retrieve a funding source, identified by the given `id` in the URL


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = tremendous.funding_sources.get_by_id(
    id="SOMEIDSOMEID",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

ID of the funding source that should be retrieved

#### 🔄 Return<a id="🔄-return"></a>

[`FundingSourcesGetByIdResponse`](./tremendous_python_sdk/pydantic/funding_sources_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/funding_sources/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.invoices.create_and_fund_account_balance`<a id="tremendousinvoicescreate_and_fund_account_balance"></a>

Creating an invoice is the way for your organization to fund your account's balance.

1. Create an invoice
2. Pay the invoice
3. Funds get added to your account's balance

## Request body<a id="request-body"></a>

<div class="object-schema-request-schema">
  <table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody class="object-schema-table-body">
    <tr class=""><td><div class="property-name">
  <code class="property-name">po_number</code>
</div>
</td><td><span class="property-type">string</span></td><td><p>Reference to the purchase order number within your organization</p>
</td></tr>
<tr class=""><td><div class="property-name">
  <code class="property-name">amount</code>
</div>
</td><td><span class="property-type">number</span> <span class="property-format">double</span></td><td><p>Amount of the invoice in USD</p>
</td></tr>
<tr class=""><td><div class="property-name">
  <code class="property-name">memo</code>
</div>
</td><td><span class="property-type">string</span></td><td><p>A note to be included in the invoice. This is for your internal use and will not be visible to the recipient.</p>
</td></tr>
  </tbody>
</table>

</div>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_and_fund_account_balance_response = (
    tremendous.invoices.create_and_fund_account_balance(
        amount=50.35,
        po_number="123-PO-EE",
        memo="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

Amount of the invoice in USD

##### po_number: `Optional[str]`<a id="po_number-optionalstr"></a>

Reference to the purchase order number within your organization

##### memo: `Optional[str]`<a id="memo-optionalstr"></a>

A note to be included in the invoice. This is for your internal use and will not be visible to the recipient. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`InvoicesCreateAndFundAccountBalanceRequest`](./tremendous_python_sdk/type/invoices_create_and_fund_account_balance_request.py)
Invoice details

#### 🔄 Return<a id="🔄-return"></a>

[`InvoicesCreateAndFundAccountBalanceResponse`](./tremendous_python_sdk/pydantic/invoices_create_and_fund_account_balance_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/invoices` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.invoices.get_all`<a id="tremendousinvoicesget_all"></a>

Fetch a list of all invoices on your account.

> 🚧 Deleted invoices are omitted
>
> The response does not include any previously deleted invoices.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = tremendous.invoices.get_all(
    offset=10,
    limit=10,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### offset: `int`<a id="offset-int"></a>

Offsets the returned list by the given number of invoices. The returned invoices are ordered (and offsetted) by their creation date (DESC).

##### limit: `int`<a id="limit-int"></a>

Limits the number of invoices listed. The maximum and default value is 10.

#### 🔄 Return<a id="🔄-return"></a>

[`InvoicesGetAllResponse`](./tremendous_python_sdk/pydantic/invoices_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/invoices` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.invoices.get_by_id`<a id="tremendousinvoicesget_by_id"></a>

Retrieve an invoice, identified by the given `id` in the URL

> 📘 Deleted Invoices
>
> This endpoint can be used to retrieve details on deleted invoices
> that the list of invoices omits.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = tremendous.invoices.get_by_id(
    id="PPS-26873",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

ID of the invoice that should be retrieved

#### 🔄 Return<a id="🔄-return"></a>

[`InvoicesGetByIdResponse`](./tremendous_python_sdk/pydantic/invoices_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/invoices/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.invoices.get_csv`<a id="tremendousinvoicesget_csv"></a>

Generates a CSV version for an invoice listing the associated rewards and orders


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_csv_response = tremendous.invoices.get_csv(
    id="PPS-26873",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

ID of the Invoice for that the CSV should be generated

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/invoices/{id}/csv` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.invoices.get_pdf`<a id="tremendousinvoicesget_pdf"></a>

Generates a PDF version for an invoice


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_pdf_response = tremendous.invoices.get_pdf(
    id="PPS-26873",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

ID of the Invoice for that the PDF should be generated

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/invoices/{id}/pdf` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.invoices.remove_invoice`<a id="tremendousinvoicesremove_invoice"></a>

Removes an invoice. This has no further consequences but is a rather cosmetic operation.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_invoice_response = tremendous.invoices.remove_invoice(
    id="PPS-26873",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

ID of the invoice that should be retrieved

#### 🔄 Return<a id="🔄-return"></a>

[`InvoicesRemoveInvoiceResponse`](./tremendous_python_sdk/pydantic/invoices_remove_invoice_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/invoices/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.members.create_new_member`<a id="tremendousmemberscreate_new_member"></a>

Each organization has one or more users that can access and manage that organization. These users are called members.

Members can take actions via the Tremendous web dashboard directly. These actions include adding funding sources to the organization, creating Campaigns, and more.

### Permissions<a id="permissions"></a>

Members can have one of two roles that determine their permissions within the organization:

1. `MEMBER`: Limited permissions. Can view their own reward and order histories only.
2. `ADMIN`: Update organization settings, invite other members to the organization, and view all member order and reward histories within their organization.

To create members of a sub-organizations [create an API key for that organization](https://developers.tremendous.com/) first, then use the new API key in the create member request.

### Inviting new members<a id="inviting-new-members"></a>

After creating a member, an automatic invite is sent to the email address. If the user is not registered yet, that person will then need to sign up for a Tremendous account.

> ❗️ Automatic invitations are not available in the sandbox
>
> You must manually use the returned `invite_url` field in the payload instead.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_member_response = tremendous.members.create_new_member(
    email="jane@example.com",
    name="Jane Doe",
    role="MEMBER",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

Email address of the member

##### name: `str`<a id="name-str"></a>

Full name of the member

##### role: `str`<a id="role-str"></a>

Role of the member within the organization.  <table>   <thead>     <tr>       <th>Role</th>       <th>Description</th>     </tr>   </thead>     <tr>       <td><code>MEMBER</code></td>       <td>Limited permissions. Can view their own reward and order histories only.</td>     </tr>     <tr>       <td><code>ADMIN</code></td>       <td>Update organization settings, invite other members to the organization, and view all member order and reward histories within their organization.</td>     </tr>   <tbody> </table> 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MembersCreateNewMemberRequest`](./tremendous_python_sdk/type/members_create_new_member_request.py)
Member details

#### 🔄 Return<a id="🔄-return"></a>

[`MembersCreateNewMemberResponse`](./tremendous_python_sdk/pydantic/members_create_new_member_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.members.get_member`<a id="tremendousmembersget_member"></a>

Retrieve member

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_member_response = tremendous.members.get_member(
    id="SOMEIDSOMEID",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

ID of the member to retrieve

#### 🔄 Return<a id="🔄-return"></a>

[`MembersGetMemberResponse`](./tremendous_python_sdk/pydantic/members_get_member_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.members.list_members`<a id="tremendousmemberslist_members"></a>

To list members of a sub-organization [create an API key for that organization](https://developers.tremendous.com/) first, then use the new API key in the list members request.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_members_response = tremendous.members.list_members()
```

#### 🔄 Return<a id="🔄-return"></a>

[`MembersListMembersResponse`](./tremendous_python_sdk/pydantic/members_list_members_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.orders.approve_order_by_id`<a id="tremendousordersapprove_order_by_id"></a>

Approves an order that is pending review, identified by the given `id` in the URL.

Approvals is a feature that requires orders to be approved by an organization admin
before they are sent out. To enable approvals for your organization, please enable
'Allow approvals via API' via the organization''s 'Order Approvals' settings from the Tremendous dashboard.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
approve_order_by_id_response = tremendous.orders.approve_order_by_id(
    id="SOMEIDSOMEID",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

ID of the order that should be approved. In case the order has an `external_id` reference supplied by the customer on creation, it's possible to use it instead.

#### 🔄 Return<a id="🔄-return"></a>

[`OrdersApproveOrderByIdResponse`](./tremendous_python_sdk/pydantic/orders_approve_order_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/order_approvals/{id}/approve` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.orders.create_order`<a id="tremendousorderscreate_order"></a>

Every time you want to send out a reward through Tremendous you need to create an order for it.

> 📘 Getting started with your first order
>
> Our step-by-step guide walks you through everything you need
> to send your first gift card through the Tremendous API:
>
> <strong><a style="display: block; margin-top: 20px;" href="/docs/sending-rewards-intro">Check it out!</a></strong>

## Request body<a id="request-body"></a>

<div class="object-schema-request-schema">
  <table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody class="object-schema-table-body">
    <tr class=""><td><div class="property-name">
  <code class="property-name">external_id</code>
</div>
</td><td><span class="property-type">string</span></td><td><p>Reference for this order, supplied by the customer.</p>

<p>When set, <code>external_id</code> makes order idempotent. All requests that use the same <code>external_id</code>
after the initial order creation, will result in a response that returns the data of the
initially created order. The response will have a <code>201</code> response code. These responses
<strong>fail</strong> to create any further orders.</p>

<p>It also allows for retrieving by <code>external_id</code> instead of <code>id</code> only.</p>
</td></tr>
<tr class=""><td><div class="property-name">
  <code class="property-name">payment</code>
</div>
</td><td><span class="property-type">object</span></td><td></td></tr>  <tr>
    <td colspan="3">
      <details>
        <summary>Show object properties</summary>
        <table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody class="object-schema-table-body">
    <tr class=""><td><div class="property-name">
  <code class="property-name">funding_source_id</code>
</div>
</td><td><span class="property-type">string</span></td><td><p>Tremendous ID of the funding source that will be used to pay for the order. Use <code>balance</code> to use your Tremendous&#39;s balance.</p>
</td></tr>
  </tbody>
</table>

</tr>

<tr class=""><td><div class="property-name">
  <code class="property-name">reward</code>
</div>
</td><td><span class="property-type">object</span></td><td><p>A single reward, sent to a recipient. A reward is always part of an order.</p>

<p>Either <code>products</code> or <code>campaign_id</code> must be specified.</p>
</td></tr>  <tr>
    <td colspan="3">
      <details>
        <summary>Show object properties</summary>
        <table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody class="object-schema-table-body">
    <tr class="property-conditional-hint-response-only"><td><div class="property-name">
  <code class="property-name">id</code>
</div>
</td><td><span class="property-type">string</span></td><td><p>Tremendous ID of the reward</p>
</td></tr>
<tr class="property-conditional-hint-response-only"><td><div class="property-name">
  <code class="property-name">order_id</code>
</div>
</td><td><span class="property-type">string</span></td><td><p>Tremendous ID of the order this reward is part of.</p>
</td></tr>
<tr class="property-conditional-hint-response-only"><td><div class="property-name">
  <code class="property-name">created_at</code>
</div>
</td><td><span class="property-type">string</span> <span class="property-format">date-time</span></td><td><p>Date the reward was created</p>
</td></tr>
<tr class="property-conditional-hint-request-only"><td><div class="property-name">
  <code class="property-name">campaign_id</code>
</div>
</td><td><span class="property-type">string</span></td><td><p>ID of the campaign in your account, that defines the available products (different gift cards, charity, etc.)
that the recipient can choose from.</p>
</td></tr>
<tr class="property-conditional-hint-request-only"><td><div class="property-name">
  <code class="property-name">products</code>
</div>
</td><td><span class="property-type">array</span> <span class="property-format">string</span></td><td><p>List of IDs of product (different gift cards, charity, etc.) that will be available
to the recipient to choose from.</p>

<p>Providing a <code>products</code> array will override the products made available by the campaign
specified using the <code>campaign_id</code> property unless the <code>products</code> array is empty. It will
<em>not</em> override other campaign attributes, like the message and customization of the look and feel.</p>
</td></tr>
<tr class=""><td><div class="property-name">
  <code class="property-name">value</code>
</div>
</td><td><span class="property-type">object</span></td><td></td></tr>  <tr>
    <td colspan="3">
      <details>
        <summary>Show object properties</summary>
        <table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody class="object-schema-table-body">
    <tr class=""><td><div class="property-name">
  <code class="property-name">denomination</code>
</div>
</td><td><span class="property-type">number</span> <span class="property-format">double</span></td><td><p>Amount of the reward</p>
</td></tr>
<tr class=""><td><div class="property-name">
  <code class="property-name">currency_code</code>
</div>
</td><td><span class="property-type">string</span></td><td><p>Currency of the reward</p>
</td></tr>
  </tbody>
</table>

</tr>

<tr class=""><td><div class="property-name">
  <code class="property-name">recipient</code>
</div>
</td><td><span class="property-type">object</span></td><td><p>Details of the recipient of the reward</p>
</td></tr>  <tr>
    <td colspan="3">
      <details>
        <summary>Show object properties</summary>
        <table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody class="object-schema-table-body">
    <tr class=""><td><div class="property-name">
  <code class="property-name">name</code>
</div>
</td><td><span class="property-type">string</span></td><td><p>Name of the recipient</p>
</td></tr>
<tr class=""><td><div class="property-name">
  <code class="property-name">email</code>
</div>
</td><td><span class="property-type">string</span></td><td><p>Email address of the recipient</p>
</td></tr>
<tr class=""><td><div class="property-name">
  <code class="property-name">phone</code>
</div>
</td><td><span class="property-type">string</span></td><td><p>Phone number of the recipient. For non-US phone numbers, specify the country code (prefixed with +).</p>
</td></tr>
  </tbody>
</table>

</tr>

<tr class=""><td><div class="property-name">
  <code class="property-name">deliver_at</code>
</div>
</td><td><span class="property-type">string</span> <span class="property-format">date</span></td><td><p>Timestamp of reward delivery within the next year. Note that if date-time is provided, the time values will be ignored.</p>
</td></tr>
<tr class=""><td><div class="property-name">
  <code class="property-name">custom_fields</code>
</div>
</td><td><span class="property-type">array</span></td><td></td></tr>  <tr>
    <td colspan="3">
      <details>
        <summary>Show array item type</summary>
        <table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody class="object-schema-table-body">
    <tr class=""><td><div class="property-name">
  <code class="property-name">id</code>
</div>
</td><td><span class="property-type">string</span></td><td><p>Tremendous ID of the custom field</p>
</td></tr>
<tr class=""><td><div class="property-name">
  <code class="property-name">value</code>
</div>
</td><td><span class="property-type">string</span></td><td><p>Value of the custom field</p>
</td></tr>
  </tbody>
</table>

</tr>

<tr class=""><td><div class="property-name">
  <code class="property-name">language</code>
</div>
</td><td><span class="property-type">string</span></td><td><p>Set this to translate the redemption experience for this reward. Pass a 2-letter <a href="https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes">ISO-639-1 code</a> for the desired language. Defaults to <code>en</code>.</p>
</td></tr>
<tr class=""><td><div class="property-name">
  <code class="property-name">delivery</code>
</div>
</td><td><span class="property-type">object</span></td><td><p>Details on how the reward is delivered to the recipient.</p>
</td></tr>  <tr>
    <td colspan="3">
      <details>
        <summary>Show object properties</summary>
        <table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody class="object-schema-table-body">
    <tr class=""><td><div class="property-name">
  <code class="property-name">method</code>
</div>
</td><td><span class="property-type">string</span></td><td><p>How to deliver the reward to the recipient.</p>

<table>
  <thead>
    <tr>
      <th>Delivery Method</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>EMAIL</code></td>
      <td>Deliver the reward to the recipient by email</td>
    </tr>
    <tr>
      <td><code>LINK</code></td>
      <td>
        <p>Deliver the reward to the recipient via a link.</p>
        <p>The link can be retrieved on a successfully ordered reward via the <code>/rewards</code> or <code>/rewards/{id}</code> endpoint. That link must then be  delivered to the recipient out-of-band.</p>
      </td>
    </tr>
    <tr>
      <td><code>PHONE</code></td>
      <td>Deliver the reward to the recipient by SMS</td>
    </tr>
  </tbody>
</table>
</td></tr>
  </tbody>
</table>

</tr>

  </tbody>
</table>

</tr>

  </tbody>
</table>

</div>


### Funding sources<a id="funding-sources"></a>

There are different ways to pay for gift cards and rewards on Tremendous. Every payment mechanism is called a "funding source".

You can retrieve a list of all available funding sources by using the [Funding sources API endpoint](https://tremendous.readme.io/reference/core-funding-source-index).

The Tremendous API sandbox environment comes with a single funding source that allows you to spend up to $5,000 in *fake money* to test the API. [Learn more about the sandbox environment](https://tremendous.readme.io/reference/sandbox).

The HTTP status code `200` on the response will be used to indicate success.

After processing successfully the reward gets queued to be delivered to it's recipient
(for delivery method `EMAIL` and `PHONE`). Delivery will happen asynchronously, after the response
has been sent.

### Idempotence<a id="idempotence"></a>

Requests issued with the same external_id are idempotent.

Submitting an order with an already existing `external_id`, will result in a `201` response code.
In this case the response will return a representation of the already existing order in the response body.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_order_response = tremendous.orders.create_order(
    payment={
        "funding_source_id": "funding_source_id_example",
    },
    reward={
        "campaign_id": "SOMEIDSOMEID",
        "deliver_at": "2023-12-31",
        "language": "de",
    },
    external_id="Your-Individual-Identifier-for-This-Order",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment: [`OrdersCreateOrderRequestPayment`](./tremendous_python_sdk/type/orders_create_order_request_payment.py)<a id="payment-orderscreateorderrequestpaymenttremendous_python_sdktypeorders_create_order_request_paymentpy"></a>


##### reward: [`OrdersCreateOrderRequestReward`](./tremendous_python_sdk/type/orders_create_order_request_reward.py)<a id="reward-orderscreateorderrequestrewardtremendous_python_sdktypeorders_create_order_request_rewardpy"></a>


##### external_id: `Optional[str]`<a id="external_id-optionalstr"></a>

Reference for this order, supplied by the customer.  When set, `external_id` makes order idempotent. All requests that use the same `external_id` after the initial order creation, will result in a response that returns the data of the initially created order. The response will have a `201` response code. These responses **fail** to create any further orders.  It also allows for retrieving by `external_id` instead of `id` only. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OrdersCreateOrderRequest`](./tremendous_python_sdk/type/orders_create_order_request.py)
Order to create

#### 🔄 Return<a id="🔄-return"></a>

[`OrdersCreateOrderResponse`](./tremendous_python_sdk/pydantic/orders_create_order_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/orders` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.orders.get_list`<a id="tremendousordersget_list"></a>

Retrieve a list of orders


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = tremendous.orders.get_list(
    offset=10,
    campaign_id="IVM0I3WNJJL0",
    external_id="12878",
    created_at_gte="2023-07-15T18:12:18Z",
    created_at_lte="2023-08-01T18:12:18Z",
    limit=10,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### offset: `int`<a id="offset-int"></a>

Offsets the returned list by the given number of orders. The returned orders are ordered (and offsetted) by their creation date (DESC).

##### campaign_id: `str`<a id="campaign_id-str"></a>

Only return results with a matching campaign_id.

##### external_id: `str`<a id="external_id-str"></a>

Only return results with a matching external_id.

##### created_at_gte: `str`<a id="created_at_gte-str"></a>

Only return results where the created_at field is greater than or equal to the supplied value. The string needs to be an ISO 8601 datetime.

##### created_at_lte: `str`<a id="created_at_lte-str"></a>

Only return results where the created_at field is less than or equal to the supplied value. The string needs to be an ISO 8601 datetime.

##### limit: `int`<a id="limit-int"></a>

Limits the number of orders listed. The maximum value is 100 and the default is 10.

#### 🔄 Return<a id="🔄-return"></a>

[`OrdersGetListResponse`](./tremendous_python_sdk/pydantic/orders_get_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/orders` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.orders.get_order_by_id`<a id="tremendousordersget_order_by_id"></a>

Retrieve the order, identified by the given `id` in the URL


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_order_by_id_response = tremendous.orders.get_order_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

ID of the order that should be retrieved. In case the order has an `external_id` reference supplied by the customer on creation, it's possible to use it instead. 

#### 🔄 Return<a id="🔄-return"></a>

[`OrdersGetOrderByIdResponse`](./tremendous_python_sdk/pydantic/orders_get_order_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/orders/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.orders.reject_by_id`<a id="tremendousordersreject_by_id"></a>

Rejects an order that is pending review, identified by the given `id` in the URL.

Approvals is a feature that requires orders to be approved by an organization admin
before they are sent out. To enable approvals for your organization, please enable
'Allow approvals via API' via the organization''s 'Order Approvals' settings from the Tremendous dashboard.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
reject_by_id_response = tremendous.orders.reject_by_id(
    id="SOMEIDSOMEID",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

ID of the order that should be rejected. In case the order has an `external_id` reference supplied by the customer on creation, it's possible to use it instead.

#### 🔄 Return<a id="🔄-return"></a>

[`OrdersRejectByIdResponse`](./tremendous_python_sdk/pydantic/orders_reject_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/order_approvals/{id}/reject` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.organizations.create_api_key`<a id="tremendousorganizationscreate_api_key"></a>

Creates a new API key. The API key used to make the request will remain active.

Created API keys are generated randomly and returned in the response. **You cannot retrieve them again.**


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_api_key_response = tremendous.organizations.create_api_key()
```

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationsCreateApiKeyResponse`](./tremendous_python_sdk/pydantic/organizations_create_api_key_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/create_api_key` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.organizations.create_new_organization`<a id="tremendousorganizationscreate_new_organization"></a>

Organizations are a way to separate different parts of your business within the same Tremendous account.

You can assign users in your Tremendous team as members to any organization. Users can be members of multiple organizations at once.

API keys belong to a single organization. The API key used in a request determines on behalf of which organization the request is carried out.

**Important note:** When creating an organization, you are required to either pass `with_api_key` or `copy_settings[user]` in the request body as `true`. This ensures that your new Organization can either be accessed via the API or the Dashboard.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_organization_response = tremendous.organizations.create_new_organization(
    name="ACME Inc.",
    website="https://www.example.com/some-org",
    with_api_key=True,
    copy_settings={
        "campaigns": False,
        "custom_fields": False,
        "order_approvals": False,
        "payment_methods": False,
        "security_settings": True,
        "users": False,
    },
    phone="123-456-7890",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the organization

##### website: `str`<a id="website-str"></a>

URL of the website of that organization

##### with_api_key: `bool`<a id="with_api_key-bool"></a>

Default value is `false`. Set to true to also generate an API key associated to the new organization.

##### copy_settings: [`OrganizationsCreateNewOrganizationRequestCopySettings`](./tremendous_python_sdk/type/organizations_create_new_organization_request_copy_settings.py)<a id="copy_settings-organizationscreateneworganizationrequestcopysettingstremendous_python_sdktypeorganizations_create_new_organization_request_copy_settingspy"></a>


##### phone: `str`<a id="phone-str"></a>

Phone number of the organization. For non-US phone numbers, specify the country code (prefixed with +).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OrganizationsCreateNewOrganizationRequest`](./tremendous_python_sdk/type/organizations_create_new_organization_request.py)
Organization details

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationsCreateNewOrganizationResponse`](./tremendous_python_sdk/pydantic/organizations_create_new_organization_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.organizations.get_list`<a id="tremendousorganizationsget_list"></a>

The returned list only includes the organization to which the API key belongs to, that is used for the request.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = tremendous.organizations.get_list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationsGetListResponse`](./tremendous_python_sdk/pydantic/organizations_get_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.organizations.get_organization`<a id="tremendousorganizationsget_organization"></a>

Retrieve organization

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_organization_response = tremendous.organizations.get_organization(
    id="SOMEIDSOMEID",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

ID of the organization to retrieve

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationsGetOrganizationResponse`](./tremendous_python_sdk/pydantic/organizations_get_organization_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.products.get_by_id`<a id="tremendousproductsget_by_id"></a>

Retrieve a product, identified by the given `id` in the URL


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = tremendous.products.get_by_id(
    id="SOMEIDSOMEID",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

ID of the product that should be retrieved

#### 🔄 Return<a id="🔄-return"></a>

[`ProductsGetByIdResponse`](./tremendous_python_sdk/pydantic/products_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/products/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.products.get_list`<a id="tremendousproductsget_list"></a>

Retrieve a list of available products


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = tremendous.products.get_list(
    country="US,UK",
    currency="USD,EUR",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country: `str`<a id="country-str"></a>

Comma-separated list of [Alpha-2 country codes](https://www.iban.com/country-codes), used to only retrieve products available in the provided countries

##### currency: `str`<a id="currency-str"></a>

Comma-separated list of [currency codes](https://www.iban.com/currency-codes), used to only retrieve products available in the provided currencies

#### 🔄 Return<a id="🔄-return"></a>

[`ProductsGetListResponse`](./tremendous_python_sdk/pydantic/products_get_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/products` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.rewards.generate_embed_token`<a id="tremendousrewardsgenerate_embed_token"></a>

Generate a temporary reward token identified by the `id` in the URL.
These tokens are needed to render a reward when using [Tremendous Embed](https://github.com/tremendous-rewards/embed/blob/master/docs/documentation.md).
The token is valid for 24 hours.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_embed_token_response = tremendous.rewards.generate_embed_token(
    id="SOMEIDSOMEID",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

ID of the reward

#### 🔄 Return<a id="🔄-return"></a>

[`RewardsGenerateEmbedTokenResponse`](./tremendous_python_sdk/pydantic/rewards_generate_embed_token_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rewards/{id}/generate_embed_token` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.rewards.generate_link`<a id="tremendousrewardsgenerate_link"></a>

Generate a redemption link for the reward identified by the `id` in the URL


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_link_response = tremendous.rewards.generate_link(
    id="SOMEIDSOMEID",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

ID of the reward

#### 🔄 Return<a id="🔄-return"></a>

[`RewardsGenerateLinkResponse`](./tremendous_python_sdk/pydantic/rewards_generate_link_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rewards/{id}/generate_link` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.rewards.get_single_reward`<a id="tremendousrewardsget_single_reward"></a>

Retrieve the reward, identified by the given `id` in the URL


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_reward_response = tremendous.rewards.get_single_reward(
    id="SOMEIDSOMEID",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

ID of the reward that should be retrieved

#### 🔄 Return<a id="🔄-return"></a>

[`RewardsGetSingleRewardResponse`](./tremendous_python_sdk/pydantic/rewards_get_single_reward_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rewards/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.rewards.list_all_rewards`<a id="tremendousrewardslist_all_rewards"></a>

Retrieve a list of all created rewards


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_rewards_response = tremendous.rewards.list_all_rewards(
    offset=10,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### offset: `int`<a id="offset-int"></a>

Offsets the returned list by the given number of rewards. The returned rewards are ordered (and offsetted) by their creation date (DESC).

#### 🔄 Return<a id="🔄-return"></a>

[`RewardsListAllRewardsResponse`](./tremendous_python_sdk/pydantic/rewards_list_all_rewards_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rewards` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.rewards.resend_reward_by_id`<a id="tremendousrewardsresend_reward_by_id"></a>

Resends a reward, identified by the given `id` in the URL, to its recipient.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
resend_reward_by_id_response = tremendous.rewards.resend_reward_by_id(
    id="SOMEIDSOMEID",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

ID of the reward that should be resent

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rewards/{id}/resend` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.webhooks.create_webhook`<a id="tremendouswebhookscreate_webhook"></a>

Tremendous uses webhooks as a notification system for various events that happen in your account.

> 📘 Learn more about Webhooks
>
> Our guide explains everything you need to know about the Tremendous webhooks:
> [Read it here](https://developers.tremendous.com/)

Every organization can define a single webhook endpoint where we send requests to, whenever an event happens.

This endpoint allows you to setup that endpoint. The URL of the endpoint can be changed by making a request to this endpoint again with the new URL.

## Request body<a id="request-body"></a>

<div class="object-schema-request-schema">
  <table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody class="object-schema-table-body">
    <tr class=""><td><div class="property-name">
  <code class="property-name">url</code>
</div>
</td><td><span class="property-type">string</span> <span class="property-format">uri</span></td><td><p>URL the webhook will make requests to</p>
</td></tr>
  </tbody>
</table>

</div>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_webhook_response = tremendous.webhooks.create_webhook(
    url="https://example.com/webhook",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### url: `str`<a id="url-str"></a>

URL the webhook will make requests to

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhooksCreateWebhookRequest`](./tremendous_python_sdk/type/webhooks_create_webhook_request.py)
Webhook details

#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksCreateWebhookResponse`](./tremendous_python_sdk/pydantic/webhooks_create_webhook_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.webhooks.get_details`<a id="tremendouswebhooksget_details"></a>

Every organization can only have one webhook. This endpoint shows the details about that webhook.

> 📘 Learn more about Webhooks
>
> Our guide explains everything you need to know about the Tremendous webhooks:
> [Read it here](https://developers.tremendous.com/)


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = tremendous.webhooks.get_details()
```

#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksGetDetailsResponse`](./tremendous_python_sdk/pydantic/webhooks_get_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.webhooks.get_details_0`<a id="tremendouswebhooksget_details_0"></a>

> 📘 Learn more about Webhooks
>
> Our guide explains everything you need to know about the Tremendous webhooks:
> [Read it here](https://developers.tremendous.com/)


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_0_response = tremendous.webhooks.get_details_0(
    id="SOMEIDSOMEID",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

ID of the webhook to retrieve

#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksGetDetails200Response`](./tremendous_python_sdk/pydantic/webhooks_get_details200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.webhooks.list_events`<a id="tremendouswebhookslist_events"></a>

Lists all event types that can be sent to the configured webhook endpoint.

> 📘 Learn more about Webhooks
>
> Our guide explains everything you need to know about the Tremendous webhooks:
> [Read it here](https://developers.tremendous.com/)


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_events_response = tremendous.webhooks.list_events(
    id="SOMEIDSOMEID",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

ID of the webhook to list the events for

#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksListEventsResponse`](./tremendous_python_sdk/pydantic/webhooks_list_events_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks/{id}/events` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tremendous.webhooks.trigger_event`<a id="tremendouswebhookstrigger_event"></a>

Making a request to this endpoint will cause our system to trigger a webhook for the specified event. This can be very useful when testing the setup that processes webhooks on your end.

> 📘 Learn more about Webhooks
>
> Our guide explains everything you need to know about the Tremendous webhooks:
> [Read it here](https://developers.tremendous.com/)


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trigger_event_response = tremendous.webhooks.trigger_event(
    event="INVOICES.PAID",
    id="SOMEIDSOMEID",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### event: `str`<a id="event-str"></a>

The event to test. See the [List events endpoint reference](https://developers.tremendous.com/) for all available events.

##### id: `str`<a id="id-str"></a>

ID of the webhook to test

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhooksTriggerEventRequest`](./tremendous_python_sdk/type/webhooks_trigger_event_request.py)
Webhook details

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks/{id}/simulate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
