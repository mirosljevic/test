from api.executor import api
from environment import hosts


@api
def get_bonus_campaign(session, player_bonus_id):
    return {
        "session": session,
        "method": "GET",
        "host": hosts.cc,
        "endpoint": f"/cc/bonus/rest/v1/bonus-campaigns/{player_bonus_id}",
    }


@api
def get_bonus_objects(session, bonus_object=None, page_number=1, page_size=10, **kwargs):
    return {
        "session": session,
        "method": "GET",
        "host": hosts.cc,
        "endpoint": "/cc/bonus/rest/v1/bonus-objects/",
        "params": {
            "searchTerm": bonus_object,
            "pageNumber": page_number,
            "pageSize": page_size
        },
        **kwargs
    }


@api
def create_bonus_object(session, bonus_data, **kwargs):
    return {
        "session": session,
        "method": "POST",
        "host": hosts.cc,
        "endpoint": "/cc/bonus/rest/v1/bonus-objects",
        "json": bonus_data,
        **kwargs
    }


@api
def archive_bonus_object(session, bonus_object_id, **kwargs):
    return {
        "session": session,
        "method": "POST",
        "host": hosts.cc,
        "endpoint": f"/cc/bonus/rest/v1/bonus-objects/archive/{bonus_object_id}",
        **kwargs
    }


@api
def get_bonus_object_with_requested_id(session, bonus_object_id, **kwargs):
    return {
        "session": session,
        "method": "GET",
        "host": hosts.cc,
        "endpoint": f"/cc/bonus/rest/v1/bonus-objects/{bonus_object_id}",
        **kwargs
    }


@api
def update_bonus_object(session, bonus_object_id, payload, **kwargs):
    return {
        "session": session,
        "method": "PUT",
        "host": hosts.cc,
        "endpoint": f"/cc/bonus/rest/v1/bonus-objects/{bonus_object_id}",
        "json": payload,
        **kwargs
    }


@api
def get_all_bonus_objects_for_manual_payout(session, **kwargs):
    return {
        "session": session,
        "method": "GET",
        "host": hosts.cc,
        "endpoint": "/cc/bonus/rest/v1/bonus-objects/manual",
        **kwargs
    }


@api
def get_player_bonus_history(session, player_id, **kwargs):
    return {
        "session": session,
        "method": "GET",
        "host": hosts.cc,
        "endpoint": f"/cc/bonus/rest/v1/player-bonuses/history/{player_id}",
        **kwargs
    }
