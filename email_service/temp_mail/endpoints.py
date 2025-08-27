from api.executor import api
from .config import HOST


@api
def get_domains():
    return {
        "method": "get",
        "host": HOST,
        "endpoint": "/domains",
        "expected_status_code": 200,
        "validate_response": True
    }


@api
def create_account(email, password):
    return {
        "method": "post",
        "host": HOST,
        "endpoint": "/accounts",
        "json": {"address": email, "password": password},
        "expected_status_code": 201,
        "validate_response": True
    }


@api
def get_token(email, password):
    return {
        "method": "post",
        "host": HOST,
        "endpoint": "/token",
        "json": {"address": email, "password": password},
        "expected_status_code": 200,
        "validate_response": True
    }


@api
def get_messages(token):
    return {
        "method": "get",
        "host": HOST,
        "endpoint": "/messages",
        "bearer_token": token,
        "expected_status_code": 200,
        "validate_response": True
    }


@api
def get_message(token, message_id):
    return {
        "method": "get",
        "host": HOST,
        "endpoint": f"/messages/{message_id}",
        "bearer_token": token,
        "expected_status_code": 200,
        "validate_response": True
    }