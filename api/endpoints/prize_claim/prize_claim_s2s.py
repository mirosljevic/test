from api.executor import api
from environment import hosts


@api
def get_list_of_audit_logs(access_token, object_type=None, object_id=None,  rev=None,
                           include_only_changes=None, date_from=None, date_to=None, **kwargs):
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
        "endpoint": "/api/prizeclaim/rest/v1/audit-history",
        "bearer_token": access_token,
        "params": params,
        **kwargs
    }


@api
def generate_w2g_doc(access_token, claim_id, tax, player_id):
    payload = {
        "deductionAmounts":
            {"federalTax": tax},
            "playerId": player_id}
    return {
        "host": hosts.api,
        "endpoint": f"/api/prizeclaim/rest/v1/w2g-forms/{claim_id}",
        "bearer_token": access_token,
        "method": "PUT",
        "json": payload
    }
