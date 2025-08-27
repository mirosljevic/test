from api.executor import api
from environment import hosts
from .config import MAILINATOR_DOMAIN, MAILINATOR_TOKEN, MAILINATOR_HOST


@api
def get_messages(session, username):
    return {
        "session": session,
        "method": "get",
        "host": MAILINATOR_HOST,
        "endpoint": f"/api/v2/domains/{MAILINATOR_DOMAIN}/inboxes/{username}",
        "params": {
            "limit": "1",
            "sort": "descending",
            "token": MAILINATOR_TOKEN
        },
        "validate_response": True,
        "log_response": False
    }

@api
def get_message(session, username, message_id):
    return {
        "session": session,
        "method": "get",
        "host": MAILINATOR_HOST,
        "endpoint": f"/api/v2/domains/{MAILINATOR_DOMAIN}/inboxes/{username}/messages/{message_id}",
        "validate_response": True,
        "log_response": False,
    }