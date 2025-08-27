from api.executor import api
from environment import hosts


@api
def get_message_preferences(session, player_id, **kwargs):
    return {
        "session": session,
        "method": "get",
        "host": hosts.gateway_web,
        "endpoint": f"/web/communication/rest/v1/messages-preferences/{player_id}",
        "log_response": True,
        **kwargs
    }
