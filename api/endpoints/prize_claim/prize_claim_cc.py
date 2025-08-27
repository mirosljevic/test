from api.executor import api
from environment import hosts


@api
def get_w2g_cc(session, claim_id, **kwargs):
    return {
        "session": session,
        "method": "GET",
        "host": hosts.cc,
        "endpoint": f"/cc/prizeclaim/rest/v1/w2g-forms/{claim_id}",
        **kwargs
    }
