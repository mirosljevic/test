from api.executor import api
from environment import hosts


@api
def get_w2g_web(session, claim_id, **kwargs):

    return {
        "session": session,
        "method": "get",
        "host": hosts.gateway_web,
        "endpoint": f"/web/prizeclaim/rest/v1/w2g-forms/{claim_id}",
        **kwargs
    }
