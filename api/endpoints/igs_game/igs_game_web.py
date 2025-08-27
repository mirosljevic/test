from api.executor import api
from environment import hosts


@api
def game_step(session, game_id, method_name, request_token=None, session_id=None, method_parameters=None, **kwargs):
    return {
        "session": session,
        "host": hosts.gateway_web,
        "endpoint": f"/web/igs-game/games/{game_id}",
        "method": "POST",
        "json": {
            "clientRequestToken": request_token,
            "clientSessionId": session_id,
            "methodName": method_name,
            "methodParameters": method_parameters if method_parameters else []
        },
        **kwargs
    }
