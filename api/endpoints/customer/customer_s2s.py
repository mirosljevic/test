from api.executor import api
from environment import hosts


@api
def get_contracts(access_token, contract_id, **kwargs):
    return {
        "host": hosts.api,
        "endpoint": "/api/customer/rest/v1/customers/contracts",
        "bearer_token": access_token,
        "params": {
            "contractId": contract_id
        },
        **kwargs
    }


@api
def get_contract_agreement_status(access_token, player_id, **kwargs):
    return {
        "host": hosts.api,
        "endpoint": f"/api/customer/rest/v1/customers/{player_id}/contract-agreements/status",
        "bearer_token": access_token,
        "method": "GET",
        **kwargs
    }


@api
def add_contract_to_player(access_token, contract_id, player_id, **kwargs):
    payload = {
        "contractId": contract_id
    }
    return {
        "host": hosts.api,
        "endpoint": f"/api/customer/rest/v1/customers/{player_id}/contract-agreements",
        "bearer_token": access_token,
        "method": "POST",
        "json": payload,
        **kwargs
    }


@api
def get_customers(access_token, login_name, **kwargs):
    return {
        "host": hosts.api,
        "endpoint": "/api/customer/rest/v1/customers",
        "method": "GET",
        "bearer_token": access_token,
        "params": {
            "loginName": login_name
        },
        **kwargs
    }


@api
def get_player(access_token, player_id, **kwargs):
    return {
        "host": hosts.api,
        "endpoint": f"/api/customer/rest/v2/players/{player_id}",
        "method": "GET",
        "bearer_token": access_token,
        **kwargs
    }


@api
def player_self_exclude(access_token, player_id, payload, **kwargs):
    return {
        "host": hosts.api,
        "endpoint": f"/api/customer/rest/v1/customers/{player_id}/self-exclude",
        "method": "POST",
        "bearer_token": access_token,
        "json": payload,
        **kwargs
    }


@api
def player_cancel_self_exclude(access_token, player_id, **kwargs):
    return {
        "host": hosts.api,
        "endpoint": f"/api/customer/rest/v1/customers/{player_id}/self-exclude",
        "method": "PATCH",
        "bearer_token": access_token,
        **kwargs
    }


@api
def flag_player(access_token, player_id, payload, **kwargs):
    return {
        "host": hosts.api,
        "endpoint": f"/api/customer/rest/v2/players/{player_id}/flag",
        "method": "PUT",
        "bearer_token": access_token,
        "json": payload,
        **kwargs
    }


@api
def get_player_flags(access_token, player_id, **kwargs):
    return {
        "host": hosts.api,
        "endpoint": f"/api/customer/rest/v2/players/{player_id}/flags",
        "method": "GET",
        "bearer_token": access_token,
        **kwargs
    }


@api
def get_player_verification(access_token, player_id, **kwargs):
    return {
        "host": hosts.api,
        "endpoint": f"/api/customer/rest/v1/customers/{player_id}/verifications",
        "bearer_token": access_token,
        "method": "GET",
        **kwargs
    }


@api
def request_player_verification(access_token, player_id, payload, **kwargs):
    return {
        "host": hosts.api,
        "method": "POST",
        "endpoint": f"/api/customer/rest/v1/customers/{player_id}/verifications",
        "json": payload,
        "bearer_token": access_token,
        **kwargs
    }


@api
def confirm_verification(access_token, player_id, payload, **kwargs):
    return {
        "host": hosts.api,
        "method": "POST",
        "endpoint": f"/api/customer/rest/v1/customers/{player_id}/verifications/confirm",
        "json": payload,
        "bearer_token": access_token,
        **kwargs
    }


@api
def confirm_verifications(access_token, player_id, payload, **kwargs):
    return {
        "host": hosts.api,
        "method": "POST",
        "endpoint": f"/api/customer/rest/v1/customers/{player_id}/verifications/confirm-verifications",
        "json": payload,
        "bearer_token": access_token,
        **kwargs
    }


@api
def reject_verification(access_token, player_id, payload, **kwargs):
    return {
        "host": hosts.api,
        "method": "POST",
        "endpoint": f"/api/customer/rest/v1/customers/{player_id}/verifications/reject",
        "json": payload,
        "bearer_token": access_token,
        **kwargs
    }
