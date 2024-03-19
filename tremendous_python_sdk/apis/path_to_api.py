import typing_extensions

from tremendous_python_sdk.paths import PathValues
from tremendous_python_sdk.apis.paths.rewards import Rewards
from tremendous_python_sdk.apis.paths.rewards_id import RewardsId
from tremendous_python_sdk.apis.paths.rewards_id_generate_link import RewardsIdGenerateLink
from tremendous_python_sdk.apis.paths.rewards_id_generate_embed_token import RewardsIdGenerateEmbedToken
from tremendous_python_sdk.apis.paths.rewards_id_resend import RewardsIdResend
from tremendous_python_sdk.apis.paths.orders import Orders
from tremendous_python_sdk.apis.paths.orders_id import OrdersId
from tremendous_python_sdk.apis.paths.order_approvals_id_approve import OrderApprovalsIdApprove
from tremendous_python_sdk.apis.paths.order_approvals_id_reject import OrderApprovalsIdReject
from tremendous_python_sdk.apis.paths.products import Products
from tremendous_python_sdk.apis.paths.products_id import ProductsId
from tremendous_python_sdk.apis.paths.campaigns import Campaigns
from tremendous_python_sdk.apis.paths.campaigns_id import CampaignsId
from tremendous_python_sdk.apis.paths.funding_sources import FundingSources
from tremendous_python_sdk.apis.paths.funding_sources_id import FundingSourcesId
from tremendous_python_sdk.apis.paths.invoices import Invoices
from tremendous_python_sdk.apis.paths.invoices_id import InvoicesId
from tremendous_python_sdk.apis.paths.invoices_id_pdf import InvoicesIdPdf
from tremendous_python_sdk.apis.paths.invoices_id_csv import InvoicesIdCsv
from tremendous_python_sdk.apis.paths.balance_transactions import BalanceTransactions
from tremendous_python_sdk.apis.paths.organizations import Organizations
from tremendous_python_sdk.apis.paths.organizations_id import OrganizationsId
from tremendous_python_sdk.apis.paths.organizations_create_api_key import OrganizationsCreateApiKey
from tremendous_python_sdk.apis.paths.members import Members
from tremendous_python_sdk.apis.paths.members_id import MembersId
from tremendous_python_sdk.apis.paths.fields import Fields
from tremendous_python_sdk.apis.paths.webhooks import Webhooks
from tremendous_python_sdk.apis.paths.webhooks_id import WebhooksId
from tremendous_python_sdk.apis.paths.webhooks_id_simulate import WebhooksIdSimulate
from tremendous_python_sdk.apis.paths.webhooks_id_events import WebhooksIdEvents

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.REWARDS: Rewards,
        PathValues.REWARDS_ID: RewardsId,
        PathValues.REWARDS_ID_GENERATE_LINK: RewardsIdGenerateLink,
        PathValues.REWARDS_ID_GENERATE_EMBED_TOKEN: RewardsIdGenerateEmbedToken,
        PathValues.REWARDS_ID_RESEND: RewardsIdResend,
        PathValues.ORDERS: Orders,
        PathValues.ORDERS_ID: OrdersId,
        PathValues.ORDER_APPROVALS_ID_APPROVE: OrderApprovalsIdApprove,
        PathValues.ORDER_APPROVALS_ID_REJECT: OrderApprovalsIdReject,
        PathValues.PRODUCTS: Products,
        PathValues.PRODUCTS_ID: ProductsId,
        PathValues.CAMPAIGNS: Campaigns,
        PathValues.CAMPAIGNS_ID: CampaignsId,
        PathValues.FUNDING_SOURCES: FundingSources,
        PathValues.FUNDING_SOURCES_ID: FundingSourcesId,
        PathValues.INVOICES: Invoices,
        PathValues.INVOICES_ID: InvoicesId,
        PathValues.INVOICES_ID_PDF: InvoicesIdPdf,
        PathValues.INVOICES_ID_CSV: InvoicesIdCsv,
        PathValues.BALANCE_TRANSACTIONS: BalanceTransactions,
        PathValues.ORGANIZATIONS: Organizations,
        PathValues.ORGANIZATIONS_ID: OrganizationsId,
        PathValues.ORGANIZATIONS_CREATE_API_KEY: OrganizationsCreateApiKey,
        PathValues.MEMBERS: Members,
        PathValues.MEMBERS_ID: MembersId,
        PathValues.FIELDS: Fields,
        PathValues.WEBHOOKS: Webhooks,
        PathValues.WEBHOOKS_ID: WebhooksId,
        PathValues.WEBHOOKS_ID_SIMULATE: WebhooksIdSimulate,
        PathValues.WEBHOOKS_ID_EVENTS: WebhooksIdEvents,
    }
)

path_to_api = PathToApi(
    {
        PathValues.REWARDS: Rewards,
        PathValues.REWARDS_ID: RewardsId,
        PathValues.REWARDS_ID_GENERATE_LINK: RewardsIdGenerateLink,
        PathValues.REWARDS_ID_GENERATE_EMBED_TOKEN: RewardsIdGenerateEmbedToken,
        PathValues.REWARDS_ID_RESEND: RewardsIdResend,
        PathValues.ORDERS: Orders,
        PathValues.ORDERS_ID: OrdersId,
        PathValues.ORDER_APPROVALS_ID_APPROVE: OrderApprovalsIdApprove,
        PathValues.ORDER_APPROVALS_ID_REJECT: OrderApprovalsIdReject,
        PathValues.PRODUCTS: Products,
        PathValues.PRODUCTS_ID: ProductsId,
        PathValues.CAMPAIGNS: Campaigns,
        PathValues.CAMPAIGNS_ID: CampaignsId,
        PathValues.FUNDING_SOURCES: FundingSources,
        PathValues.FUNDING_SOURCES_ID: FundingSourcesId,
        PathValues.INVOICES: Invoices,
        PathValues.INVOICES_ID: InvoicesId,
        PathValues.INVOICES_ID_PDF: InvoicesIdPdf,
        PathValues.INVOICES_ID_CSV: InvoicesIdCsv,
        PathValues.BALANCE_TRANSACTIONS: BalanceTransactions,
        PathValues.ORGANIZATIONS: Organizations,
        PathValues.ORGANIZATIONS_ID: OrganizationsId,
        PathValues.ORGANIZATIONS_CREATE_API_KEY: OrganizationsCreateApiKey,
        PathValues.MEMBERS: Members,
        PathValues.MEMBERS_ID: MembersId,
        PathValues.FIELDS: Fields,
        PathValues.WEBHOOKS: Webhooks,
        PathValues.WEBHOOKS_ID: WebhooksId,
        PathValues.WEBHOOKS_ID_SIMULATE: WebhooksIdSimulate,
        PathValues.WEBHOOKS_ID_EVENTS: WebhooksIdEvents,
    }
)
