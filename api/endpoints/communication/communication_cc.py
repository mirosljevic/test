from api.executor import api
from environment import hosts


@api
def get_emails(session, player_id, **kwargs):
    return {
        "session": session,
        "host": hosts.cc,
        "endpoint": "/cc/communication/rest/v2/emails",
        "params": {
            "playerId": player_id
        },
        **kwargs
    }
