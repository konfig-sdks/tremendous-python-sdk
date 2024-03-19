operation_parameter_map = {
    '/balance_transactions-GET': {
        'parameters': [
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'created_at[gte]'
            },
            {
                'name': 'created_at[lte]'
            },
        ]
    },
    '/campaigns-GET': {
        'parameters': [
        ]
    },
    '/campaigns/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/fields-GET': {
        'parameters': [
        ]
    },
    '/funding_sources-GET': {
        'parameters': [
        ]
    },
    '/funding_sources/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/invoices-POST': {
        'parameters': [
            {
                'name': 'amount'
            },
            {
                'name': 'po_number'
            },
            {
                'name': 'memo'
            },
        ]
    },
    '/invoices-GET': {
        'parameters': [
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/invoices/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/invoices/{id}/csv-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/invoices/{id}/pdf-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/invoices/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/members-POST': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'name'
            },
            {
                'name': 'role'
            },
        ]
    },
    '/members/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/members-GET': {
        'parameters': [
        ]
    },
    '/order_approvals/{id}/approve-POST': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/orders-POST': {
        'parameters': [
            {
                'name': 'payment'
            },
            {
                'name': 'reward'
            },
            {
                'name': 'external_id'
            },
        ]
    },
    '/orders-GET': {
        'parameters': [
            {
                'name': 'offset'
            },
            {
                'name': 'campaign_id'
            },
            {
                'name': 'external_id'
            },
            {
                'name': 'created_at[gte]'
            },
            {
                'name': 'created_at[lte]'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/orders/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/order_approvals/{id}/reject-POST': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/organizations/create_api_key-POST': {
        'parameters': [
        ]
    },
    '/organizations-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'website'
            },
            {
                'name': 'with_api_key'
            },
            {
                'name': 'copy_settings'
            },
            {
                'name': 'phone'
            },
        ]
    },
    '/organizations-GET': {
        'parameters': [
        ]
    },
    '/organizations/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/products/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/products-GET': {
        'parameters': [
            {
                'name': 'country'
            },
            {
                'name': 'currency'
            },
        ]
    },
    '/rewards/{id}/generate_embed_token-POST': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rewards/{id}/generate_link-POST': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rewards/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rewards-GET': {
        'parameters': [
            {
                'name': 'offset'
            },
        ]
    },
    '/rewards/{id}/resend-POST': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/webhooks-POST': {
        'parameters': [
            {
                'name': 'url'
            },
        ]
    },
    '/webhooks-GET': {
        'parameters': [
        ]
    },
    '/webhooks/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/webhooks/{id}/events-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/webhooks/{id}/simulate-POST': {
        'parameters': [
            {
                'name': 'event'
            },
            {
                'name': 'id'
            },
        ]
    },
};