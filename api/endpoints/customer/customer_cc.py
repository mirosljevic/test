from api.executor import api
from environment import hosts


@api
def confirm_verification(session, player_id, **kwargs):
    return {
        "session": session,
        "method": "POST",
        "host": hosts.cc,
        "endpoint": f"/cc/customer/rest/v1/players/{player_id}/verifications/confirm",
        **kwargs
    }


@api
def get_verifications(session, player_id, **kwargs):
    return {
        "session": session,
        "host": hosts.cc,
        "endpoint": f"/cc/customer/rest/v1/players/{player_id}/verifications",
        **kwargs
    }


@api
def get_segments(session, player_id, **kwargs):
    return {
        "session": session,
        "host": hosts.cc,
        "endpoint": f"/cc/customer/rest/v2/players/{player_id}/segments",
        **kwargs
    }


@api
def find_players(session, search_term, page_number=1, page_size=10, **kwargs):
    return {
        "session": session,
        "host": hosts.cc,
        "endpoint": "/cc/customer/rest/v2/players",
        "params": {
            "searchTerm": search_term,
            "pageNumber": page_number,
            "pageSize": page_size
        },
        **kwargs
    }


@api
def request_verifications(session, player_id, ssn, **kwargs):
    return {
        "session": session,
        "method": "POST",
        "host": hosts.cc,
        "endpoint": f"/cc/customer/rest/v1/players/{player_id}/verifications/request-verifications",
        "json": [{
            "data": ssn,
            "verificationType": "SSN9"
        }],
        **kwargs
    }
