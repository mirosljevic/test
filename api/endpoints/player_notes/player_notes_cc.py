from api.executor import api
from environment import hosts


@api
def add_notes(session, player_id, case_id, text, **kwargs):
    payload = {
        "caseIds": [case_id],
        "categoryId": 6,
        "contactType": "INTERNAL",
        "externalId": "",
        "isConfidential": False,
        "noteText": text,
        "noteType": "CASE",
        "playerId": player_id,
        "subcategoryId": 22
    }
    return {
        "session": session,
        "method": "POST",
        "host": hosts.cc,
        "endpoint": "/cc/player-notes/rest/v1/notes",
        "json": payload,
        **kwargs
    }
