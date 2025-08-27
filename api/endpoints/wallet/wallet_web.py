from api.executor import api
from environment import hosts


@api
def get_payment_methods(session=None, direction=None, **kwargs):
    return {
        "session": session,
        "method": "get",
        "host": hosts.gateway_web,
        "endpoint": f"/web/wallet/rest/v2/customers/me/payment-methods?direction={direction}",
        **kwargs
    }


@api
def withdrawal(session=None, amount=None, payment_method_id=None, **kwargs):
    return {
        "session": session,
        "method": "post",
        "host": hosts.gateway_web,
        "endpoint": "/web/wallet/rest/v1/customers/me/payments/withdrawal",
        "json": {
            "paymentMethodId": payment_method_id,
            "amount": {
                "amount": amount,
                "currency": "USD"
            }
        },
        **kwargs
    }


@api
def get_transactions(session=None, sort="-date", **kwargs):
    return {
        "session": session,
        "method": "get",
        "host": hosts.gateway_web,
        "endpoint": "/web/wallet/rest/v2/customers/me/accounts/transactions/aggregations",
        "params": {
            "sort": sort
        },
        **kwargs
    }


@api
def get_transaction_by_id(session=None, id=None, **kwargs):
    return {
        "session": session,
        "method": "get",
        "host": hosts.gateway_web,
        "endpoint": f"/web/wallet/rest/v2/customers/me/accounts/transactions/aggregations/{id}",
        **kwargs
    }


@api
def get_accounts(session=None, **kwargs):
    return {
        "session": session,
        "method": "get",
        "host": hosts.gateway_web,
        "endpoint": "/web/wallet/rest/v2/customers/me/accounts",
        **kwargs
    }


@api
def get_claimable_prizes(session=None, **kwargs):
    return {
        "session": session,
        "method": "get",
        "host": hosts.gateway_web,
        "endpoint": "/web/wallet/rest/v1/customers/me/claimable-prizes",
        **kwargs
    }


@api
def submit_claim_request(session=None, claim_id=None, **kwargs):
    return {
        "session": session,
        "method": "put",
        "host": hosts.gateway_web,
        "endpoint": f"/web/wallet/rest/v1/customers/me/claimable-prizes/{claim_id}",
        "expected_status_code": 204,
        **kwargs
    }


@api
def remove_payment_method(session=None, payment_method_id=None, **kwargs):
    return {
        "session": session,
        "method": "patch",
        "host": hosts.gateway_web,
        "endpoint": f"/web/wallet/rest/v2/customers/me/payment-methods/{payment_method_id}",
        "json": {
            "status": "DELETED"
        },
        **kwargs
    }


@api
def check_limit(session=None, **kwargs):
    params = {
        "limitType": "DEPOSIT",
        "includePendingAmounts": "true",
        "includeBalances": "true",
        "includeQuantityTrack": "true"
    }
    return {
        "session": session,
        "method": "get",
        "host": hosts.gateway_web,
        "endpoint": "/web/wallet/rest/v1/customers/me/limits/",
        "params": params,
        **kwargs
    }


@api
def set_funding_limit(session=None, amount=None, period=None, **kwargs):
    return {
        "session": session,
        "method": "post",
        "host": hosts.gateway_web,
        "endpoint": "/web/wallet/rest/v1/customers/me/limits/",
        "json": [{
            "quantityType": "MAX_AMOUNT",
            "quantity": {
                "amount": amount,
                "currency": "USD"
            },
            "limitType": "DEPOSIT",
            "period": period
        }],
        **kwargs
    }


@api
def get_latest_wins():
    return {
        "host": hosts.gateway_web,
        "endpoint": "/web/wallet/rest/v1/claimable-prizes/latest-wins",
        "method": "get",
    }
