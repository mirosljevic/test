from api.executor import api
from environment import hosts


@api
def get_messages(email):
    return {
        "method": "get",
        "host": hosts.mailhog,
        "endpoint": "/api/v2/search",
        "params": {
            "kind": "containing",
            "query": email
        },
        "validate_response": True,
        "log_response": False
    }