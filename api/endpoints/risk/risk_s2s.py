from api.executor import api
from environment import hosts


@api
def get_list_of_audit_logs(access_token, object_type, object_id, rev, include_only_changes,
                           date_from=None, date_to=None, **kwargs):
    params = {
        "objectType": object_type,
        "objectId": object_id,
        "rev": rev,
        "includeOnlyChanges": include_only_changes,
        "from": date_from,
        "to": date_to
    }
    return {
        "host": hosts.api,
        "endpoint": "/api/risk/rest/v1/audit-history",
        "bearer_token": access_token,
        "params": params,
        **kwargs
    }


@api
def check_withdrawal_risk(access_token, balance, amount, payment_method_id, payment_id, player_id, **kwargs):
    payload = {
        "balance": balance,
        "amount": amount,
        "paymentMethodId": payment_method_id,
        "paymentId": payment_id
    }
    return {
        "bearer_token": access_token,
        "host": hosts.api,
        "endpoint": f"/api/risk/rest/v1/validation/withdrawal/{player_id}",
        "method": "POST",
        "json": payload,
        **kwargs
    }


@api
def create_risk_exception(access_token, risk_scenario_id, player_id, **kwargs):
    return {
        "bearer_token": access_token,
        "host": hosts.api,
        "endpoint": f"/api/risk/rest/v1/risk-exceptions/scenarios/{risk_scenario_id}/players/{player_id}",
        "method": "POST",
        **kwargs
    }


@api
def delete_risk_exception(access_token, risk_exception_id, **kwargs):
    return {
        "bearer_token": access_token,
        "host": hosts.api,
        "endpoint": f"/api/risk/rest/v1/risk-exceptions/{risk_exception_id}",
        "method": "DELETE",
        **kwargs
    }


@api
def enable_disable_risk_scenario(access_token, risk_scenario_id, admin_id, enabled, **kwargs):
    payload = {
        "updatedBy": admin_id,
        "enabled": enabled
    }
    return {
        "bearer_token": access_token,
        "host": hosts.api,
        "endpoint": f"/api/risk/rest/v1/scenarios/{risk_scenario_id}",
        "method": "PUT",
        "json": payload,
        **kwargs
    }


@api
def update_app_config(access_token, config_id, config_key, config_value, **kwargs):

    return {
        "bearer_token": access_token,
        "host": hosts.api,
        "endpoint": "/api/risk/rest/v1/configuration",
        "method": "PUT",
        "json": {"appConfigDtos": [{
            "id": config_id,
            "configKey": config_key,
            "configValue": [config_value]}]

        },
        **kwargs
    }
