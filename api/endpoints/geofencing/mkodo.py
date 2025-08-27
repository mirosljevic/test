import time
import jwt
import uuid
import base64
from typing import Optional
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
from requests import Session
from api.executor import api
from environment import hosts, geofencing



@api
def authenticate(**kwargs):
    return {
        "method": "post",
        "host": hosts.mkodo,
        "endpoint": "/gateway/authenticate",
        "json": {
            "gatewayAcl": geofencing.token
        },
        "validate_response": True,
        "expected_status_code": 204,
        "log_response": False,
        **kwargs
    }


@api
def get_mkodo_token(session, client_id):
    return {
        "method": "post",
        "host": hosts.mkodo,
        "endpoint": "/csrftoken",
        "session": session,
        "headers": {
            "x-client-id": client_id
        },
        "log_response": True
    }


@api
def send_ping(
        session: Session,
        player_id: str,
        session_state: str,
        client_secret: str,
        client_id: str,
        latitude: Optional[str] = None,
        longitude: Optional[str] = None,
        csrf_token: Optional[str] = None,
        public_key: Optional[str] = None):
    data = _ping_data(player_id, session_state, latitude, longitude)

    try:
        if geofencing.csrf_enabled:
            jwt_token = jwt.encode(data, client_secret, algorithm="HS256")
            header, payload, signature = jwt_token.split('.')
            signature = signature.encode('utf-8')

            public_key_bytes = base64.b64decode(public_key)

            public_key = serialization.load_der_public_key(public_key_bytes)
            encrypted_signature = public_key.encrypt(
                signature,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            jwt_token = f"{header}.{payload}.{base64.b64encode(encrypted_signature).decode('utf-8')}"

            headers = {
                "x-client-id": client_id,
                "x-gateway-geo-service": "async",
                "x-gateway-geo-vault": jwt_token,
                "x-gateway-geo-csrf-token": csrf_token,
                "x-gateway-geo-transaction-id": str(uuid.uuid4())
            }
        else:
            headers = {
                "x-client-id": client_id,
                "X-Gateway-Geo-Service": "async",
                "X-Gateway-Geo-Vault": jwt.encode(data, client_secret, algorithm="HS256")
            }
    except Exception as e:
        raise

    return {
        "method": "POST",
        "host": hosts.mkodo,
        "endpoint": "/ping",
        "session": session,
        "headers": headers,
        "expected_status_code": 204,
        "log_response": True
    }


def _ping_data(
        player_id: str,
        session_state: str,
        latitude: str,
        longitude: str):
    return {
        "device": {
            "screenRatio": geofencing.screen_ratio,
            "utcOffset": geofencing.utc_offset,
            "platform": geofencing.platform,
            "gpu": geofencing.gpu,
            "userAgent": geofencing.user_agent,
            "staticDevice": geofencing.static_device
        },
        "location": {
            "accuracy": geofencing.accuracy,
            "latitude": latitude,
            "longitude": longitude,
            "trust": geofencing.trust
        },
        "source": geofencing.source,
        "state": {
            "code": "OK"
        },
        "sdkVersion": geofencing.sdk_version,
        "version": 1,
        "identities": {
            "plrUniqueIdentity": player_id,
            "sessionState": session_state
        },
        "debug": {
            "devToolsExecTime": 0,
            "ifrLoc": "0.000003|-0.000007"
        },
        "activity": "scheduled-ping",
        "iat": int(time.time() * 1000),
        "iss": "mkodo"
    }