from api.executor import api
from environment import hosts


@api
def quick_pick(session, app_name, game_id, row_count=1, **kwargs):
    return {
        "session": session,
        "method": "get",
        "host": hosts.gateway_web,
        "endpoint": f"/web/{app_name}/rest/games/{game_id}/quickpick?rowCount={row_count}",
        **kwargs
    }
