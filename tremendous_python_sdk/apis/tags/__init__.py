# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from tremendous_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    INVOICES = "Invoices"
    REWARDS = "Rewards"
    ORDERS = "Orders"
    WEBHOOKS = "Webhooks"
    ORGANIZATIONS = "Organizations"
    MEMBERS = "Members"
    PRODUCTS = "Products"
    CAMPAIGNS = "Campaigns"
    FUNDING_SOURCES = "Funding sources"
    BALANCE_TRANSACTIONS = "Balance transactions"
    FIELDS = "Fields"
