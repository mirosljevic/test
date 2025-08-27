from api.executor import api
from environment import hosts


@api
def get_oidc_login(session=None):
    return {
        "session": session,
        "method": "GET",
        "host": hosts.cc,
        "endpoint": "/cc/gateway/oidc/login",
        "allow_redirects": False,
        "validate_response": True,
        "expected_status_code": 302,
        "log_response": False
    }


@api
def get_adfs_login_link(session, location):
    return {
        "session": session,
        "method": "GET",
        "endpoint": location,
        "validate_response": True,
        "expected_status_code": 200,
        "log_response": False
    }


@api
def get_saml_post_binding(session, link):
    return {
        "session": session,
        "method": "GET",
        "endpoint": link,
        "validate_response": True,
        "expected_status_code": 200,
        "log_response": False
    }


@api
def get_adfs_client_request(session, action, saml_request, relay_state):
    return {
        "session": session,
        "method": "POST",
        "endpoint": action,
        "content_type": "application/x-www-form-urlencoded",
        "data": {
            "SAMLRequest": saml_request,
            "RelayState": relay_state
        },
        "validate_response": True,
        "expected_status_code": 200,
        "log_response": False
    }


@api
def authenticate_operator(session, action, username, password):
    return {
        "session": session,
        "method": "POST",
        "endpoint": action,
        "content_type": "application/x-www-form-urlencoded",
        "data": {
            "username": username,
            "password": password
        },
        "validate_response": True,
        "expected_status_code": 200,
        "log_response": False
    }


@api
def finalize_login(session, action, saml_response, relay_state):
    return {
        "session": session,
        "method": "POST",
        "endpoint": action,
        "content_type": "application/x-www-form-urlencoded",
        "data": {
            "SAMLResponse": saml_response,
            "RelayState": relay_state
        },
        "validate_response": True,
        "expected_status_code": 200,
        "log_response": False
    }
