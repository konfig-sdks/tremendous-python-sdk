import typing_extensions

from tremendous_python_sdk.apis.tags import TagValues
from tremendous_python_sdk.apis.tags.invoices_api import InvoicesApi
from tremendous_python_sdk.apis.tags.rewards_api import RewardsApi
from tremendous_python_sdk.apis.tags.orders_api import OrdersApi
from tremendous_python_sdk.apis.tags.webhooks_api import WebhooksApi
from tremendous_python_sdk.apis.tags.organizations_api import OrganizationsApi
from tremendous_python_sdk.apis.tags.members_api import MembersApi
from tremendous_python_sdk.apis.tags.products_api import ProductsApi
from tremendous_python_sdk.apis.tags.campaigns_api import CampaignsApi
from tremendous_python_sdk.apis.tags.funding_sources_api import FundingSourcesApi
from tremendous_python_sdk.apis.tags.balance_transactions_api import BalanceTransactionsApi
from tremendous_python_sdk.apis.tags.fields_api import FieldsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.INVOICES: InvoicesApi,
        TagValues.REWARDS: RewardsApi,
        TagValues.ORDERS: OrdersApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.ORGANIZATIONS: OrganizationsApi,
        TagValues.MEMBERS: MembersApi,
        TagValues.PRODUCTS: ProductsApi,
        TagValues.CAMPAIGNS: CampaignsApi,
        TagValues.FUNDING_SOURCES: FundingSourcesApi,
        TagValues.BALANCE_TRANSACTIONS: BalanceTransactionsApi,
        TagValues.FIELDS: FieldsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.INVOICES: InvoicesApi,
        TagValues.REWARDS: RewardsApi,
        TagValues.ORDERS: OrdersApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.ORGANIZATIONS: OrganizationsApi,
        TagValues.MEMBERS: MembersApi,
        TagValues.PRODUCTS: ProductsApi,
        TagValues.CAMPAIGNS: CampaignsApi,
        TagValues.FUNDING_SOURCES: FundingSourcesApi,
        TagValues.BALANCE_TRANSACTIONS: BalanceTransactionsApi,
        TagValues.FIELDS: FieldsApi,
    }
)
