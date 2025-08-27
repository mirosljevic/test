from api.executor import api
from environment import hosts


@api
def get_bonus_availability(session, player_id, game, amount, **kwargs):
    payload = {
        "games": [
            {
                "gameId": game,
                "amount": amount
            }
        ]
    }
    return {
        "session": session,
        "method": "POST",
        "host": hosts.gateway_web,
        "endpoint": f"/web/bonus/rest/v1/player-bonuses/{player_id}/availability",
        "json": payload,
        **kwargs
    }
