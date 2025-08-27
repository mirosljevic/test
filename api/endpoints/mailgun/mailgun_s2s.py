from api.executor import api
from environment import hosts


@api
def webhook_update_email(access_token, payload):
    return {
        "host": hosts.api,
        "endpoint": "/api/mailgun/rest/v1/update-email",
        "method": "POST",
        "bearer_token": access_token,
        "json": payload
    }


@api
def webhook_store_email(access_token, payload):
    return {
        "host": hosts.api,
        "endpoint": "/api/mailgun/rest/v1/store-email",
        "method": "POST",
        "bearer_token": access_token,
        "json": payload
    }


@api
def webhook_hard_bounce_email(access_token, payload):

    return {
        "host": hosts.api,
        "endpoint": "/api/mailgun/rest/v1/hard-bounce-email",
        "method": "POST",
        "json": payload
    }
