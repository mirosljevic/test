from api.executor import api
from environment import hosts


@api
def get_player_bonus(access_token, player_bonus_id, **kwargs):
    return {
        "bearer_token": access_token,
        "host": hosts.api,
        "method": "get",
        "endpoint": f"/api/bonus/rest/v1/player-bonuses/{player_bonus_id}",
        **kwargs
    }


@api
def get_player_bonuses(access_token, player_id, game_id=None, game_type=None, **kwargs):
    return {
        "bearer_token": access_token,
        "host": hosts.api,
        "endpoint": "/api/bonus/rest/v1/bonus-prizes",
        "params": {
            "playerId": player_id,
            "gameId": game_id,
            "gameType": game_type,
        },
        **kwargs
    }


@api
def achieve_bonus(access_token, player_id, bonus_object_id, external_campaign_id, status, time_stamp, condition_met,
                  event_data, **kwargs):
    payload = {
        "playerIds": [player_id],
        "bonusObjectIds": [bonus_object_id],
        "campaignId": external_campaign_id,
        "status": status,
        "timestamp": time_stamp,
        "conditionMet": condition_met,
        "eventData": event_data
    }

    return {
        "bearer_token": access_token,
        "host": hosts.api,
        "method": "PUT",
        "endpoint": "/api/bonus/rest/v1/tracking-events",
        "json": payload,
        **kwargs
    }


@api
def create_bonus_campaign(access_token, external_campaign_id, name, bonus_object_ids, number_of_triggers, valid_from,
                          valid_to, data, triggers, **kwargs):
    payload = {
        "name": name,
        "bonusObjectIds": bonus_object_ids,
        "numberOfTriggers": number_of_triggers,
        "validFrom": valid_from,
        "validTo": valid_to,
        "data": data,
        "triggers": triggers
    }
    return {
        "bearer_token": access_token,
        "host": hosts.api,
        "endpoint": f"/api/bonus/rest/v1/bonus-campaigns/{external_campaign_id}",
        "method": "PUT",
        "json": payload,
        **kwargs
    }


@api
def get_audit_history(access_token, object_type, object_id=None, **kwargs):
    return {
        "bearer_token": access_token,
        "host": hosts.api,
        "endpoint": "/api/bonus/rest/v1/audit-history",
        "params": {
            "objectType": object_type,
            "objectId": object_id
        },
        **kwargs
    }


@api
def process_buy_requests_from_wallet(access_token, user_id, payload, **kwargs):
    return {
        "bearer_token": access_token,
        "host": hosts.api,
        "endpoint": f"/api/bonus/rest/v1/users/1-{user_id}/funds",
        "method": "POST",
        "json": payload,
        **kwargs
    }


@api
def manual_bonus_payout(access_token, payload, **kwargs):
    return {
        "bearer_token": access_token,
        "host": hosts.api,
        "endpoint": "/api/bonus/rest/v1/player-bonuses/payout",
        "method": "POST",
        "json": payload,
        **kwargs
    }
