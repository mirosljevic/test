from api.executor import api
from environment import hosts


@api
def get_activities(session, **kwargs):
    return {
        "session": session,
        "host": hosts.cc,
        "endpoint": "/cc/activity/rest/v1/activities",
        **kwargs
    }
