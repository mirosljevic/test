from api.executor import api
from environment import hosts


@api
def init_new_payment_method(session, kind, **kwargs):
    return {
        "session": session,
        "method": "post",
        "host": hosts.gateway_web,
        "endpoint": "/web/payment-processor-integration/rest/v1/payment-methods",
        "json": {
            "paymentMethodType": kind
        },
        **kwargs
    }


@api
def init_update_payment_method(session=None, payment_method_id=None, **kwargs):
    return {
        "session": session,
        "method": "put",
        "host": hosts.gateway_web,
        "endpoint": f"/web/payment-processor-integration/rest/v1/payment-methods/{payment_method_id}",
        **kwargs
    }


@api
def new_payment(session=None, payment_method_id=None, amount=None, **kwargs):
    return {
        "session": session,
        "method": "post",
        "host": hosts.gateway_web,
        "endpoint": "/web/payment-processor-integration/rest/v1/payments",
        "json": {
            "paymentMethodId": payment_method_id,
            "amount": amount
        },
        **kwargs
    }
