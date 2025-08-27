from api.executor import api
from environment import hosts


@api
def get_oidc_login(session=None):
    return {
        "session": session,
        "host": hosts.gateway_web,
        "endpoint": "/web/gateway/oidc/login",
        "allow_redirects": False,
        "validate_response": True,
        "expected_status_code": 302,
        "log_response": False
    }


@api
def get_keycloak_player_login(session, location):
    return {
        "session": session,
        "endpoint": location,
        "validate_response": True,
        "log_response": False
    }


@api
def authenticate_player(session, action, email, password):
    return {
        "session": session,
        "method": "POST",
        "endpoint": action,
        "content_type": "application/x-www-form-urlencoded",
        "data": {"username": email, "password": password},
        "validate_response": True,
        "log_response": False
    }
