from api.executor import api
from environment import hosts


@api
def get_risk_scenario(session, scenario_id, **kwargs):
    return {
        "session": session,
        "method": "GET",
        "host": hosts.cc,
        "endpoint": f"/cc/risk/rest/v1/scenarios/{scenario_id}",
        **kwargs
    }


@api
def get_risk_scenarios(session, scenario_name=None, page_number=None, page_size=None, sort_by=None, direction=None, **kwargs):

    params = {
        "scenarioId": scenario_name,
        "pageNumber": page_number,
        "pageSize": page_size,
        "sortBy": sort_by,
        "direction": direction
    }

    return {
        "session": session,
        "method": "GET",
        "host": hosts.cc,
        "endpoint": "/cc/risk/rest/v1/scenarios",
        "params": params,
        **kwargs
    }


@api
def get_player_risk_exceptions(session, player_id, **kwargs):
    return {
        "session": session,
        "method": "GET",
        "host": hosts.cc,
        "endpoint": f"/cc/risk/rest/v1/risk-exceptions/players/{player_id}",
        **kwargs
    }


def get_active_risk_exceptions_for_player(session, player_id, scenario_id):

    params = {}
    if player_id:
        params["playerId"] = player_id
    if scenario_id:
        params["scenarioId"] = scenario_id

    return {
        "session": session,
        "method": "GET",
        "host": hosts.cc,
        "endpoint": "/cc/risk/rest/v1/active-risk-exceptions"
    }
