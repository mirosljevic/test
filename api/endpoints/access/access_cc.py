from api.executor import api
from environment import hosts


@api
def get_feature_sets(session, player_id, **kwargs):
    return {
        "session": session,
        "host": hosts.cc,
        "endpoint": f"/cc/access/rest/v1/customers/{player_id}/feature-sets",
        **kwargs
    }


@api
def get_current_user(session, **kwargs):
    return {
        "session": session,
        "host": hosts.cc,
        "endpoint": "/cc/access/rest/v1/sessions/current",
        **kwargs
    }
