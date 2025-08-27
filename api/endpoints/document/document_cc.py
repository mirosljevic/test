from api.executor import api
from environment import hosts


@api
def get_documents(session, player_id, **kwargs):
    return {
        "session": session,
        "method": "GET",
        "host": hosts.cc,
        "endpoint": "/cc/document/rest/v1/documents",
        "params": {"playerId": player_id},
        **kwargs,
    }


@api
def get_document_requests(session, player_id, **kwargs):
    return {
        "session": session,
        "method": "GET",
        "host": hosts.cc,
        "endpoint": "/cc/document/rest/v1/requests",
        "params": {"status": "REQUESTED", "playerId": player_id, "unlinked": "true"},
        **kwargs,
    }
