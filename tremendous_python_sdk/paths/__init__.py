# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from tremendous_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    REWARDS = "/rewards"
    REWARDS_ID = "/rewards/{id}"
    REWARDS_ID_GENERATE_LINK = "/rewards/{id}/generate_link"
    REWARDS_ID_GENERATE_EMBED_TOKEN = "/rewards/{id}/generate_embed_token"
    REWARDS_ID_RESEND = "/rewards/{id}/resend"
    ORDERS = "/orders"
    ORDERS_ID = "/orders/{id}"
    ORDER_APPROVALS_ID_APPROVE = "/order_approvals/{id}/approve"
    ORDER_APPROVALS_ID_REJECT = "/order_approvals/{id}/reject"
    PRODUCTS = "/products"
    PRODUCTS_ID = "/products/{id}"
    CAMPAIGNS = "/campaigns"
    CAMPAIGNS_ID = "/campaigns/{id}"
    FUNDING_SOURCES = "/funding_sources"
    FUNDING_SOURCES_ID = "/funding_sources/{id}"
    INVOICES = "/invoices"
    INVOICES_ID = "/invoices/{id}"
    INVOICES_ID_PDF = "/invoices/{id}/pdf"
    INVOICES_ID_CSV = "/invoices/{id}/csv"
    BALANCE_TRANSACTIONS = "/balance_transactions"
    ORGANIZATIONS = "/organizations"
    ORGANIZATIONS_ID = "/organizations/{id}"
    ORGANIZATIONS_CREATE_API_KEY = "/organizations/create_api_key"
    MEMBERS = "/members"
    MEMBERS_ID = "/members/{id}"
    FIELDS = "/fields"
    WEBHOOKS = "/webhooks"
    WEBHOOKS_ID = "/webhooks/{id}"
    WEBHOOKS_ID_SIMULATE = "/webhooks/{id}/simulate"
    WEBHOOKS_ID_EVENTS = "/webhooks/{id}/events"
