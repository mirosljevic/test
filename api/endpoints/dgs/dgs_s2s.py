from api.executor import api
from environment import hosts
import json


@api
def get_draw(access_token, app_name, game_id, draw_id, **kwargs):
    return {
        "host": hosts.api,
        "endpoint": f"/api/{app_name}/rest/dgs/v1/games/{game_id}/draws/{draw_id}",
        "bearer_token": access_token,
        **kwargs
    }


@api
def get_draws(access_token, app_name, game_id, status, **kwargs):
    return {
        "host": hosts.api,
        "endpoint": f"/api/{app_name}/rest/dgs/v1/games/{game_id}/draws/{status}?pageNumber=1&pageSize=100",
        "bearer_token": access_token,
        **kwargs
    }


@api
def get_available_draws(access_token, app_name, game_id, date, **kwargs):
    return {
        "host": hosts.api,
        "endpoint": f"/api/{app_name}/rest/dgs/v1/games/{game_id}/draws/available?date={date}",
        "bearer_token": access_token,
        **kwargs
    }


@api
def get_draw_results(access_token, app_name, game_id, draw_id, **kwargs):
    return {
        "host": hosts.api,
        "endpoint": f"/api/{app_name}/rest/dgs/v1/games/{game_id}/draws/{draw_id}/results",
        "bearer_token": access_token,
        **kwargs
    }


@api
def get_games(access_token, app_name, **kwargs):
    return {
        "host": hosts.api,
        "endpoint": f"/api/{app_name}/rest/dgs/v1/games",
        "bearer_token": access_token,
        **kwargs
    }


@api
def set_game_content_for_draw(access_token, app_name, game_id, draw_id, content_key, payload, **kwargs):
    return {
        "host": hosts.api,
        "method": "PUT",
        "json": payload,
        "endpoint": f"/api/{app_name}/rest/dgs/v1/gamecontent/{game_id}/draws/{draw_id}/{content_key}",
        "bearer_token": access_token,
        **kwargs
    }


@api
def enter_winning_numbers(access_token, app_name, game_id, draw_id, payload, **kwargs):
    return {
        "host": hosts.api,
        "method": "PUT",
        "endpoint": f"/api/{app_name}/rest/dgs/v1/games/{game_id}/draws/{draw_id}/results",
        "json": payload,
        "bearer_token": access_token,
        "headers": {
            "x-Admin-id": '3'
        },
        **kwargs
    }


@api
def confirm_winning_numbers(access_token, app_name, game_id, draw_id, payload, **kwargs):
    return {
        "host": hosts.api,
        "method": "POST",
        "endpoint": f"/api/{app_name}/rest/dgs/v1/games/{game_id}/draws/{draw_id}/results",
        "json": payload,
        "bearer_token": access_token,
        "headers": {
            "x-Admin-id": '4'
        },
        **kwargs
    }


@api
def confirm_winners(access_token, app_name, game_id,  draw_id, **kwargs):
    return {
        "host": hosts.api,
        "method": "POST",
        "endpoint": f"/api/{app_name}/rest/dgs/v1/games/{game_id}/draws/{draw_id}/confirm",
        "bearer_token": access_token,
        "headers": {
            "x-Admin-id": '3'
        },
        **kwargs
    }


@api
def backend_check_status(access_token, app_name, process_name, run_id, **kwargs):
    return {
        "host": hosts.api,
        "method": "GET",
        "endpoint": f"/api/{app_name}/rest/dgs/v1/backends/{process_name}/{run_id}",
        "bearer_token": access_token,
        **kwargs
    }


@api
def backend_enter_and_confirm_winning_numbers(access_token, app_name, game_id, draw_id, draw_results, **kwargs):
    payload = {
        "processParameters": ["-gameId", game_id, "-drawId", draw_id, "-drawResults", json.dumps(draw_results)]
    }
    return {
        "host": hosts.api,
        "method": "POST",
        "endpoint": f"/api/{app_name}/rest/dgs/v1/backends/enterconfirmdrawresults",
        "json": payload,
        "bearer_token": access_token,
        **kwargs
    }


@api
def backend_winnerscan(access_token, app_name, game_id, draw_id, **kwargs):
    payload = {
        "processParameters": ["-gameId", game_id, "-drawId", draw_id]
    }
    return {
        "host": hosts.api,
        "method": "POST",
        "endpoint": f"/api/{app_name}/rest/dgs/v1/backends/winnerscan",
        "json": payload,
        "bearer_token": access_token,
        **kwargs
    }


@api
def backend_winnerselection(access_token, app_name, game_id, draw_id, **kwargs):
    payload = {
        "processParameters": ["-gameId", game_id, "-drawId", draw_id]
    }
    return {
        "host": hosts.api,
        "method": "POST",
        "endpoint": f"/api/{app_name}/rest/dgs/v1/backends/winnerselection",
        "json": payload,
        "bearer_token": access_token,
        **kwargs
    }


@api
def backend_payout(access_token, app_name, game_id,  draw_id, **kwargs):
    payload = {
        "processParameters": ["-gameId", game_id, "-drawId", draw_id]
    }
    return {
        "host": hosts.api,
        "method": "POST",
        "endpoint": f"/api/{app_name}/rest/dgs/v1/backends/prizepayout",
        "json": payload,
        "bearer_token": access_token,
        **kwargs
    }
