from api.executor import api
from environment import hosts


@api
def add_payment_method(session, token, account_data, **kwargs):
    return {
        "session": session,
        "method": "post",
        "host": hosts.payment_vault,
        "endpoint": "/web/paymentmethod-vault/rest/v1/payment-methods",
        "json": account_data,
        "bearer_token": token,
        **kwargs
    }


@api
def update_payment_method(session=None, token=None, account_data=None, **kwargs):
    return {
        "session": session,
        "method": "put",
        "host": hosts.payment_vault,
        "endpoint": "/web/paymentmethod-vault/rest/v1/payment-methods",
        "json": account_data,
        "bearer_token": token,
        **kwargs
    }
