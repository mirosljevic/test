from api.executor import api
from environment import hosts, credentials


@api
def get_access_token(**kwargs):
    payload = (f"grant_type={credentials.grant_type}&client_id={credentials.client_id}"
               f"&client_secret={credentials.client_secret}")

    return {
        "host": hosts.keycloak,
        "endpoint": "/auth/realms/b2b/protocol/openid-connect/token",
        "method": "POST",
        "content_type": "application/x-www-form-urlencoded",
        "data": payload,
        **kwargs
    }
